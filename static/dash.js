/**
 * Created with PyCharm.
 * User: hemalatha_ganireddy
 * Date: 28/11/16
 * Time: 02:35
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function (){
    function get_status(device){
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/'+device,
            success: function (msg) {
                console.log(msg);
                $('#'+device +'_status').text(msg);
            },
            complete:function(){
                setTimeout(function(){get_status(device);}, 10000);
            }
        });
    }
    get_status('led');
    get_status('temperature');
    get_status('motor1');
    get_status('motor2');
});
