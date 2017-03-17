$(function(){

	$('#like_link').click(function(){
		var proid;
		proid = $(this).attr("data-proid");
		$.get('/shop/like/', {product_id: proid}, function(data){
			 $('#like_num').html(data);
		});
		
	});

}); // end $(function()


/*$(function(){

	$('#likes').click(function(){
		var proid;
		proid = $(this).attr("data-proid");
		$.get('/shop/like_product/', {product_id: proid}, function(data){
			 $('#like_count').html(data);
			 //$('#likes').hide();
			 $('#likes').attr("disabled","disabled");

		});
		
	});

});*/


		
	


