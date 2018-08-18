var socket;
function openSocket() {
    console.log('JS: opening socket connection');
    socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('JS: We are connected!')
        socket.emit('message', JSON.stringify("hello from JS, time: " + Date.now()));
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


    initAccel();


}

function closeSocket() {


}
function initAccel() {
    // socket.emit('message', JSON.stringify("initAccel, time: " + Date.now()));
    var xout = document.querySelector('#xout'); //beta
    var yout = document.querySelector('#yout'); //gamma
    var zout = document.querySelector('#zout'); //alpha
    window.addEventListener('deviceorientation', function(event) {

        socket.emit('accelData', JSON.stringify({
            'x':(Math.round(event.beta*100))/100,
            'y':(Math.round(event.gamma*100))/100,
            'z':(Math.round(event.alpha*100))/100,
            't':Date.now()
        }))
        // socket.emit('message', JSON.stringify("inside listener, time: " + Date.now()));
        // alert('hi');
        // var alpha;
        // if (event.absolute) {
        //     alpha = event.alpha;
        // } else if (event.hasOwnProperty('webkitCompassHeading')) {
        //     // get absolute orientation for Safari/iOS
        //     alpha = 360 - event.webkitCompassHeading; // conversion taken from a comment on Google Documentation, not tested
        // } else {
        //     console.log('Could not retrieve absolute orientation');
        // }
        // console.log(alpha);
        // xout.innerHTML = (Math.round(event.beta*100))/100;
        // yout.innerHTML = (Math.round(event.gamma*100))/100;
        // zout.innerHTML = (Math.round(event.alpha*100))/100;
    });
    // socket.emit('message', JSON.stringify("listener added, time: " + Date.now()));
    window.addEventListener("compassneedscalibration", function(event) {
        alert('Your compass needs calibrating! Wave your device in a figure-eight motion');
        event.preventDefault();
    }, true);
 }
