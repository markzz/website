<?php

include_once "../../config/config.php";

class DB {
    public static $dbh = null;

    public static function connect() {
        global $config;

        $backend = $config["DB"]["backend"];

        if (self::$dbh === null) {
            try {
                if ($backend == "pgsql") {
                    $dsn = $backend .
                        ":host" . $config["DB"]["host"] .
                        ";dbname" . $config["DB"]["dbname"];

                    self::$dbh = new PDO($dsn, $config["DB"]["user"], $config["DB"]["password"]);
                } else if ($backend == "sqlite") {
                    $dsn = $backend .
                        ":" . $config["DB"]["dbname"];

                    self::$dbh = new PDO($dsn, null, null);
                } else {
                    die ("database backend \"" . $backend . "\" unsupported!");
                }
            } catch (PDOException $e) {
                die("Could not connect to db!");
            }
        }

        return self::$dbh;
    }
}