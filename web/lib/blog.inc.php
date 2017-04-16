<?php

set_include_path(get_include_path() . PATH_SEPARATOR . "../templates");

function get_comments_from_post($post_id) {
    $dbh = DB::connect();

    $q = "SELECT id, name, body, post, ts ";
    $q.= "FROM BlogComments ";
    $q.= "WHERE post = " . intval($post_id) . " ";
    $q.= "ORDER BY ts";

    $result = $dbh->query($q);

    $ret = array();
    while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
        $ret[] = $row;
    }

    return $ret;
}

function display_blog_post($id) {
    $dbh = DB::connect();

    $q = "SELECT p.title as title, p.body as body, ";
    $q.= "p.created as created, p.edited as edited, u.username as username ";
    $q.= "FROM BlogPosts p ";
    $q.= "LEFT JOIN Users u ON p.user = u.id ";
    $q.= "WHERE p.id = " . intval($id);

    $result = $dbh->query($q);
    $row = $result->fetch(PDO::FETCH_ASSOC);

    if (!$row) {
        header("HTTP/1.0 404 Not Found");
        include "404.php";
        return;
    }

    $comments = get_comments_from_post($id);

    html_header("Blog - " . $row["title"]);
    include "post.php";
    include "comments.php";
    html_footer();
}

function display_blog_list($start=0, $num=10) {
    $last = $start + $num;

    $dbh = DB::connect();


}