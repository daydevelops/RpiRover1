function openSocket() {
    console.log('JS: opening socket connection');
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('JS: We are connected!')
        socket.emit('message', JSON.stringify("hello from js"));
    });

    socket.on('message', function(msg){
        console.log('JS: Hey, we got a message: ' + msg)
    });

    $('#num-input').keyup(() => {
        if ($('#num-input').val() !=='') {
            socket.emit('plzSqr', $('#num-input').val());
        }
    })

    socket.on('plzSqr-res',(msg) => {
        $('#num-output').html(msg);
    })
}

function closeSocket() {


}
