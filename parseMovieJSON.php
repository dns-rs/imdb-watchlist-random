<?php
/*
Error reporting helps you understand what's wrong with your code, remove in production.
*/
error_reporting(E_ALL); 
ini_set('display_errors', 1);

$read = exec("python test.py user@domain.tld 123456");

echo($read);

// if($read == "OK")
//    {
//       echo "ok, registered";
//    }
// else if($read == "KO")
//    {
//       echo "failed";
//    }
?>