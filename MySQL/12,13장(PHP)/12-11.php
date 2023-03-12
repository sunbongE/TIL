<?php
   $hap=0;
   
   $i=123;
   while( $i<=456 ) {
	  $hap = $hap + $i;
	   $i=$i+2;
   }
   
   echo "123부터 456까지 홀수의 합계 : ", $hap;
 ?>