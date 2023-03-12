<?php
   $jumsu=83;
   
   switch(intval($jumsu / 10)) {
		case 10:
		case 9:
			echo "A학점"; break;
		case 8:
			echo "B학점"; break;
		case 7:
			echo "C학점"; break;
		case 6:
			echo "D학점"; break;			
	    default:
			echo "F학점";
   }
 ?>