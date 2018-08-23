$(document).ready(function(){
  $('#id_cnpj').mask('00.000.000/0000-00', {placeholder: "Digite apenas os números"}) ;
  $('#id_agencia').mask('000-0', {placeholder: "Digite apenas os números"});
  $('#id_conta').mask('00.000-0', {placeholder: "Digite apenas os números"});
  $('#id_data_cadastro').mask('00/00/0000', {placeholder: "__/__/____"});
  $('#id_telefone').mask('(00) 00000-0000');

  $(".errorlist").addClass("alert alert-danger");

$('form#establish').find('input').each(function(){
    if(!$(this).prop('required')){
        console.log(this);
    } else {
        console.log(this);
    }
});
});