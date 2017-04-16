<?php
set_include_path(get_include_path() . PATH_SEPARATOR . "../lib" . PATH_SEPARATOR . "../templates");

if (!extension_loaded("alpm")) {
    die("Extension alpm not loaded!");
}

include_once "main.inc.php";

$path = isset($_SERVER["PATH_INFO"]) ? $_SERVER["PATH_INFO"] : "";
$tokens = explode("/", $path);
array_shift($tokens);

/* start routing pages */
if (!isset($tokens[0]) || $tokens[0] === "") {
    include_once "home.php";
} else if ($tokens[0] === "blog") {
    if (isset($tokens[1])) {
        if ($tokens[1] === "posts") {
            if (!isset($tokens[2]) || $tokens[2] === "") {
                header("Location: /blog");
            } else {

            }
        } else if ($tokens[1] === "id") {
            if (isset($tokens[2])) {
                if ($tokens[2] === "") {
                    header("Location: /blog");
                } else {
                    display_blog_post($tokens[2]);
                }
            } else {
                header("Location: /blog");
            }
        }
    } else {
       /* unused */
    }
} else if ($tokens[0] === "repos") {
    if (isset($tokens[1])) {
        display_repo_details($tokens[1]);
    } else {
        display_repo_list();
    }
}