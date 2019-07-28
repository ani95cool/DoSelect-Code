<?php 
session_start();

?>

<?php
defined('BASEPATH') OR exit('No direct script access allowed!!');

class Register extends CI_Controller {

  public function myrun(){
    $this->load->view('Individual');
  }


}




?>