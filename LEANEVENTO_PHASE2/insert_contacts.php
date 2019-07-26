<?php 
$firstname = $_POST["number"];
$surname = $_POST["apellido"];
$email = $_POST["correo"];
$topic = $_POST["tema"];
$message = $_POST["description"];

$dbname = "leaneventos";
$servername = "localhost";
$password = "";
$idname = "root";

$con = mysqli_connect($servername, $idname, $password, $dbname);
if($con){
	echo "<script>
	alert('The database is connected!!');
	</script>";
}else{
	echo "Error: " . mysqli_error();
}

$sql = "INSERT INTO `contactinfo` (`firstname`, `surname`, `email`, `topic`, `message`) VALUES ('$firstname','$surname','$email','$topic','$message');";
$result = mysqli_query($con, $sql);

if($result){
	echo "<script>
	alert('congrats your details have been saved we will get back to you shortly');
	window.location.href='contacto.php';
	</script>";

	
}else{
	echo "<script>
	alert('I am sorry please try again someother time!!!');
	window.location.href='contacto.php';
	</script>";

}




?>