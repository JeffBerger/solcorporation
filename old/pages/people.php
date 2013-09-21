<?php 

$quote = "The man with a new idea is a crank, until the idea succeeds.";
$quoteattrib = "-Mark Twain";

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
		
			<div class="aboutpic">
					<img src="http://www.solcorporation.com/img/jeffpic.jpg">
					<p>Dr. Jeffrey Berger recieved his Ph.D. in Theoretical Nuclear and Particle physics from 
					Penn State in 2012.  He currently works as a programmer and data scientist at We-Care.com.
					He is an accomplished bladesmith and has several technology and scientific startup companies
					currently in the works.  When Sol Corp succeeds it is pretty much because of him.  Jeff 
					can be reached by email at <a href="mailto:jeff@solcorporation.com">jeff@solcorporation.com</a></p>
					<hr>
			</div>
			
			<div class="aboutpic">
					<img src="http://www.solcorporation.com/img/joshpic.jpg">
					<p>Dr. Joshua Wickman earned his Ph.D. in theoretical cosmology and particle physics from 
					the University of Delaware in 2012.  He is currently an Assistant Professor teaching physics 
					at Gloucester County College.  He plays guitar (poorly) and brews his own beer (less poorly).  
					Josh can be reached by email at <a href="mailto:josh@solcorporation.com">josh@solcorporation.com</a></p>
					<hr>
			</div>
			
			<div class="aboutpic">
					<img src="http://www.solcorporation.com/img/rosspic.jpg">
					<p>Wannabe Dr. Ross Martin-Wells is still trying to get a Ph.D. in atomic molecular and optical physics
					from Penn State.  One day we hope he'll do it, until then he is catching up on a lot of science fiction
					reading as well as setting new speed records for how quickly he can grade student's papers.  Ross 
					can be reached by email at <a href="mailto:ross@solcorporation.com">ross@solcorporation.com</a></p>
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