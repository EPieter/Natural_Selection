<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if ($_POST["try_to_connect"] == "give_return" && $_GET["url"]=="test_connection") {
        echo("connected");
    }
} else {
    header('HTTP/1.0 403 Forbidden');
}