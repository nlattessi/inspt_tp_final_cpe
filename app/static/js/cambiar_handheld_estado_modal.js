$('#cambiarModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var handheld = button.data('handheld');
  var handheldEstado = button.data('handheld-estado');
  $("#id_estado").val(handheldEstado);
  var cambiarUrl = button.data('handheld-cambiar-url');
  $('#cambiarForm').attr('action', cambiarUrl);
  var modal = $(this);
  modal.find('.modal-title').text('Cambiar estado Handheld: ' + handheld);
});
