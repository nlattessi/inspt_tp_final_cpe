$('#removerModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget);
  var vendedor = button.data('vendedor');
  var removerUrl = button.data('vendedor-remover-url');
  $('#removerForm').attr('action', removerUrl);
  var modal = $(this);
  modal.find('.modal-title').text('Remover Handheld al vendedor: ' + vendedor);
});
