<?php 
session_start();
$sess = $_SESSION["email_id"];
if(!isset($_SESSION["email_id"])){
	echo "<script>
	alert('You are not yet logged in');
	window.location.href='Individual.html';

	</script>";
}else{
	

	


}
?>



<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>LEANEVENTO website</title>
	<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="sayitright.css">
	<style type="text/css">
		li img {font: bold 14px;}
		li img {width: 30px; height: 30px;}
		section img {width: 1200px; height: 320px;}
		#moveme {left: 250px;}
		#top_menu ul{
			transform: translate(85%);

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
			<li style="font: bold 10px Roboto;"><img src="C:\Users\Anirudh Deshpande\Desktop\Deshpande_LEANEVENTO\imagenes\logo-blanco.png" />LEANEVENTOS</li>
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
			<li class="new">Comparar Boletos</li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
		</ul>
	</nav>

	<section id="main_section">
		<br />
		<!--<img src="C:\Users\Anirudh Deshpande\Desktop\Deshpande_LEANEVENTO\imagenes\mine.png" /><br /><br />-->
		<span></span>
		<span></span>
		<span></span>
		<h2 id="io" style="position: absolute; left: 500px; top: 50px;">Lista de Eventos</h2>	<br /> <br />
		<br /> <br />
		<center><table class="table table-borderles" style="position: relative; left: 120px;top: 40px;">
  <thead style="background-color: #F2F3F4; padding: 20px;">
    <tr>
      <th></th>
      <th width="60%"><center>DETALLES DEL EVENTOS</center></th>
      <th width="40%"><center>LUGAR</center></th>
      <th width="40%">FECHA</th>
      <th width="40%">HORA</th>
      <th></th>
      <th width="40%">ASISTENCIA</th>
    </tr>
  </thead>
  <tbody>
    <tr class="mytr">
    <div class="mytd">	
      <td class="prop"><img src="C:\Users\Anirudh Deshpande\Desktop\Deshpande_LEANEVENTO\more_imagenes\minibaner1.jpg"/></td>
      <td width="60%">Nombre del Evento y sus detailes</td>
      <td width="40%">Direccion del lugar</td>
      <td width="40%">14/01/2019</td>
      <td width="40%">8 AM</td>
      <td></td>
      <td width="40%"><button class="button">Confirmar</button></td>
    </div>  
    </tr>
    <tr class="mytr">
    <div class="mytd">	

      <td class="prop"><img src="C:\Users\Anirudh Deshpande\Desktop\Deshpande_LEANEVENTO\more_imagenes\minibaner2.jpg"/></td>
      <td width="60%">Nombre del Evento y sus detailes</td>
      <td width="40%">Direccion del lugar</td>
      <td width="40%">14/01/2019</td>
      <td width="40%">8 AM</td>
      <td></td>
      <td width="40%"><button class="button">Confirmar</button></td>
    </div>  
    </tr>
    <tr class="mytr">
    <div class="mytd">
    <center>	
      <td class="prop"><img src="C:\Users\Anirudh Deshpande\Desktop\Deshpande_LEANEVENTO\more_imagenes\minibaner3.jpg"/></td>
      <td width="60%">Nombre del Evento y sus detailes</td>
      <td width="40%">Direccion del lugar</td>
      <td width="40%">14/01/2019</td>
      <td width="40%">8 AM</td>
      <td></td>
      <td width="40%"><button class="button">Confirmar</button></td></center>
    </div>  
    </tr>
    <tr>
    <div class="mytd">	
    	<td></td>
    	<td></td>
    	<td></td>
    	<td></td>
    	<td></td>
    	<td></td>
    </div>
    </tr>
  </tbody>
</table></center>

		<br /> <br /><br /> <br />
		<br /> <br /><br /> <br />
		<br /> <br />
		<h1></h1>
		<h1></h1>
		<p></p>
		<p></p>
		
	<div style="right: 2500px;">
	<span id="moveme">Copyright ©2019 All rights reserved| This web is made with ♡ by DiazApps</span>
	</div>
	</section><br><br><br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>
	<br><br>

	
	</div>

</body>
</html>