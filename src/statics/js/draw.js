// Inspired by https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx

var canvas, ctx, painting, paint_style;
var mouse = {x: 0, y: 0};
var current_case = 0;
var training = true;


var data = [
    {
        "x": 20,
        "y": 20
    },
    {
        "x": 80,
        "y": 20
    },
    {
        "x": 200,
        "y": 200
    },
    {
        "x": 700,
        "y": 400
    }
];

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
        //clearCanvas();
        ctx.beginPath();
        ctx.moveTo(mouse.x, mouse.y);
        canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    // Mouse release
    canvas.addEventListener('mouseup', function () {
        canvas.removeEventListener('mousemove', onPaint, false);
    }, false);


    load_case(current_case);

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

function drawPoints(case_) {
    for (i = 0; i < case_.length; i++) {
        ctx.fillRect(case_[i].x - 10, case_[i].y - 10, 20, 20);
    }
}

function drawPath(case_) {
    // Settings of ctx
    ctx.lineWidth = 10;
    ctx.lineJoin = 'square';
    ctx.lineCap = 'square';
    ctx.strokeStyle = 'black';


    ctx.beginPath();
    ctx.moveTo(case_[0].x, case_[0].y);
    for (i = 1; i < case_.length; i++) {
        ctx.lineTo(case_[i].x, case_[i].y);
    }
    ctx.stroke();
    setPenSettings();
}

// https://www.quackit.com/json/tutorial/json_with_http.cfm
function getCase(id) {
    return data
}

/*    // Store XMLHttpRequest and the JSON file location in variables
var xhr = new XMLHttpRequest();
var url = "127.0.0.1";

// Called whenever the readyState attribute changes
xhr.onreadystatechange = function() {

  // Check if fetch request is done
  if (xhr.readyState == 4 && xhr.status == 200) {

    // Parse the JSON string
    var jsonData = JSON.parse(xhr.responseText);

    // Call the showArtists(), passing in the parsed JSON string
    showArtists(jsonData);
  }
};

// Do the HTTP call using the url variable we specified above
xhr.open("GET", url, true);
xhr.send();
}*/

function load_case(id) {
    var cur_case = getCase(id);
    // Only draw case in training modus.
    if (training) {
        drawPoints(cur_case);
        drawPath(cur_case);
    }
}


