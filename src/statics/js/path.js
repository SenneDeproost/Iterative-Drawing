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
    var url = window.location.href + "post_case/";

    xhr.onreadystatechange = function () {
        // Check if fetch request is done
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Handle answer from server
            handleRes(xhr.responseText);
        }

    };
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(data);
}

function handleRes(response) {
    // Can we go to the next case, do we have to retry or is the session over?
    switch (response) {
        case "tolerated":
            break;
        case "not tolerated":
            break;
        case "session done":
            if (training) {
                alert("Training session is complete");
                window.location.href = "./testing";
            }
            else{
                alert("Testing session is complete");
                window.location.href = "/";
            }
            break;
        default:
            break;
    }
}

var record = true;