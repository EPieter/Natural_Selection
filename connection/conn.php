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
            case 'check_if_user_exist':
                $sql = "
                    SELECT * FROM ns_users 
                    WHERE user_name = '".$_POST['user']."'
                ";
                $sql_n = mysqli_query($conn,$sql);
                $result_sql = mysqli_fetch_assoc($sql_n);
                if (mysqli_num_rows($sql_n) == 1) {
                    if ($_POST['password']==$result_sql['password']) {
                        echo('access');
                    } else {
                        echo('wrong_password');
                    }
                } elseif (mysqli_num_rows($sql_n) == 0) {
                    echo("no_user");
                } else {
                    echo("someting_went_wrong");
                }
                break;
            default:
                echo('error');
        }
    } else {
        echo('There is an error');
    }
  }
?>
