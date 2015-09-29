$(document).ready(function() {

    $('#run').on('click', function() {
        $.ajax({
            url: "/search",
            type: "GET",
            data: { entered_url: $("#entered_url").val() },
            success: function (data) {
                $("#result_text").val(data.result_text);
                $("#result_summary").val(data.result_summary);
            }
        })
    });

});
