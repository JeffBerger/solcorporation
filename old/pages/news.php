<?php 

$quote = "The choice is: the Universe…or nothing.";
$quoteattrib = "-H.G. Wells";

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

$newssection = "";
$newsentrynumber = count($newsfiles);

if($newsentrynumber > 10)
	$newsentrynumber = 10;
$newscount = 0;

foreach ($newsfiles as $newsentry) {
		$newscount++;
		$filename = '/home2/westphal/public_html/solcorporation/pages/news/'.$newsentry;
		$newssection .= file_get_contents($filename);
		if($newscount != $newsentrynumber)
			$newssection .= '<hr>';
		else
			break;
}


$content =<<<HTML
		
	<div id="content">	

		<div id="imageleft">
			<img src="http://www.solcorporation.com/img/sidebar2.jpg" id="leftimg">
		</div>
	
		<div id="contentarea">
			<div id="newscontent">
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