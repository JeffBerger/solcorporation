<?php 

$quote = "We are all agreed that your theory is crazy. The question that divides us is whether it is crazy enough to have a chance of being correct.";
$quoteattrib = "-Neils Bohr to Wolfgang Pauli";

include 'solpageelements.php';
echo $solheader;
echo $solpagetop;

echo $solpagequote;

$newsfiles = array();

if ($handle = opendir('/home2/westphal/public_html/solcorporation/pages/news')) {

	while (false !== ($entry = readdir($handle))) {
		if($entry != "." && $entry != "..")
			$newsfiles[] = $entry;
	}

	closedir($handle);
}

rsort($newsfiles);

$newssection="";

if(isset($newsfiles[0])){
		$filename = '/home2/westphal/public_html/solcorporation/pages/news/'.$newsfiles[0];
		$newssection .= file_get_contents($filename);
}

$content =<<<HTML
		
	<div id="content">	

		<div id="imageleft">
			<img src="http://www.solcorporation.com/img/sidebar2.jpg" id="leftimg">
		</div>
	
		<div id="contentarea">
			<p>Dedicated to a new era of humanity amongst the stars.  This time, with 97% less rocket fuel!</p>	
			<div id="newscontent">
				<hr>
				$newssection
			</div>
		</div>
		
		<div id="imageright">
			<img src="http://www.solcorporation.com/img/sidebar5.jpg" id="rightimg">
		</div>
		
	</div>
		
HTML;

echo $content;

echo $soltail;

?>