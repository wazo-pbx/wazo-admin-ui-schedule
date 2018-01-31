$(document).ready(function () {
  init_time_picker()
  $('.add-row-entry').click(function(e) {
    init_time_picker()
  });
});

function init_time_picker() {
  $('[class^=schedule_date_hours_]').timepicker({
    timeFormat: 'hh:mm',
  });
}