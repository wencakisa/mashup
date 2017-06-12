$('.datepicker').pickadate({
    selectMonths: true,
    selectYears: 1,
    min: new Date()
});

$('#from_date').change(() => {
    $('#to_date').pickadate('picker').set('min', new Date(this.value));
});

$('.timepicker').pickatime({
    autoclose: false,
    twelvehour: true,
    default: '12:00:00'
});

$('#eventDeleteBtn').on('click', () => {
    return confirm('Are you sure you want to delete this event?');
});
