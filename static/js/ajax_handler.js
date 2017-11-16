$("#valid").hide();
console.log('we are here')

$('#btn-valid').click(function(){
      let id = $("span.tr_id").attr("id").split('-')[1];
      console.log(id);
      var url_str =  '/tr_valid/' + id;
      console.log(url_str);
      $.ajax({
      url: url_str,
      success: function(){
        $("#btn-valid").hide();
        $('#valid').show();
      }
    });
});