$("#signup_btn").click(function(event){
	event.preventDefault(); 	
	alert('hi');
	$.ajax({
		type : "POST",
		url : '/user-signup/',
		data : {'name':$('#name').val(),'email':$('#email').val(),'password':$('#password').val()},
		cache: false,
	    processData: false,
	    contentType: false,                       
                   
	    success: function (response) {
	        if(response.success=='true'){
	        $("#affiliate-modal1").modal('show');
	        $("#transaction_code1").text(response.transaction_code);
	        	}
				if (response.success == "false") {
					$("#error-modal1").modal('show');
					$("#error-message1").text(response.message);                                        
	 			}							                        		                      		                       		
	      },
	      				beforeSend: function () {
        $("#processing").css('display','block');
        },
        complete: function () {
            $("#processing").css('display','none');
        },
	      error : function(response){
	         	alert("_Error");
	   	}              
	  });  

});	
