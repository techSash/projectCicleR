function getFile() {
    document.getElementById("upfile").click();
}

function sub(obj) {
    var file = obj.value;
    var fileName = file.split("\\");
    document.getElementById("yourBtn").innerHTML = fileName[fileName.length - 1];
    document.myForm.submit();
    event.preventDefault();
}

function image_form_submit(event) {
    event.preventDefault();
    var data = new FormData($('.image_upload_form').get(0));

    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,

        beforeSend: function () {
            $('.loading_gif_container').css('display', 'block');
            $(".result_container").load(" .result_container");
        },

        complete: function () {
            $('.loading_gif_container').css('display', 'none');
        },

        success: function (data) {
            status_msg = "image uploaded successfully"
            prediction_msg = "Prediction: " + data['prediction']

            $('#status').html(status_msg)
            $('.result').html(prediction_msg)
        }
    })

    return false;
}

$(function () {
    $('.image_upload_form').submit(image_form_submit);
})

$(document).ready(function() {
    $('.primary_button').click(function () {
        $('html, body').animate({scrollTop:$(document).height()}, 'slow');
        return false;
    });
})