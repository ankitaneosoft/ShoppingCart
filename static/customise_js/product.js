$("#review_form").submit(function(event){
	event.preventDefault();
	var formData= new FormData();
	formData.append("name",$('#name').val());
	formData.append("email",$('#email').val());
	formData.append("review",$('#review').val());
	formData.append("product_id",$('#product_id').val()); 	
	$.ajax({
		type : "POST",
		url : '/product/add-review/',
		data : formData,
		cache: false,
	    processData: false,
	    contentType: false,                       
                   
	    success: function (response) {
	        if(response.success=='true'){
	        	$("#message").text(response.message); 
	        	}
				if (response.success == "false") {
				$("#message").text(response.message);                                        
	 			}							                        		                      		                       		
	      },

	      error : function(response){
	         	alert("_Error");
	   	}              
	  });  

});	
