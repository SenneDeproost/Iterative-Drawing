// Inspired by https://codepen.io/jakebown/pen/weoVxg

var frames = [];
var host = window.location.hostname;

// Record mouse movements
$(window).mousemove(function (e) {
    // button_pressed
    var position = {"x": e.clientX, "y": e.clientY};
    frames.push(position);
});

function resetPathRecord() {
    frames = [];
}

// https://stackoverflow.com/questions/24468459/sending-a-json-to-server-and-retrieving-a-json-in-return-without-jquery
function sendInput() {

    var data = JSON.stringify(frames);

    var xhr = new XMLHttpRequest();
    var url = "/training/post_case/";

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(data);
}


var record = true;