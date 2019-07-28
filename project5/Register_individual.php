<?php 
session_start();

?>

<?php
defined('BASEPATH') OR exit('No direct script access allowed!!');

class Register_individual extends CI_Controller {

  public function myrun(){
    $this->load->view('Individual');
  }

  public function validate_fields(){
    $this->load->library('form_validation');
    $this->form_validation->set_rules('nombre', 'Nombre', 'required|regex_match[/^(?!.__.)(?!.\.\..)[a-zA-Z_.]+$/]');
    $this->form_validation->set_rules('correo', 'Correo', 'regex_match[/^[0-9]*[a-z]{1,23}+[0-9|_-]*[!@#$_]+[a-zA-Z]+[.|a-zA-Z]+$/]');
    $this->form_validation->set_rules('contrasena', 'Contraseña', 'regex_match[/^[!@#&_]+\w{1,5}[a-zA-Z]+[0-9]+[!@$#_]+$/]');
    $this->form_validation->set_rules('apellido', 'Apellido', 'regex_match[/^(?!.__.)(?!.\.\..)[a-zA-Z_.]+$/]');
    $this->form_validation->set_rules('direccion', 'Direccion', 'regex_match[/^[0-9]*[\s+|,|a-zA-Z]+[0-9]*[a-zA-Z]{1,23}+[0-9|a-zA-z|\s+|,]+$/]');
    $this->form_validation->set_rules('ciudad', 'Ciudad', 'regex_match[/^[a-zA-Z|-]+$/]');
    $this->form_validation->set_rules('estado', 'Estado', 'regex_match[/^[a-zA-Z|-]+$/]');
    $this->form_validation->set_rules('codigo', 'Codigo', 'regex_match[/^[0-9|-]+$/]');

    if($this->form_validation->run() == FALSE){
      echo "Not possible";
    }else{
      $db1 = $this->load->db('leaneventos');
      $this->load->view('welcome_message');

    }




  }

  


}




?>