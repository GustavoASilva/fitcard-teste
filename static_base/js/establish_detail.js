$.getJSON("/establishment/api/all/" , function( data ) {
    establishs_data = data;

     var trHTML = '';

    $.each(establishs_data, function (i, establish) {
         var detailButtonHTML = ' <td> <input id="' + establish.id + '"' +  'class="btn btn-dark detail" type="button" value="Detalhes">   '
         var editButtonHTML = ' <input id="' + establish.id + '"' +  'class="btn btn-warning edit" type="button" value="Editar">'
         var deleteButtonHTML = ' <input id="' + establish.id + '"' +  'class="btn btn-danger delete" type="button" value="Deletar"> </td>  '
         trHTML += '<tr> <td>'
         + establish.razao_social + '</td><td>'
         + establish.cnpj + '</td><td>'
         + establish.cidade + '</td><td>'
         + establish.estado + '</td><td>'
         + establish.telefone + '</td><td>'
         + establish.get_category_display  + '</td>'
         + detailButtonHTML
         + editButtonHTML
         + deleteButtonHTML
         + '</tr>'
    });
    $('#establishments').append(trHTML);