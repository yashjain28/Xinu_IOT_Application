$(document).ready(function () {
    $('#spclick').click(function () {
        console.log("Enter")
       var recognition = new webkitSpeechRecognition();
       recognition.onresult = function(event) {
           console.log(event)
           recognizedtext = event.results[0][0].transcript
           console.log(recognizedtext)
           if (recognizedtext.toLowerCase() == "led on") {
               $.ajax({
                   type: 'GET',
                   url: 'http://127.0.0.1:5000/led1',
                   success: function (msg) {
                       console.log(msg);
                       //set_weather_icon(msg);
                   }
               });
           }
       }
       recognition.start();
    })
    $('#btnclick').click(function () {
        console.log("bondy");
        //console.log(currentPosition);
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/',
            success: function (msg) {
                console.log(msg);
                $('#temperature').text(msg);
                $('#toggle').removeAttr('style');
                //set_weather_icon(msg);
            }
        });
    });
    $('#toggle').click(function () {
        if ($('#txt').html() === 'Celcius') {
            $('#txt').html('Farenhiet');
            $('#temperature').text(convert_celcius_to_farenhiet($('#temperature').html() - 0));
        } else {
            $('#txt').html('Celcius');
            $('#temperature').text(convert_farenhiet_to_celcius($('#temperature').html() - 0));
        }
    });
});

function set_weather_icon(msg) {
    var cond;
    switch (msg.weather[0].main) {
    case 'Clouds':
        cond = 'cloudy';
        break;
    case 'Thunderstorm':
        cond = 'thunderstorm';
        break;
    default:
        cond = 'sunny';
    }
    $('#weather-icon').addClass('wi-day-' + cond);
}
function convert_kelvin_to_celcius(temp) {
    return round(temp - 273.15);
}
function convert_celcius_to_farenhiet(temp) {
    return round(9 * temp / 5 + 32);
}
function convert_farenhiet_to_celcius(temp) {
    return round(5 * (temp - 32) / 9);
}
function round(num) {
    return Math.round(num * 100) / 100;
}