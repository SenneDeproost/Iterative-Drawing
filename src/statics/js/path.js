// Inspired by https://codepen.io/jakebown/pen/weoVxg
var recorder = {

    var:resolution = 2,

    // Get coordinates of mouse
    capture:function() {
        var coordinates;
        $(window).mousemove(function (event) {
            coordinates = [event.clientX, event.clientY];
        });
        return this.coordinates;
    },


    // Record mouse movements and push coordinates in list
    listener:function() {
      $(window).mousemove(function(e) {

          setTimeout(this.listener, 1000/this.resolution)

      });
    }

};

/*
 * Listen for the mouse movements
 */
recorder.frames = [];
recorder.listener();