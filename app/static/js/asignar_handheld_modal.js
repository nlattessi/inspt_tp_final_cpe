$('#asignarModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var vendedor = button.data('vendedor') // Extract info from data-* attributes
  var asignarUrl = button.data('vendedor-asignar-url');
  $('#asignarForm').attr('action', asignarUrl);
  var modal = $(this)
  modal.find('.modal-title').text('Asignar Handheld al vendedor: ' + vendedor)
});
$('#asignarModal').on('hidden.bs.modal', function (event) {
  $('#id_handheld').val('');
});
