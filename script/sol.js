
var _DEBUG = true;

function _alert(msg)
{
	if(_DEBUG)alert(msg);
}

$(document).ready(function() {
	// Handler for .ready() called.
	//_alert("Template ready");

	$("#header-News").click(function() {
	  $("#newsBox").animate({height:'150px'}, 300);
	});
});


$(document).scroll(function() {
	var Top = $(window).scrollTop();
	if(Top > 550)
	{
		$('#header-Navigation').css('position', 'fixed');
		$('#header-Navigation').css('top', '0px');
		//$('#header-Navigation').css('left', '0px');
		$('#header-Navigation').css('right', '0px');
		$('#header-Navigation').addClass('floatingNav');
		//$('#YourTotal').css('opacity', '1');
		//$('#header-Logo').css('margin-top', '55px');
	}
	else
	{
		$('#header-Navigation').css('position', 'absolute');
		$('#header-Navigation').css('top', '550px');
		//$('#header-Navigation').css('left', '10%');
		$('#header-Navigation').css('right', '15%');
		$('#header-Navigation').removeClass('floatingNav');
		//$('#YourTotal').css('opacity', '0');
		//$('#header-Logo').css('margin-top', '30px');
	}
});
