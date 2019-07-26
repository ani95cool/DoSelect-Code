<?php 
session_start();

?>

<?php
$email = $_POST["correo"];
$pass = $_POST["contrasena"];
$firstname = $_POST["nombre"];
$surname = $_POST["apellido"];
$city = $_POST["ciudad"];
$address = $_POST["direccion"];
$state = $_POST["estado"];
$zip = $_POST["codigo"];
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

$sql = "SELECT `Email`FROM `individual` WHERE `Email` = '$email' ";
$result = mysqli_query($con, $sql);

if(mysqli_num_rows($result) > 0){
	$row = mysqli_fetch_assoc($result);
	if($row["Email"] == $email){
		echo "<script>
		alert('User Already has Registered');
		window.location.href='Individual.html';
		</script>";
	}
		
}
$sql2 = "INSERT INTO `individual` (`Email`, `Password`, `Firstname`, `Surname`, `City`, `Address`, `State`, `Zip`) VALUES ('$email','$pass','$firstname','$surname','$city','$address','$state','$zip');";
$res = mysqli_query($con,$sql2);

	if($res){
		echo "<script>
		alert('User ".$firstname." has Registered');
		alert('Please Log in');
		window.location.href='home_individual.php';
		</script>";

	}else{
		print "Not done";
	}

print "Hey";



?>