$(document).ready(function() {
    $('#upload-form').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var formData = new FormData(this); // Create FormData object

        $.ajax({
            url: '{% url "upload_data" %}', // The URL for the request
            type: 'POST',
            data: formData,
            contentType: false, // Do not set content type
            processData: false, // Do not process data
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                // Upload progress event
                xhr.upload.addEventListener("progress", function(evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = (evt.loaded / evt.total) * 100;
                        $('#progress-bar').width(percentComplete + '%');
                        $('#progress-bar').text(Math.round(percentComplete) + '%');
                    }
                }, false);
                return xhr;
            },
            success: function(data) {
                $('#result-message').text('File uploaded successfully!');
                // Optionally, you can also clear the progress bar or do something else
                $('#progress-bar').width('0%').text('0%');
            },
            error: function(jqXHR, textStatus, errorThrown) {
                $('#result-message').text('Error uploading file. Please try again.');
            }
        });
    });
});
