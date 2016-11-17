/**
 * Created by arunmavumkal on 11/5/16.
 */


// dynamic form fields with jquery

$('#inlineRadio1').click(function () {
    if($('#inlineRadio1').is(':checked')) {
        console.log('checked radio button to yes');
        $('#civilian_killed_label').text(function () {
            return 'Civilians Killed';
        });
    }
});



// reset red border after correction.

$('#datetimepicker1').change(function () {
    $('#datetimepicker1').css('border-color','#ccc');
});

$('#city').change(function () {
    if (!$('#city').val() == '')
        $('#city').css('border-color','#ccc');
});

$('#states_list').change(function () {
    if (!$('#states_list').val() == '')
        $('#states_list').css('border-color','#ccc');
});

$('#killed').change(function () {
    if ($.isNumeric($('#killed').val()) && !($('#killed').val() == ''))
        $('#killed').css('border-color','#ccc');
});

$('#injured').change(function () {
    if ($.isNumeric($('#injured').val()) && !($('#injured').val() == ''))
        $('#injured').css('border-color','#ccc');
});


// checks submission for errors.

$("#gvform").submit(function (event) {

    var submitform = true;
    $('#required_fields_warning').css('display','none');
    $('#non_numeric_warning_killed').css('display','none');
    $('#non_numeric_warning_injured').css('display','none');
    $('#required_fields_warning').css('display','none');
    if ($('#datetimepicker1').val() == '') {
        $('#datetimepicker1').css('border-color','red');
        $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    }

    if ($('#city').val() == '') {
        $('#city').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    }

    if ($('#states_list').val() == '') {
        $('#states_list').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    }

    if ($('#killed').val() == '') {
        $('#killed').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    } else if (!$.isNumeric($('#killed').val())) {
        $('#killed').css('border-color','red');
        $('#non_numeric_warning_killed').slideToggle('slow');
        submitform = false;
    }


    if ($('#injured').val() == '') {
        $('#injured').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    } else if (!$.isNumeric($('#injured').val())) {
        $('#injured').css('border-color','red');
        $('#non_numeric_warning_injured').slideToggle('slow');
        submitform = false;
    }
    if (submitform)
        return true;
    else
        event.preventDefault();

});

