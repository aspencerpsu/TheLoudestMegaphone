/**
 * Created by arunmavumkal on 11/5/16.
 */

$('#civilian_injured').val('0');
$('#civilian_killed').val('0');
$('#police_injured').val(0);
$('#police_killed').val(0);
// dynamic form fields with jquery

$('#inlineRadio1').click(function () {
    if($('#inlineRadio1').is(':checked')) {
        console.log('checked radio button to yes');
        $('#civilian_killed_label').text(function () {
            return 'Civilians Killed';
        });
        $('#civilian_injured_label').text(function () {
            return 'Civilians Injured';
        });
        $('#police_casualty_row').show('slow');
    }
});

$('#inlineRadio2').click(function () {
    if ($('#inlineRadio2').is(':checked')) {
        $('#civilian_killed_label').text(function () {
            return 'Killed';
        });
        $('#civilian_injured_label').text(function () {
            return 'Injured';
        });
        $('#police_casualty_row').css('display','none');
        $('#police_injured').val(0);
        $('#police_killed').val(0);
    }
});


/**
 * form validation scripts
 */

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

$('#civilian_killed').change(function () {
    if ($.isNumeric($('#civilian_killed').val()) && !($('#civilian_killed').val() == ''))
        $('#civilian_killed').css('border-color','#ccc');
});

$('#civilian_injured').change(function () {
    if ($.isNumeric($('#civilian_injured').val()) && !($('#civilian_injured').val() == ''))
        $('#civilian_injured').css('border-color','#ccc');
});

$('#police_killed').change(function () {
    if ($.isNumeric($('#police_killed').val()) && !($('#police_killed').val() == ''))
        $('#police_killed').css('border-color','#ccc');
});

$('#police_injured').change(function () {
    if ($.isNumeric($('#police_injured').val()) && !($('#police_injured').val() == ''))
        $('#police_injured').css('border-color','#ccc');
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

    if ($('#civilian_killed').val() == '') {
        $('#civilian_killed').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    } else if (!$.isNumeric($('#civilian_killed').val())) {
        $('#civilian_killed').css('border-color','red');
        $('#non_numeric_warning_killed').slideToggle('slow');
        submitform = false;
    }


    if ($('#civilian_injured').val() == '') {
        $('#civilian_injured').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    } else if (!$.isNumeric($('#civilian_injured').val())) {
        $('#civilian_injured').css('border-color','red');
        $('#non_numeric_warning_injured').slideToggle('slow');
        submitform = false;
    }

    if ($('#police_injured').val() == '') {
        $('#police_injured').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    } else if (!$.isNumeric($('#police_injured').val())) {
        $('#police_injured').css('border-color','red');
        $('#non_numeric_warning_injured').slideToggle('slow');
        submitform = false;
    }
    if ($('#police_killed').val() == '') {
        $('#police_killed').css('border-color','red');
        if (submitform)
            $('#required_fields_warning').slideToggle('slow');
        submitform = false;
    } else if (!$.isNumeric($('#police_killed').val())) {
        $('#police_killed').css('border-color','red');
        $('#non_numeric_warning_injured').slideToggle('slow');
        submitform = false;
    }
    if (submitform)
        return true;
    else
        event.preventDefault();

});

