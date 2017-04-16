<?php
set_include_path(get_include_path() . PATH_SEPARATOR . "../templates");
date_default_timezone_set("America/Detroit");

include_once "DB.class.php";
include_once "blog.inc.php";
include_once "alpm-repo.inc.php";

function html_header($title="") {
    include "header.php";
}

function html_footer() {
    include "footer.php";
}