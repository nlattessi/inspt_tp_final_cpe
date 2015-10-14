$('#moverModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var handheld = button.data('handheld');
  var handheldSucursal = button.data('handheld-sucursal');
  $("#id_sucursal").val(handheldSucursal);
  var moverUrl = button.data('handheld-mover-url');
  $('#moverForm').attr('action', moverUrl);
  var modal = $(this);
  modal.find('.modal-title').text('Mover de sucursal la Handheld: ' + handheld);
});
