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

// Reset canvas is used when a user wants to redo its input.
function drawCase() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Draw path when in training mode
    if (training) {
        drawPath(path);
    }
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
    drawCase(path);
    setAction(action);
}

