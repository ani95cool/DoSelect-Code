<?php 


session_start();
   $user = $_POST["user"];
   $pass = $_POST["pass"];
   $dbname = "leaneventos";
   $servername = "localhost";
   $password = "";
   $idname = "root";
   $_SESSION["email_id"] = $user;

   


   function sign_me_in($user, $mypass, $fecthed_email, $fetched_password, $con){
       $sql2 = "SELECT `Firstname` FROM `individual` WHERE `Email` = '$user' AND `Password` = '$mypass' ";
       $result2 = mysqli_query($con, $sql2);

       if(mysqli_num_rows($result2) > 0){
        $select = mysqli_fetch_assoc($result2);
        echo "<script>
        window.location.href='home_individual.php';
        </script>";


       }else{
        print "";
       }


   }

   function Logmein($user, $mypass, $con){
      $sql = "SELECT `Email`, `Password` FROM `individual` WHERE `Email` = '$user' AND `Password` = '$mypass' ";
      print  $sql;
      $result = mysqli_query($con, $sql);

      if(mysqli_num_rows($result) > 0){
        $row = mysqli_fetch_assoc($result);
          $fecthed_email = $row["Email"];
          $fetched_password = $row["Password"];
          if($row["Email"] == $user && $row["Password"] == $mypass){
            sign_me_in($user, $mypass, $fecthed_email, $fetched_password, $con);
          }else{
            print "Nothing found";

          }
        
      }

   }

   $con = mysqli_connect($servername, $idname, $password, $dbname);
   if($con){
    echo "<script>
    alert('The data base is connected');
    </script>";

   }else{
    echo "Error: " . mysqli_error($con);
   }

   Logmein($user, $pass, $con); 
?> 