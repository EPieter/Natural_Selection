<?php
$db_server = "db.nsgame.nl";
$db_username = "md488088db551267";
$db_password = "NaturalSelection2021!";
$db_name = "md488088db551267";

// Create connection
$conn = mysqli_connect($db_server, $db_username, $db_password, $db_name);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // collect value of input field
    if (isset($_POST['method'])) {
        switch ($_POST['method']) {
            case 'get_user_data':
                echo('get user data');
                break;
            case 'create_new_user':
                echo('new user');
                break;
            default:
                echo('error');
        }
    } else {
        echo('There is an error');
    }
  }
?>
