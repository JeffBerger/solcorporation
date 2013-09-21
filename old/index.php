<?php


$URL_STRING = trim(stripslashes($_REQUEST['URL_STRING']));
$URL_STRING = trim($URL_STRING, '/');
$URL_PATH = split("/", $URL_STRING);

$filepath = "/home2/westphal/public_html/solcorporation/pages/". $URL_STRING . ".php";

if(isset($URL_PATH[0]))
	if($URL_PATH[0] == "ReZound")
		$filepath = "/home2/westphal/public_html/solcorporation/". $URL_STRING . ".php";
	
	
if($URL_STRING == "")
	include '/home2/westphal/public_html/solcorporation/pages/home.php';
else if(file_exists($filepath))
	include $filepath;
else
	include '/home2/westphal/public_html/solcorporation/pages/error.php';
	
?>