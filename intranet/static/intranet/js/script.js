$(document).ready(function(){
	$(".hide-comments").hide();
	$(".comments-box").hide();
	$('#intranet-body').css('background-color',' #e5faff');
	$('input[name="image"]').inputfile({
		uploadText: '<span class="glyphicon glyphicon-upload"></span> Upload an image',
        	removeText: '<span class="glyphicon glyphicon-trash"></span>',
        	restoreText: '<span class="glyphicon glyphicon-remove"></span>',
        
        	uploadButtonClass: 'btn btn-green',
        	removeButtonClass: 'btn btn-default',
    	});
	
        $('input[name="file_upload"]').inputfile({
		uploadText: '<span class="glyphicon glyphicon-upload"></span> Upload a file',
        	removeText: '<span class="glyphicon glyphicon-trash"></span>',
        	restoreText: '<span class="glyphicon glyphicon-remove"></span>',
        
        	uploadButtonClass: 'btn btn-green',
        	removeButtonClass: 'btn btn-default',
    	});
	window.showComments = function(postid){
		$("#comments-"+postid).show();
		$('#show-comments-'+postid).hide();
		$('.hide-comments-'+postid).show();
	}
	window.hideComments = function(postid){
		$('.show-comments').show();
		$("#comments-"+postid).hide();
		$(".hide-comments").hide();
	}
	$('#post-form').on('submit', function(event){
    		event.preventDefault();
    		console.log("form submitted!")  // sanity check
    		create_post();
	});
	window.comment_to_post = function(post_id){
		$.ajax({
        		url : "/comment_to_posts/", // the endpoint
        		type : "POST", // http method
        		data : { parent_post_id : post_id  }, // data sent with the post request

        		// handle a successful response
        		success : function(json) {
        		// remove the value from the input
			console.log(json);
          		},

        		// handle a non-successful response
        		error : function(xhr,errmsg,err) {
            		console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        		},
			crossDomain:false
    		});
	}
	
	
});
