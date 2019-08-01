/////////////////////////////////////
//// DRAW ///////////////////////////
/////////////////////////////////////

// Inspired by https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx

var canvas, ctx, painting, paint_style;
var mouse = {x: 0, y: 0};
var training = true;
var host = window.location.hostname;


// Default
var path = [];
var action;

// Draw
function onPaint() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
}

// When the page is done loading, get the necessary elements of the page and load the drawing application
window.onload = function () {
    // Elements of the canvas
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    painting = document.getElementById('canvasDiv');
    paint_style = getComputedStyle(painting);

    // Prevent scrolling while drawing
    canvas.addEventListener("touchstart", function (event) {
        event.preventDefault()
    });
    canvas.addEventListener("touchmove", function (event) {
        event.preventDefault()
    });
    canvas.addEventListener("touchend", function (event) {
        event.preventDefault()
    });
    canvas.addEventListener("touchcancel", function (event) {
        event.preventDefault()
    });


    setPenSettings();

    // Add eventListeners to the canvas
    // Moving mouse
    canvas.addEventListener('mousemove', function (e) {
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
    }, false);

    // Mouse press
    canvas.addEventListener('mousedown', function (e) {
        //resetCanvas();
        ctx.beginPath();
        ctx.moveTo(mouse.x, mouse.y);
        canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    // Mouse release
    canvas.addEventListener('mouseup', function () {
        canvas.removeEventListener('mousemove', onPaint, false);
    }, false);

    // Equivalence for touch devices
    // Set up touch events for mobile, etc
    canvas.addEventListener("touchstart", function (e) {
        mousePos = getTouchPos(canvas, e);
        var touch = e.touches[0];
        mouse.x = touch.clientX;
        mouse.y = touch.clientY;
        var mouseEvent = new MouseEvent("mousedown", {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    }, {passive: true});

    canvas.addEventListener("touchend", function (e) {
        var mouseEvent = new MouseEvent("mouseup", {});
        canvas.dispatchEvent(mouseEvent);
    }, {passive: true});

    canvas.addEventListener("touchmove", function (e) {
        var touch = e.touches[0];
        var mouseEvent = new MouseEvent("mousemove", {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    }, {passive: true});

// Get the position of a touch relative to the canvas
    function getTouchPos(canvasDom, touchEvent) {
        var rect = canvasDom.getBoundingClientRect();
        return {
            x: touchEvent.touches[0].clientX - rect.left,
            y: touchEvent.touches[0].clientY - rect.top
        };
    }


    getCase();

};

// Set pen settings for the drawing part of the session.
function setPenSettings() {
    // Settings of ctx
    ctx.lineWidth = 30;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#00CC99';
}

function resetCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}


// Draw the case
function drawCase() {
    // Clear the canvas
    resetCanvas();
    // Draw path with arrow head
    var len = path.length;
    drawPath(path);
    drawArrowhead(ctx, path[len - 2], path[len - 1], 25);
}

// Draw path function
function drawPath(cse) {
    // Settings of ctx
    ctx.lineWidth = 10;
    ctx.lineJoin = 'square';
    ctx.lineCap = 'square';
    ctx.strokeStyle = 'black';

    ctx.beginPath();
    ctx.moveTo(cse[0].x, cse[0].y);
    for (i = 1; i < cse.length; i++) {
        ctx.lineTo(cse[i].x, cse[i].y);
    }
    ctx.stroke();

    setPenSettings();
}


// https://www.quackit.com/json/tutorial/json_with_http.cfm
// Make a connection with the server an load in the path of the test case.
function getCase() {

    var xhr = new XMLHttpRequest();
    var url = window.location.href + "get_case/";

// Called whenever the readyState attribute changes
    xhr.onreadystatechange = function () {
        //document.getElementById("actionToPerform").innerHTML = "<img src=\"{%  static \"img/loading.gif\" %}\" alt=\"Loading\">";

        // Check if fetch request is done
        if (xhr.readyState == 4 && xhr.status == 200) {

            // Parse the JSON string
            loadCase(JSON.parse(xhr.responseText));
        }
    };

// Do the HTTP call using the url variable we specified above
    xhr.open("GET", url, true);
    xhr.send();

}

// Change action displayed next to canvas.
function setAction(action) {
    document.getElementById("actionToPerform").innerHTML = action;
}

// Load case is used as callback function for getCase. It assigns the case path to the global variable path and draws
// this path in training mode.
function loadCase(data) {
    path = data.path;
    action = data.action;
    if (training) {
        drawCase(path)
    } else {
        resetCanvas()
    }
    setAction(action);
}

// Draw rectangle function, at the end of the line
// From https://gist.github.com/jwir3/d797037d2e1bf78a9b04838d73436197
function drawArrowhead(context, frm, to, radius) {
    var x_center = to.x;
    var y_center = to.y;

    var angle;
    var x;
    var y;

    context.beginPath();

    angle = Math.atan2(to.y - frm.y, to.x - frm.x);
    x = radius * Math.cos(angle) + x_center;
    y = radius * Math.sin(angle) + y_center;

    context.moveTo(x, y);

    angle += (1.0 / 3.0) * (2 * Math.PI);
    x = radius * Math.cos(angle) + x_center;
    y = radius * Math.sin(angle) + y_center;

    context.lineTo(x, y);

    angle += (1.0 / 3.0) * (2 * Math.PI);
    x = radius * Math.cos(angle) + x_center;
    y = radius * Math.sin(angle) + y_center;

    context.lineTo(x, y);

    context.closePath();

    context.fill();
}


/////////////////////////////////////
//// RECORD /////////////////////////
/////////////////////////////////////

// Inspired by https://codepen.io/jakebown/pen/weoVxg

var frames = [];
var host = window.location.hostname;
var date = new Date();
var start_time = date.getTime();
var recording = false;

function time() {
    date = new Date();
    return date.getTime() - start_time;
}

// Record mouse movements
$(window).mousemove(function (e) {
    if (recording) {
        var position = {"x": Math.round(e.clientX), "y": Math.round(e.clientY), "t": Math.round(time())};
        frames.push(position);
    }
});
// Touch movement
document.addEventListener('touchmove', function (e) {
    if (recording) {
        // e.preventDefault();
        var touch = e.touches[0];
        var position = {"x": Math.round(touch.pageX), "y": Math.round(touch.pageY), "t": Math.round(time())};
        frames.push(position);
    }
}, {passive: true});

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
            console.log("not tolerated");
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
    getCase();
    resetPathRecord();
}

var record = true;


