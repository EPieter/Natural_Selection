<?php
include 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // collect value of input field
    if (isset($_POST['method'])) {
        switch ($_POST['method']) {
            case 'get_user_data':
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
                    echo("something_went_wrong|1");
                }
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
                    echo("something_went_wrong|3");
                }
                break;
            case 'make_new_user':
                echo('new user');
                break;
            default:
                echo('something_went_wrong|4');
        }
    } else {
        echo('something_went_wrong|2');
    }
  }
?>
