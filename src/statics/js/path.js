// Inspired by https://codepen.io/jakebown/pen/weoVxg

var frames = [];

// Record mouse movements
$(window).mousemove(function (e) {
    // button_pressed
    var position = {"x": e.clientX, "y": e.clientY};
    frames.push(position);
});

function reset_path() {
    frames = [];
}

// https://stackoverflow.com/questions/24468459/sending-a-json-to-server-and-retrieving-a-json-in-return-without-jquery
function send_input() {

    var xhr = new XMLHttpRequest();
    var url = "127.0.0.1";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify(frames);
    xhr.send(data);
}




var record = true;