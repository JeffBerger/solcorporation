<?php 

$quote = " Taking a new step...is what people fear most.";
$quoteattrib = "-Dostoyevski";

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
			<p>Currently we are not actively seeking investors.  We are drawing up a comprehensive multi-phased proposal
				for Sol-Corp and we are making sure the science in the proposal is the best it can be.  We want you to 
				know that we aren't just dreaming this, we are putting our own time and money into this right now.  We 
				believe in this and want to make a believer out of you.</p>
			<p>If you would like to make a donation then please
				use the button on this page.  If you have passion and would like to partner with us in our dream to make 
				orbital travel available to millions rather than dozens then please send $jeffmail an email and we'd be 
				more than happy to discuss potential arrangements.</p>	
		</div>
		
		<div id="imageright">
			<img src="http://www.solcorporation.com/img/sidebar5.jpg" id="rightimg">
		</div>
		
	</div>
		
HTML;

echo $content;

echo $soltail;

?>