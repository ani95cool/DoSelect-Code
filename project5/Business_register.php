<?php 
session_start();
$email = $_POST["user"];
$pass = $_POST["contrasena"];
$firstname = $_POST["nombre"];
$surname = $_POST["apellido"];
$city = $_POST["ciudad"];
$address = $_POST["direccion"];
$state = $_POST["estado"];
$zip = $_POST["codigo"];
$type = $_POST["type"];
$dbname = "anirudhr_leaneventos";
   $servername = "uta.cloud";
   $password = "root123@uta";
   $idname = "anirudhr_lean";
$_SESSION["email_id"] = $email;

if ($_SERVER["REQUEST_METHOD"] == "POST"){

      if(!empty($_POST["correo"])){
        $email=$_POST["correo"];
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
          $error_msg = "Invalid email id";
          $error_flag = true;
        }

        }
      if(!empty($_POST["contrasena"])){
        $pswd=$_POST["contrasena"];
        $pswd_pat = "/(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20}/";
        if(!preg_match($pswd_pat, $pswd))
          {
            $error_msg = "Invalid password format";
            $error_flag = true;
          }

      }
      if(!empty($_POST["nombre"])){
        //$fname=$_POST["nombre"];
        $fname_pat = "/^(?!.*__.*)(?!.*\.\..*)[a-zA-Z_.]+$/";
        if(!preg_match($fname_pat, $fname)){
          $error_msg = "Invalid firstname format";
          $error_flag = true;
        }

      }
      if(!empty($_POST["apellido"])){
          //$lname=$_POST["apellido"];
          $lname_pat = "/^(?!.*__.*)(?!.*\.\..*)[a-zA-Z_.]+$/";
          if(!preg_match($lname_pat, $lname)){

            $error_msg = "Invalid lastname format"; 
            $error_flag = true;
          }

      }
      if(!empty($_POST["direccion"])){
          //$addr=$_POST["address"];
          $addr_pat = "/^[a-zA-Z0-9\s,.'-]{3,}$/";
          if(!preg_match($addr_pat, $addr)){

            $error_msg = "Invalid address format";
            $error_flag = true;
          }

      }
      if(!empty($_POST["ciudad"])){
          //$city=$_POST["city"];
          $city_pat = "/^(?!.*__.*)(?!.*\.\..*)[a-zA-Z_.]+$/";
          if(!preg_match($city_pat, $city)){
            $error_msg = "Invalid firstname format"; 
            $error_flag = true;
          }

      }
      if(!empty($_POST["codigo"])){
          //$zipcode=$_POST["zipcode"];
          $zipcode_pat = "/(?=.*\d)\w{5,10}$/";
          if(!preg_match($zipcode_pat, $zipcode)){
          	$error_msg = "Invalid zipcode format";
            $error_flag = true;
          }
      }
      if(!$error_flag){
        //$state = $_POST['state'];
          $table_name = 'individual';
          $conn = mysqli_connect($servername, $username, $password, $dbname);
          $sql = "SELECT Email FROM '$table_name' where email='$email' ";
          $result = mysqli_query($conn, $sql);
          if (mysqli_num_rows($result) > 0) {
            $_SESSION["email_id"]= $email;
            echo "<script>
            alert('The user already exists');
            window.location.href='Individual.php';
            </script>";
            

          }
          else{
                echo $pswd;
                $sql = "INSERT INTO individual (email, password, fname, lname, address, city, state, zipcode,type) VALUES ('$email','$pass','$firstname','$surname','$address','$city','$state','$zip', '$type')";

                if (mysqli_query($conn, $sql)) {
                $_SESSION["email_id"]= $email;
                echo "<script>
            alert('The user already exists');
            window.location.href='home_individual.php';
            </script>";



              } else {
                  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
          }
        

      }

    }
?>