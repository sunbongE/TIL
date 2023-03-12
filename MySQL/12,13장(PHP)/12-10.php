<?php
   $hap=0;
   
   for( $i=123; $i<=456 ; $i=$i+2 ) {
	  $hap = $hap + $i;
   }
   
   echo "123부터 456까지 홀수의 합계 : ", $hap;
 ?>