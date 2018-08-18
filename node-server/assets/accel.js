addEventListener('load',init);

function init() {
    var xout = document.querySelector('#xout'); //beta
    var yout = document.querySelector('#yout'); //gamma
    var zout = document.querySelector('#zout'); //alpha

    window.addEventListener('deviceorientation', function(event) {
        var alpha;
        if (event.absolute) {
            alpha = event.alpha;
        } else if (event.hasOwnProperty('webkitCompassHeading')) {
            // get absolute orientation for Safari/iOS
            alpha = 360 - event.webkitCompassHeading; // conversion taken from a comment on Google Documentation, not tested
        } else {
            console.log('Could not retrieve absolute orientation');
        }
        console.log(alpha);
        xout.innerHTML = (Math.round(event.beta*100))/100;
        yout.innerHTML = (Math.round(event.gamma*100))/100;
        zout.innerHTML = (Math.round(event.alpha*100))/100;
    });
    window.addEventListener("compassneedscalibration", function(event) {
        alert('Your compass needs calibrating! Wave your device in a figure-eight motion');
        event.preventDefault();
    }, true);


}
