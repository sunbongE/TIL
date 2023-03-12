<?php
   $con=mysqli_connect("localhost", "root", "1234", "sqlDB") or die("MySQL 접속 실패 !!");

   $userID = $_POST["userID"];
   $name = $_POST["name"];
   $birthYear = $_POST["birthYear"];
   $addr = $_POST["addr"];
   $mobile1 = $_POST["mobile1"];
   $mobile2 = $_POST["mobile2"];
   $height = $_POST["height"];   
   $mDate = $_POST["mDate"]; 
   
   $sql ="UPDATE userTbl SET name='".$name."', birthYear=".$birthYear;
   $sql = $sql.", addr='".$addr."', mobile1='".$mobile1."',mobile2='".$mobile2;
   $sql = $sql."', height=".$height.", mDate='".$mDate."' WHERE userID='".$userID."'";
   
   $ret = mysqli_query($con, $sql);
 
    echo "<h1> 회원 정보 수정 결과 </h1>";
   if($ret) {
	   echo "데이터가 성공적으로 수정됨.";
   }
   else {
	   echo "데이터 수정 실패!!!"."<br>";
	   echo "실패 원인 :".mysqli_error($con);
   } 
   mysqli_close($con);
   
   echo "<br> <a href='main.html'> <--초기 화면</a> ";
?>
