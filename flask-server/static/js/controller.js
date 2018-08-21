var socket;

addEventListener('load',() => {
	toggleSocketBtn('isclosed');
})

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

    initAccel();
    
    toggleSocketBtn('isopen');
}

function closeSocket() {
	toggleSocketBtn('isclosed');
	socket.disconnect();
}

function initAccel() {
    window.addEventListener('deviceorientation', function(event) {

        socket.emit('accelData', JSON.stringify({
            'x':(Math.round(event.beta*100))/100,
            'y':(Math.round(event.gamma*100))/100,
            'z':(Math.round(event.alpha*100))/100,
            't':Date.now()
        }))
    });
    // socket.emit('message', JSON.stringify("listener added, time: " + Date.now()));
    window.addEventListener("compassneedscalibration", function(event) {
        alert('Your compass needs calibrating! Wave your device in a figure-eight motion');
        event.preventDefault();
    }, true);
}

function toggleSocketBtn(cmd) {
	if (cmd==='isopen') {
		
        var btn = document.querySelector('#open-close-socket');
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-danger');
        btn.innerHTML = 'Close Socket';
        btn.removeEventListener('click',openSocket);
        btn.addEventListener('click',closeSocket)
        
    } else if (cmd==='isclosed') {
		
        var btn = document.querySelector('#open-close-socket');
        btn.classList.add('btn-primary');
        btn.classList.remove('btn-danger');
        btn.innerHTML = 'Open Socket';
        btn.addEventListener('click',openSocket);
        btn.removeEventListener('click',closeSocket)
        
	}
}
		
