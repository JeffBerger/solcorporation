<?php 

$quote = "Freedom lies in being bold.";
$quoteattrib = "-Robert Frost";

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
			<h2>Space is for everyone</h2>
				<p>We want to go into space, and we want you to come with us.  The cost of orbital launch is extremely
					prohibitive currently and there is no sign that we will see a dramatic decrease in the cost.  Privatization
					of space travel has done much to reduce the cost of orbital launches, however with prices still in the 
					thousands of dollars per kilogram the cost to put something into space becomes extreme quickly.</p>
			<h2>Orbital vs Suborbital</h2>
				<p>When we talk about space launches we are talking about orbital launches, not suborbital.  You can't just 
					go straight up 100 miles because you won't stay there, you'll fall right back down.  That is a sub-orbital
					launch, where the craft reaches an altitude which is high enough to be in space but it does not have the 
					velocity to keep itself in space, thus it falls back after a small ammount of time.  Sattilites and the ISS
					 are all examples of orbital launches, where these objects orbit the earth and do not fall back down.  The 
					 fact that they stay up allows them to do much more meaningful work in space.  Who wants to spend all that 
					 energy to get into space just to come back after 10 minutes?</p>
			<h2>Rockets are so 1950s</h2>
				<p>The reason that the price is so outrageous is because rockets are an inheretly limited techonology.  
					The limitation is on the rocket fuel itself, there is only so much energy you can chemically store 
					in fuel.  Advances in composites, in turbopumps and computers can only help so much before you are faced 
					with the raw fact that rocket fuel has not changed drastically since the days of Apollo.  Most of the 
					energy of the craft is into transporting its fuel and only a small percent is payload, with some or 
					all of the vessel being discarded after launch.  How expensive would it be to visit your relatives if 
					after you drove to the next town you had to throw away your car?</p>
			<h2>A launch without rockets</h2>
				<p>The solution is to move away from the rocket model entirely.  We have the technology to now dispense with 
					carrying all of our energy with us, we can impart the energy in the vessel on the ground and then it needs 
					carry only what is required to manuver in space and accomplish the mission.  This is accomplished through 
					an electromagnetic launcher.  The launcher accelerates our craft to 25 times the speed of sound and throws 
					the payload into space.</p>
			<h2>That sounds crazy</h2>
				<p>Doesn't sitting ontop of a 300 foot tall pile of explosives and throwing out the entire tower sound crazy 
					too?  But it worked, so people believe in it.  This sounds crazy but there is no reason it can't work.</p>
			<h2>I have lots of reasons it can't work</h2>
				<p>We've come up with many solutions to these problems, and as we continue working we will solve more of them. 
					 Currently we believe there is no fundamental reason that precludes using an electromagnetic launcher for 
					 space travel.</p>
			<h2>So you want to build a gun to shoot us to space?</h2>
				<p>We prefer not to call it a gun, but yes.  Plenty of people have had this idea, but we have our own variant 
					on this and we're not content to write papers about it.  We're going to go out there and start building this!</p>
			<h2>What is the benefit of decreasing the cost of space launch?</h2>
				<p>This cannot be wholly predicted, because once the entry into space becomes cheap we can not only move to putting 
					energy collection as well as manufacturing into orbit, entire new ideas and industries will appear that we could 
					not predict before.  This could open an entire new era of humanity.</p>
			<h2>How much cheaper are we talking?</h2>
				<p>Our prelimianry calculations show it somewhere between 1/20 and 1/50 the cost of conventional rocket transport.</p>
			<h2>Interested?</h2>
				<p>Feel free to <a href="http://www.solcorporation.com/contact">get in touch</a> with us and talk more about the entire system.  We're gonna start building this ourselves, 
					might as well help out.</p>	
		</div>
		
		<div id="imageright">
			<img src="http://www.solcorporation.com/img/sidebar5.jpg" id="rightimg">
		</div>
		
	</div>
		
HTML;

echo $content;

echo $soltail;

?>