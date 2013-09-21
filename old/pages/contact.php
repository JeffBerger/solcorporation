<?php 

$quote = "Any sufficiently advanced technology is indistinguishable from magic.";
$quoteattrib = "-Arthur C. Clarke";

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
			<p>The best way to contact us is by email, so you may email either $jeffmail $rossmail or $joshmail, but you should probably just stick to $jeffmail </p>	
		</div>
		
		<div id="imageright">
			<img src="http://www.solcorporation.com/img/sidebar5.jpg" id="rightimg">
		</div>
		
	</div>
		
HTML;

echo $content;

echo $soltail;

?>