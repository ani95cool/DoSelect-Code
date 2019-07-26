<!DOCTYPE html>
<html>
<style type="text/css">


h1 {
  text-align: center;
  font-family: Tahoma, Arial, sans-serif;
  color: #06D85F;
  margin: 80px 0;
}

.box {
  width: 40%;
  margin: 0 auto;
  background: rgba(255,255,255,0.2);
  padding: 35px;
  border: 2px solid #fff;
  border-radius: 20px/50px;
  background-clip: padding-box;
  text-align: center;
}

.button {
  font-size: 1em;
  padding: 10px;
  color: #fff;
  border-radius: 3rem;
  text-decoration: none;
  cursor: pointer;
  background-color:yellow;
  transition: all 0.3s ease-out;
}


.overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  transition: opacity 500ms;
  visibility: hidden;
  opacity: 0;
}
.overlay:target {
  visibility: visible;
  opacity: 1;
}

.popup {
  margin: 70px auto;
  padding: 20px;
  display: inline-block;
  background: #E5E7E9;
  border-radius: 5px;
  width: 500px;
  height:550px;
  position: relative;
  left: 500px;

}

input, label {
	display: block;
}

.popup h2 {
  margin-top: 0;
  color: #333;
  font-family: Tahoma, Arial, sans-serif;
}
.popup .close {
  position: absolute;
  top: 20px;
  right: 30px;
  transition: all 200ms;
  font-size: 30px;
  font-weight: bold;
  text-decoration: none;
  color: #333;
}
.popup .close:hover {
  color: #06D85F;
}
.popup .content {
  max-height: 30%;
  overflow: auto;
  float:left;
}

input {
  margin-bottom: 15px;
}

.content  + .content{
  margin: 0 0 0 8px;
}

.xyz {
 position:relative;
  top:60px;
  right: 330px;
  height:30px;
}

.mn {
  position:relative;
  top:30px;
  right: 160px;
  height:30px;
}

.h {
	position: relative;
	top: 1px;
	float: left;

}

.ip {
	position: relative;
	top: 150px;
}

.h  + .h{
  margin: 0 0 0 8px;
}

.ip  + .ip{
  margin: 0 0 0 8px;
}

.di {
	position: relative;
	right: 330px;
}

.dip {
	position: relative;
	display: inline-block;
	top: 150px;
	right: 160px;
}

.myone {
  position: relative;
  display: inline-block;
  top: 150px;
  left: 3px;

}

#bu1 {
	top: 200px;
	left: 2000px;
}
button {
	border-color: yellow;
}
</style>
	<head>
		<title></title>
	</head>
<body>
	


<form id="popup1" method="POST" action="Business_register.php">
	<div class="popup">
		<h2>Registrar Organization</h2>
		<div class="content">
      <label>Correo</label><br>
      <input type="text" name="user" placeholder="Correo" required/>
      
		</div>
    <div class="content">
      <label http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">Contraseña</label><br>
      <input type="text" name="contrasena" placeholder="Contraseña" required/>
      
		</div>
    <div class="xyz">
      
      <label>Nombre</label><br>
      <input type="text" name="nombre" placeholder="Nombre" required/>      
    
      
		</div>
    
    <div class="mn">
      
      <label>Apellido</label><br>
      <input type="text" name="apellido" placeholder="Apellido" required/>
    
    </div>

    <div class="ip">
    	<label class="di">Ciudad</label><br>
    <input type="text" name="ciudad" placeholder="Ciudad" required/>
    </div>

    <div class="h">
    	<label>Direccion</label><br>
    <input type="text" name="direccion" placeholder="Direccion" required/>
    </div>	

    <div class="dip">
      <label http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">Estado</label><br>
      <input type="text" name="estado" placeholder="Estado" required/>
      
		</div>

		<div class="dip">
      <label http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">Codigo</label><br>
      <input type="text" name="codigo" placeholder="Codigo" required/>
      
		</div>
    <div class="myone">
      <input type="radio" name="type" value="1" required>Tipo de negocio 1
    </div>

    <div class="myone">
      <input type="radio" name="type" value="2" required>Tipo de negocio 2
    </div>

    <div class="myone">
      <input type="radio" name="type" value="3" required>Tipo de negocio 3
    </div>

    <br><br><br><br><br><br><br><br><br><br><br>
		<div>
			<button id="bu1" class="form__submit button button_theme_dark">Registrarse</button>
		</div>

    


    

	
		
	</div>

	
    
</form>
</body>	
</html>