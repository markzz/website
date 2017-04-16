<?php

set_include_path(get_include_path() . PATH_SEPARATOR . "../templates");

function get_pkg_list($handle, $repo) {
    $db = $handle->register_syncdb($repo, ALPM_SIG_USE_DEFAULT);

    $ret = array();

    foreach ($db->pkgcache as $pkgname) {
        $ret[] = $db->get_pkg($pkgname);
    }

//    var_dump($ret);

    return $ret;
}

function get_pkg_from_db($pkgname, $db) {
    $handle = new AlpmHandle("/", "/var/lib/pacman");
    $db = $handle->register_syncdb($db, ALPM_SIG_USE_DEFAULT);
    return $db->get_pkg($pkgname);
}

function display_repo_list() {
    $dbh = DB::connect();

    $q = "SELECT id, name, url, signed, desc ";
    $q.= "FROM AlpmRepos";

    $result = $dbh->query($q);

    $repos = array();
    while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
        $repos[] = $row;
    }

    html_header("Arch Linux Repositories");
    include "repolist.php";
    html_footer();
}

function display_repo_details($repo) {
    $dbh = DB::connect();
    $handle = new AlpmHandle("/", "/var/lib/pacman");

    $q = "SELECT id, name, url, signed, desc ";
    $q.= "FROM AlpmRepos ";
    $q.= "WHERE name = " . $dbh->quote($repo);

    $result = $dbh->query($q);
    $row = $result->fetch(PDO::FETCH_ASSOC);

    if (!$row) {
        header("HTTP/1.0 404 Not Found");
        include "404.php";
        return;
    }

    $pkglist = get_pkg_list($handle, $repo);

    html_header("Repository - " . $repo);
    include "repodetails.php";
    html_footer();
}