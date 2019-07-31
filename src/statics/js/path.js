// Inspired by https://codepen.io/jakebown/pen/weoVxg

var frames = [];
var host = window.location.hostname;
var date = new Date();
var start_time = date.getTime();
var recording = false;

function time(){
    date = new Date()
    return date.getTime() - start_time;
}

// Record mouse movements
$(window).mousemove(function (e) {
    if (recording) {
        var position = {"x": e.clientX, "y": e.clientY, "t": time()};
        frames.push(position);
    }
});

function resetPathRecord() {
    frames = [];
    var d = new Date();
    start_time = d.getTime();
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
                window.location.href = "/testing";
            } else {
                alert("Testing session is complete");
                window.location.href = "/thanks";
            }
            break;
        default:
            break;
    }
}

var record = true;