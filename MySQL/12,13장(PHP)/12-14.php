<?php
  $myArray = range(1,10);
  
  echo "임의로 섞은 값 ==> ";
  shuffle($myArray);
  foreach($myArray as $data)
	echo $data, " ";
	
  echo "<br>오름차순 정렬 ==> ";	
  sort($myArray);
  foreach($myArray as $data)
	echo $data, " ";

  echo "<br>내림차순 정렬 ==> ";	
  rsort($myArray);
  foreach($myArray as $data)
	echo $data, " ";
  
  echo "<br>순서를 반대로 ==> ";	
  $revArray = array_reverse($myArray);
  foreach($revArray as $data)
	echo $data, " ";	
 ?>