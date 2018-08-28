var socket, connected = false;

addEventListener('load',setUpControllerEvents);

function powerOn() {
	console.log('powering on');
	openSocket();
	controllerOn();
	robotOn();
}

function powerOff() {
	console.log('powering down');
	closeSocket();
	controllerOff();
}

function openSocket() {
    console.log('opening socket connection');
    socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('We are connected!')
		connected = true;
    });

	socket.on('initTrim', (data) => {
		console.log(data)
		data = JSON.parse(data);
		$('#lmtrim-val').html(data['L']);
		$('#rmtrim-val').html(data['R']);
	});
}

function closeSocket() {
	// send disconnect msg to server
	socket.emit('disconnect');
	socket.disconnect();
	console.log('We have disconnected');
	connected = false;
}


function controllerOn() {
	$('#not-connected').css('display','none');
	$('#connected').css('display','block');
}

function controllerOff() {
	$('#connected').css('display','none');
	$('#not-connected').css('display','block');
}

function robotOn() {
	socket.emit('initRobot')
	console.log('Robot On');
}

function updateMotorSpeeds() {
	// read value of both sliders and send to server
	console.log('speed: '+$("#speed-input").val()+'    heading: '+$("#heading-input").val())
	data = {
		'speed':$('#speed-input').val(),
		'heading':$('#heading-input').val()
	}
	socket.emit('speedInput',data);
}

function changeTrim(data) {
	socket.emit('updateTrim',{'L':data.L, 'R':data.R});
	console.log('asking server to update trim');
}

function turnCam(data) {
	// send change in camera heading left
	console.log(JSON.stringify(data,undefined,4));
}
