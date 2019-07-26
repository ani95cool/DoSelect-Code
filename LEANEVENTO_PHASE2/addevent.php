<?php 


$eventname = $_POST["event_name"];
$response = $_POST["responsible"];
$address = $_POST["place"];
$date = $_POST["date"];
$hour = $_POST["hour"];
$price = $_POST["price"];
$dbname = "leaneventos";
$servername = "localhost";
$password = "";
$username = "root";

//$_SESSION["event"] = $eventname;






$con = mysqli_connect($servername, $username, $password, $dbname);
if($con){
	echo "<script>
	alert('Database is connected');
	</script>";
}
else{
	print 'Database'. $dbname . ' is not connected';
}

$sql = "INSERT INTO `event` (`Name`, `Responsible`, `Address`, `Date`, `Time`, `Donation`) VALUES ('$eventname','$response','$address','$date','$hour','$price');";
$res = mysqli_query($con,$sql);

	if($res){
		echo "<script>
		alert('We have been notified of your application please wait for our reply!!!');
		window.location.href='add_Event.php';
		</script>";

	}else{
		print mysqli_error($con);
	}







?>