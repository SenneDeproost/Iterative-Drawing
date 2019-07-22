// Inspired by https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx

var canvas, ctx, painting, paint_style;
var mouse = {x: 0, y: 0};
var current_case;
var case_index = 0;
var training = true;
var host = window.location.hostname;

// Default
var path = [];

// When the page is done loading, get the necessary elements of the page and load the drawing application
window.onload = function () {
    // Elements of the canvas
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    painting = document.getElementById('canvasDiv');
    paint_style = getComputedStyle(painting);

    setPenSettings();
    path = getCase(case_index);

    // Add eventListeners to the canvas
    // Moving mouse
    canvas.addEventListener('mousemove', function (e) {
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
    }, false);

    // Mouse press
    canvas.addEventListener('mousedown', function (e) {
        //clearCanvas();
        ctx.beginPath();
        ctx.moveTo(mouse.x, mouse.y);
        canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    // Mouse release
    canvas.addEventListener('mouseup', function () {
        canvas.removeEventListener('mousemove', onPaint, false);
    }, false);


    //load_case(case_index);

};

///////////////////////////////

function setPenSettings() {
    // Settings of ctx
    ctx.lineWidth = 30;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#00CC99';
}

function onPaint() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    load_case(current_case);
}

function drawPoints(cse) {
    for (i = 0; i < cse.length; i++) {
        ctx.fillRect(cse[i].x - 10, cse[i].y - 10, 20, 20);
    }
}

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
function getCase(id) {

    function result(request){
        return request
    }


    // Store XMLHttpRequest and the JSON file location in variables
    var xhr = new XMLHttpRequest();
    var url = "/training/get_case/" + String(id);

// Called whenever the readyState attribute changes
    xhr.onreadystatechange = function () {

        // Check if fetch request is done
        if (xhr.readyState == 4 && xhr.status == 200) {

            // Parse the JSON string
            path = JSON.parse(xhr.responseText);
        }
    };

// Do the HTTP call using the url variable we specified above
    xhr.open("GET", url, true);
    xhr.send();

}

async function load_case(id) {
    getCase(id);
   // console.log(cse);
    // Only draw case in training mode.
    if (training) {
        // drawPoints(cur_case);
        drawPath(path);
    }
}

