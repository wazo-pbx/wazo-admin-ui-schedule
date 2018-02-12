$(document).ready(function () {
  init_time_picker.call(this);

  $('.row-template').on('row:cloned', function (e, row) {
    init_time_picker.call(row);
  });
});

function init_time_picker() {
  $('[class^=schedule_date_hours_]', this).timepicker({
    'timeFormat': 'H:i',
    'step': function (i) {
      return (i % 2) ? 15 : 45;
    }
  });
};
