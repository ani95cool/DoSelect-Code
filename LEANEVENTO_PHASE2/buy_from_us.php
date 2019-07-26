<?php
$dbname = "leaneventos";
$servername = "localhost";
$password = "";
$username = "root";
$con = mysqli_connect($servername, $username, $password, $dbname);
if($con){
	echo "<script>
	alert('Database is connected');
	</script>";
}
else{
	print 'Database'. $dbname . ' is not connected';
}

$sql = "SELECT `Name`, `Donation` FROM `event` ";
$result = mysqli_query($con, $sql);
$name_array = array();
$price_array = array();

if(mysqli_num_rows($result) > 0){
	//$row = mysqli_fetch_assoc($result);
	while($row = mysqli_fetch_assoc($result)){
		array_push($name_array, $row["Name"]);
		array_push($price_array, $row["Donation"]);
	}
	
		
}

//print $name_array;








//$sql = "SELECT `Donation`FROM `event` WHERE `Name` = '$email' ";





?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>LEANEVENTO website</title>
	 <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="sayitright.css">
	<style type="text/css">
		li img {font: bold 14px;}
		li img {width: 30px; height: 30px;}
		section img {width: 1200px; height: 320px;}
		div #c {text-align: center;}
		#top_menu ul{
			transform: translate(85%);

		}
		.one {
			border-radius: 5px;
		}

		.two {
			border-radius: 10px;
			transform: translate(-110%);
		}
		.description {
			transform: translate(40%);
		}
		.makeleft {
			left: 10px;
			transform: translate(1%);
		}
		.makebottom {
			left: 100px;
			transform: translate(1%);
		}
		
	</style>
</head>
<body>
	<div id="big_wrapper">
	<nav id="top_menu">
		<ul>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li style="font: bold 10px Roboto;"><img src="C:\xampp\htdocs\Deshpande_LEANEVENTO\imagenes\logo-blanco.png" />LEANEVENTOS</li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li><li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li class="new">Inicio</li>
			<li></li>
			<li></li>
			<li class="new">Quienes Somos</li>
			<li></li>
			<li></li>
			<li class="new">Blog</li>
			<li></li>
			<li></li>
			<li class="new">Contacto</li>
			<li></li>
			<li></li>
			<li class="new">Inciar Sesion</li>
			<li></li>
			<li></li>
			<li class="new" style="color: yellow;">Comparar Boletos</li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
		</ul>
	</nav>

	<section id="main_section">
		<br />
		<img src="C:\xampp\htdocs\Deshpande_LEANEVENTO\imagenes\lean_poaster.png" /><br /><br />
		<br /> <br />
		<br /> <br />
		<br /> <br />
		<br /> <br />
		<br /> <br />

		<br /> <br /><br /> <br />
		<br /> <br /><br /> <br />
		<br /> <br />
		<h1></h1>
		<h1></h1>
		<p></p>
		<p></p>
		<div id="c" style="width:800px; margin:0 auto;">
		<h3>  <span>  ¿NUESTROS EVENTOS?  </span>  </h3>
		<br /> <br />
        </div>
        <center><p class="description">Tu asistencia es importante para nosotros visitanos en los eventos qu estamos realizando</p></center>
        <br /> <br /> <br />

        
        <div id="Third_menu" style="width:700px; margin:0 auto;">
			<ul><center>
				<li>
					<div class="c">
						<span><img src="\Deshpande_LEANEVENTO\imagenes\minibaner4.jpg" /></span>
						<div class="makeleft">
							<?php echo $name_array[0]; ?><br>
							<?php echo $price_array[0]; ?>
						</div>
					</div>
				</li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li>
					<div class="c">
						<span><img src="\Deshpande_LEANEVENTO\imagenes\minibaner1.jpg" /></span>
						<div class="makeleft">
							<?php echo $name_array[1]; ?><br>
							<!--<label>LA IMPORTICA DE LOS ALIMENTOS</label>-->
							<?php echo $price_array[1]; ?>
						</div>					
					</div>
				</li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li>
					<div class="c">
						<span><img src="\Deshpande_LEANEVENTO\imagenes\minibaner2.jpg" /></span>
						<div class="makeleft">
							<?php echo $name_array[2]; ?><br>
							<?php echo $price_array[2]; ?>

							<!--<label>EDUCANDO PARA EL FUTURO</label>
							<label>Entrada Gratis</label>-->
						</div>
					</div>
				</li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>	
				<br /><br>
				<!--
				<a class="before">    &#8249;</a>
				<a class="after">    &#8250;</a>-->
			</ul></center>
		</div><br />
        <!--<img src="C:\Users\Anirudh Deshpande\Desktop\Deshpande_LEANEVENTO\more_imagenes.png" />-->
        <div style="width:1200px; margin:0 auto;"><p id="mypara"><span></span></p></div>
        <div class="social">
        <div id="fheading"><h4 font-weight:bold"><span>LEAN EN LAS REDES SOCIALES</span></h4></div>
        <div class="icons">
      <a href="#"> <i class="fa fa-twitter" style="font-size:24px;color:#FFC300"></i> </a>
 <a href="#"> <i class="fa fa-facebook"  style="font-size:24px;color:#FFC300"></i></a> 
 <a href="#"> <i class="fa fa-instagram"style="font-size:24px;color:#FFC300"></i></a></div>

		
	
		
	</section>

	<footer id="main_footer">
		<nav id="Second_menu" style="width:1200px; margin:0 auto;">
			<ul>
				<li>
					<div class="a">
						<span><center>Registrese para recibir un boletien</center>
						</span>
					</div>
				</li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li>
					<div class="one">
						<span><input type="text" name="Subscribe" value="Subscribe"/></span>					
					</div>
				</li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li>
					<div class="two">
						<span><button>Subscribir</button></span>
					</div>
				</li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
				<li></li>
			</ul>
		</nav><br />
	<footer id="main_footer">
		Copyright ©2019 All rights reserved| This web is made with ♡ by DiazApps 
	</footer>	
	</div>

</body>
</html>