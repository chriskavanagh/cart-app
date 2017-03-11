/*$(function(){

	$('#mycart').hover(function(){
		$('#myModal').modal('show');	
	});		
});*/


$(function(){

	$('#likes').click(function(){
		var proid;
		proid = $(this).attr("data-proid");
		$.get('/shop/like_product/', {product_id: proid}, function(data){
			$('#like_count').html(data);
			$('#likes').hide();

		});
		
	});

});

		
	


