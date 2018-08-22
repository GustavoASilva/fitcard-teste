$.getJSON("/establishment/api/all/" , function( data ) {
    establishs_data = data;

    var trHTML = '';

    $.each(establishs_data, function (i, establish) {
         var deleteButtonHTML = '<td> <input id="' + establish.id + '"' +  'class="btn btn-danger delete" type="button" value="Deletar"> </td> '
         var editButtonHTML = '<td> <input id="' + establish.id + '"' +  'class="btn btn-warning edit" type="button value="Editar"> </td> '
         trHTML += '<tr> <td>'
         + establish.razao_social + '</td><td>'
         + establish.cnpj + '</td><td>'
         + establish.cidade + '</td><td>'
         + establish.estado + '</td><td>'
         + establish.telefone + '</td><td>'
         + establish.get_category_display  + '</td>'
         + deleteButtonHTML +  '<tr>'
    });
    $('#establishments').append(trHTML);

$(document).ready(function() {
$('input[class="btn btn-danger delete"]').click(function(e){
     var establish_id = this.id
     outer = this
     jQuery.ajax({
            type: "POST",
            url: "api/delete/" + establish_id,
            dataType: "json",
            success: function(){
                  if(data) {
                  alert("Estabelecimento deletado !");
                    $(outer).closest('tr').remove();
                  }
            }
        });


})

$('input[class="btn btn-warning edit"]').click(function(e){
     var establish_id = this.id
     outer = this
     jQuery.ajax({
            type: "POST",
            url: "api/delete/" + establish_id,
            dataType: "json",
            success: function(){
                  if(data) {
                  alert("Estabelecimento deletado !");
                    $(outer).closest('tr').remove();
                  }
            }
        });

})
});

});
