<?php 

$quote = "All science is either physics or stamp collecting.";
$quoteattrib = "-Ernest Rutherford";

include 'solpageelements.php';
echo $solheader;
echo $solpagetop;

echo $solpagequote;

$content =<<<HTML
		
	<div id="content">	

		<div id="imageleft">
			<img src="http://www.solcorporation.com/img/sidebar2.jpg" id="leftimg">
		</div>
	
		<div id="contentarea">
			<p>I'm sorry but the page you are looking for does not exist.  If you think it should and there is a problem
				on the page please notify $jeffmail</p>	
		</div>
		
		<div id="imageright">
			<img src="http://www.solcorporation.com/img/sidebar5.jpg" id="rightimg">
		</div>
		
	</div>
		
HTML;

echo $content;

echo $soltail;

?>