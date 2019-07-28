<?php 

defined('BASEPATH') OR exit('No direct script access allowed!!');

class Contact_Us extends CI_Controller {

	public function index(){
		$this->load->view('contacto');
	}

	public function validate(){
		$this->load->library('form_validation');
		$this->form_validation->set_rules('firstname', 'Nombre', 'required|regex_match[/^(?!.__.)(?!.\.\..)[a-zA-Z_.]+$/]');
	    $this->form_validation->set_rules('email', 'Correo', 'regex_match[/^[0-9]*[a-z]{1,23}+[0-9|_-]*[!@#$_]+[a-zA-Z]+[.|a-zA-Z]+$/]');
	    //$this->form_validation->set_rules('contrasena', 'Contraseña', 'regex_match[/^[!@#&_]+\w{1,5}[a-zA-Z]+[0-9]+[!@$#_]+$/]');
	    $this->form_validation->set_rules('lastname', 'Apellido', 'regex_match[/^(?!.__.)(?!.\.\..)[a-zA-Z_.]+$/]');
	    //$this->form_validation->set_rules('direccion', 'Direccion', 'regex_match[/^[0-9]*[\s+|,|a-zA-Z]+[0-9]*[a-zA-Z]{1,23}+[0-9|a-zA-z|\s+|,]+$/]');
	    $this->form_validation->set_rules('topic', 'Tema', 'regex_match[/^[a-zA-Z|-]+$/]');
	    $this->form_validation->set_rules('description', 'Mensaje', 'required');
	    //$this->form_validation->set_rules('codigo', 'Codigo', 'regex_match[/^[0-9|-]+$/]');

	    if($this->form_validation->run() == FALSE){
	      echo "Not possible";
	    }else{
	      $db = $this->load->database();
	      $firstname = $this->input->post('firstname');
	      $email = $this->input->post('email');
	      $surname = $this->input->post('lastname');
	      $topic = $this->input->post('topic');
	      $message = $this->input->post('description');
	      $query = "INSERT INTO `contactinfo` (`firstname`, `surname`, `email`, `topic`, `message`) VALUES ('$firstname','$surname','$email','$topic','$message');";
	      $result = $this->db->query($query);
	      if($result == TRUE){
	      	echo "The record has been inserted";
	      }else{
	      	echo "There is an error";
	      }
	      $this->load->view('welcome_message');

	    }
	}


}


?>