$(document).ready(function () {
    $("#media_type").change(function () {
        if ($(this).val() === "no_media") {
            $("#file_div").hide();
        } else {
            $("#file_div").show();
        }
    });
    $("#schedule_checkbox").change(function () {
        if ($(this).is(":checked")) {
            $("#schedule_datetime_div").show();
        } else {
            $("#schedule_datetime_div").hide();
        }
    });
    $("#group_send").change(function () {
        if ($(this).val() === "days" || $(this).val() === "games")  {
            $("#count_days_div").show();
        } else {
            $("#count_days_div").hide();
        }
    });
});