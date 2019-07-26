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
$dbname = "leaneventos";
$servername = "localhost";
$password = "";
$username = "root";
$_SESSION["email_id"] = $email;

$con = mysqli_connect($servername, $username, $password, $dbname);
if($con){
	echo "<script>
	alert('Database is connected');
	</script>";
}
else{
	print 'Database'. $dbname . ' is not connected';
}

$sql = "SELECT `Email`FROM `organizations` WHERE `Email` = '$email' ";
$result = mysqli_query($con, $sql);

if(mysqli_num_rows($result) > 0){
	$row = mysqli_fetch_assoc($result);
	if($row["Email"] == $email){
		echo "<script>
		alert('User Already has Registered');
		window.location.href='Register_Organization.html';
		</script>";
	}
		
}
$sql2 = "INSERT INTO `organizations` (`Email`, `Password`, `Firstname`, `Surname`, `City`, `Address`, `State`, `Zip`, `Type`) VALUES ('$email','$pass','$firstname','$surname','$city','$address','$state','$zip', '$type');";
$res = mysqli_query($con,$sql2);

	if($res){
		echo "<script>
		alert('User ".$firstname." has Registered');
		window.location.href='home_business.php';
		</script>";

	}else{
		print "Not done";
	}


?>