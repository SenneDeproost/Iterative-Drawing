// Inspired by https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx

var canvas, ctx, painting, paint_style;
var mouse = {x: 0, y: 0};
var current_case = 0;


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
    }
];

// When the page is done loading, get the necessary elements of the page and load the drawing application
window.onload = function () {
    // Elements of the canvas
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    painting = document.getElementById('canvasDiv');
    paint_style = getComputedStyle(painting);

    // Settings of ctx
    ctx.lineWidth = 30;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#00CC99';

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

function onPaint() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
}
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    load_case(current_case);
}

function drawPoint(x, y) {
    ctx.fillRect(x, y, 20, 20);
}

function get_case(id){
    return data;
}

function load_case(id) {
    var cur_case = get_case(id);
    for (i = 0; i < data.length; i++) {
        drawPoint(data[i].x, data[i].y)
    }
}


