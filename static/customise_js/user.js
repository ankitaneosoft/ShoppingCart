$("#signup_form").submit(function(event){
	event.preventDefault();
	var formData= new FormData();
	formData.append("name",$('#name').val());
	formData.append("email",$('#email').val());
	formData.append("password",$('#password').val());
 	
	$.ajax({
		type : "POST",
		url : '/user/signup/',
		data : formData,
		cache: false,
	    processData: false,
	    contentType: false,                       
                   
	    success: function (response) {
	        if(response.success=='true'){
	        	location.href = '/home/'
	        	}
				if (response.success == "false") {
					$("#error-message").text(response.message);                                        
	 			}							                        		                      		                       		
	      },

	      error : function(response){
	         	alert("_Error");
	   	}              
	  });  

});	


<!-- signin method -->
$("#signin_form").submit(function(event){
	event.preventDefault();
	var formData= new FormData();
	formData.append("email",$('#user_email').val());
	formData.append("password",$('#user_password').val());
 	
	$.ajax({
		type : "POST",
		url : '/user/signin/',
		data : formData,
		cache: false,
	    processData: false,
	    contentType: false,                       
                   
	    success: function (response) {
	        if(response.success=='true'){
	        	location.href = '/home/'
	        	}
				if (response.success == "false") {
					$("#signin-error-message").text(response.message);                                        
	 			}							                        		                      		                       		
	      },

	      error : function(response){
	         	alert("_Error");
	   	}              
	  });  

});	
