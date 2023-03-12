<?php
  $myArray = array(100, 'MySQL', 123.123);
  echo $myArray[0], " ", $myArray[1], " ", $myArray[2], "<br>";
  
  $myArray = range(1,3);
  echo $myArray[0], " ", $myArray[1], " ", $myArray[2], "<br>";
  
  $myArray = range(1,10,2);
  echo $myArray[0], " ", $myArray[4], "<br>";
  
  $newArray[0] = 'This';
  $newArray[1] = 'is';
  $newArray[2] = 'MySQL';
  echo $newArray[0], " ", $newArray[1], " ", $newArray[2], "<br>";  
 ?>