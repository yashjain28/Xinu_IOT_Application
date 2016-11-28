$(document).ready(function() {
    $('#left').click(function() {
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/motor/left',
            success: function(resp) {
                console.log(resp);
            }
        });
    });
    $('#right').click(function() {
        console.log("working");
        //console.log(currentPosition);
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/motor/right',
            success: function(resp) {
                console.log(resp);
            }
        });
    });
    $('#bottom').click(function() {
        console.log("working");
        //console.log(currentPosition);
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/motor/backward',
            success: function(resp) {
                console.log(resp);
            }
        });
    });
    $('#up').click(function() {
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/motor/forward',
            success: function(resp) {
                console.log(resp);
            }
        });
    });
    $('#stop').click(function() {
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/motor/stop',
            success: function(resp) {
                console.log(resp);
            }
        });
    });
});