$(document).ready(function(){
	
	if($.uniform)
	   $('input:checkbox, input:radio, .uniform-file').uniform();

	
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