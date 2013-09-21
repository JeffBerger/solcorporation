<?php

$solheader =<<<HTML

<!DOCTYPE html>
<html>

	<head>
	
		<title>The Sol Corporation</title>
		<link rel="stylesheet" type="text/css" href="http://www.solcorporation.com/solcorp.css">
		<link rel="icon" type="image/png" href="http://www.solcorporation.com/img/solfavicon.png">

	<script>
		
	var imgarray = ['http://www.solcorporation.com/img/sidebar1.jpg', 'http://www.solcorporation.com/img/sidebar2.jpg', 'http://www.solcorporation.com/img/sidebar4.jpg','http://www.solcorporation.com/img/sidebar5.jpg'];    
	var leftcount =0;
	var rightcount = imgarray.length/2;
		
		
	function changeimage()
	{

		if(leftcount%2 == 0 && rightcount%2 ==0){
			document.getElementById('leftimg').setAttribute('src', imgarray[leftcount]);
			leftcount++;
		}
		else if(leftcount%2 == 1 && rightcount%2 ==0){
			document.getElementById('rightimg').setAttribute('src', imgarray[rightcount]);
			rightcount++;
		}
		else if(leftcount%2 == 1 && rightcount%2 ==1){
			document.getElementById('leftimg').setAttribute('src', imgarray[leftcount]);
			leftcount++;
		}
		else if(leftcount%2 == 0 && rightcount%2 ==1){
			document.getElementById('rightimg').setAttribute('src', imgarray[rightcount]);
			rightcount++;
		}		
		
		if(leftcount == imgarray.length){
			leftcount = 0;
		}
		
		if(rightcount == imgarray.length){
			rightcount = 0;
		}
	}
	
	setInterval(changeimage,5000);
		
</script>
	</head>
	
HTML;

$jeffmail = '<a href="mailto:jeff@solcorporation.com">Jeff</a>';
$rossmail = '<a href="mailto:ross@solcorporation.com">Ross</a>';
$joshmail = '<a href="mailto:josh@solcorporation.com">Josh</a>';

$solpagetop =<<<HTML


	<body>
	<header>
	
		<div id="bannerdiv">
			<div id="banner">
				<a  href="http://www.solcorporation.com"><img src="http://www.solcorporation.com/img/SolTestBanner.png" alt="Sol Corporation : The Sky Is No Longer The Limit"></a>
			</div>
		</div>
		
		<ul class="navigation">
			<li class="navigation"><a class="navigation" href="news">News</a></li>
			<li class="navigation"><a class="navigation" href="mission">Mission</a></li>
			<li class="navigation"><a class="navigation" href="people">People</a></li>
			<li class="navigation"><a class="navigation" href="investors">Investors</a></li>
			<li class="navigation"><a class="navigation" href="http://www.cafepress.com/SolCorp" target="_blank">Store</a></li>
			<li class="navigation"><a class="navigation" href="contact">Contact</a></li>
		</ul>
				
	</header>
	
	<hr id="postheader">
		
HTML;

$solpagequote = <<<HTML
		
		<div id="quote">
		
			<p id="quoteline">$quote</p>
			<p id="quoteattribution">$quoteattrib</p>
		
		</div>
				
		
HTML;

$solcontentstart = <<<HTML

	<div id="content">	

		<div id="contentarea">
		
HTML;



$soltail =<<<HTML

		</div>
	</div>
	
	<footer>
	<div id="footercontent">
  		<p>A Dr.Berger workin progress</p>
  	</div>
</footer>

</body>
</html>

HTML;

?>