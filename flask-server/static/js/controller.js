var socket, connected = false;

addEventListener('load',setUpControllerEvents);

function setUpControllerEvents() {

	console.log('page loaded');

	$('#power-on-btn').click(powerOn);
	$('#power-off-btn').click(powerOff);
	// $('#speed-input'). // need to figure out touch and drag events for mobile
	// $('#heading-input').
	$('#cam-left').click({'direction':'L'},turnCam);
	$('#cam-right').click({'direction':'R'},turnCam);

	$('#lmtrim-up').click({'L':1,'R':0}, changeTrim);
	$('#lmtrim-down').click({'L':-1,'R':0}, changeTrim);
	$('#rmtrim-up').click({'L':0,'R':1}, changeTrim);
	$('#rmtrim-down').click({'L':0,'R':-1}, changeTrim);

}

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
		data = JSON.parse(data);
		$('#lmtrim-val').html(data.L);
		$('#rmtrim-val').html(data.R);
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
}

function changeTrim(event) {
	socket.emit('updateTrim',{'L':event.data.L, 'R':event.data.R});
	console.log('asking server to update trim');
}

function turnCam(event) {
	// send change in camera heading left
	console.log(JSON.stringify(event.data,undefined,4));
}
