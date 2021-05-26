<?php

class DB {
    protected static string $server;
    protected static string $user;
    protected static string $password;
    protected static string $dbname;
    protected static mysqli $connection;

    protected static function connectToDatabase($connect = false) {
        if ($connect) {
            DB::$connection = mysqli_connect(DB::$server, DB::$user, DB::$password, DB::$dbname);
        }
    }

    protected static function closeConnection($disconnect = true) {
        if ($disconnect) {
            mysqli_close(DB::$connection);
        }
    }

    protected static function executeRequest($to_execute): ?array
    {
        DB::connectToDatabase($connect = true);
        $result = mysqli_query(DB::$connection, $to_execute);
        DB::closeConnection();
        $result = mysqli_fetch_assoc($result);
        return $result;
    }
}