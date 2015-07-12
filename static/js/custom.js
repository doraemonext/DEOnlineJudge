$(document).ready(function(){
	
	// dropdown in leftmenu
	$('.leftmenu .dropdown > a').click(function(){
		if(!$(this).next().is(':visible'))
			$(this).next().slideDown('fast');
		else
			$(this).next().slideUp('fast');	
		return false;
	});
	
	
	if($.uniform) 
	   $('input:checkbox, input:radio, .uniform-file').uniform();
		
	if($('.widgettitle .close').length > 0) {
		  $('.widgettitle .close').click(function(){
					 $(this).parents('.widgetbox').fadeOut(function(){
								$(this).remove();
					 });
		  });
	}
	
	
	//// show/hide left menu
	//$(window).resize(function () {
	//	if ($('.topbar').is(':visible')) {
	//		if ($('.barmenu').hasClass('open')) {
	//			$('.rightpanel, .headerinner').css({marginLeft: '260px'});
	//			$('.logo, .leftpanel').css({marginLeft: 0});
	//		} else {
	//			$('.rightpanel, .headerinner').css({marginLeft: 0});
	//			$('.logo, .leftpanel').css({marginLeft: '-260px'});
	//		}
	//	} else {
	//		$('.rightpanel, .headerinner').css({marginLeft: '260px'});
	//		$('.logo, .leftpanel').css({marginLeft: 0});
	//	}
	//});
	
	// dropdown menu for profile image
	$('.userloggedinfo img').click(function(){
		  if($(window).width() < 480) {
					 var dm = $('.userloggedinfo .userinfo');
					 if(dm.is(':visible')) {
								dm.hide();
					 } else {
								dm.show();
					 }
		  }
   });
	
	// change skin color
	$('.skin-color a').click(function(){ return false; });
	$('.skin-color a').hover(function(){
		var s = $(this).attr('href');
		if($('#skinstyle').length > 0) {
			if(s!='default') {
				$('#skinstyle').attr('href','css/style.'+s+'.css');	
				$.cookie('skin-color', s, { path: '/' });
			} else {
				$('#skinstyle').remove();
				$.cookie("skin-color", '', { path: '/' });
			}
		} else {
			if(s!='default') {
				$('head').append('<link id="skinstyle" rel="stylesheet" href="css/style.'+s+'.css" type="text/css" />');
				$.cookie("skin-color", s, { path: '/' });
			}
		}
		return false;
	});
	
	// load selected skin color from cookie
	if($.cookie('skin-color')) {
		var c = $.cookie('skin-color');
		if(c) {
			$('head').append('<link id="skinstyle" rel="stylesheet" href="css/style.'+c+'.css" type="text/css" />');
			$.cookie("skin-color", c, { path: '/' });
		}
	}
	
	
	// expand/collapse boxes
	if($('.minimize').length > 0) {
		  
		  $('.minimize').click(function(){
					 if(!$(this).hasClass('collapsed')) {
								$(this).addClass('collapsed');
								$(this).html("&#43;");
								$(this).parents('.widgetbox')
										      .css({marginBottom: '20px'})
												.find('.widgetcontent')
												.hide();
					 } else {
								$(this).removeClass('collapsed');
								$(this).html("&#8211;");
								$(this).parents('.widgetbox')
										      .css({marginBottom: '0'})
												.find('.widgetcontent')
												.show();
					 }
					 return false;
		  });
			  
	}
	
	// fixed right panel
	var winSize = $(window).height();
	if($('.rightpanel').height() < winSize) {
		$('.rightpanel').height(winSize);
	}
	
	
	// if facebook like chat is enabled
	if($.cookie('enable-chat')) {
		
		$('body').addClass('chatenabled');
		$.get('ajax/chat.html',function(data){
			$('body').append(data);
		});
		
	} else {
		
		if($('.chatmenu').length > 0) {
			$('.chatmenu').remove();
		}
		
	}

    // 设置CSRF
	$.getCookie = function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

	$.csrfSafeMethod = function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    };

	$.csrftoken = $.getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
			if (!$.csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", $.csrftoken);
			}
        }
    });
	$.makeCsrf = function (xhr, settings) {
		if (!$.csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", $.csrftoken);
		}
	};

	$.makeDangerAlert = function (content) {
		$.alerts.dialogClass = 'alert-danger';
		jAlert(content, '错误提示', function(){
			$.alerts.dialogClass = null;
		});
	};
});