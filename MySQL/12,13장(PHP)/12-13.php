<?php
  $hap = 0;
  $myArray = range(1,10);
 
  for($i=0; $i<10; $i++) {
     $hap = $hap + $myArray[$i];
  }
   echo "배열의 합계 : " , $hap;  
?>
