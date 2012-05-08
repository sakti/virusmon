//main.js

require.config({
    paths: {
        'jquery': 'lib/jquery/jquery-1.7.2.min',
        'underscore': 'lib/underscore',
        'mustache': 'lib/mustache',
        'backbone': 'lib/backbone',
        'bootstrap': 'lib/bootstrap/bootstrap.min',
        'd3': 'lib/d3/d3',
        'd3time': 'lib/d3/d3.time.min',
        'd3layout': 'lib/d3/d3.layout.min',
        'order': 'lib/require/order',
    }
});

require([
    'app',

    'order!underscore',
    'order!jquery',
    'order!mustache',
    'order!backbone',
    'order!d3',
    'order!d3time',
    'order!d3layout',
    'order!bootstrap',
    'order!app',
], function(app){
    // hack fix max width sidebar
    $(function(){
        resize = function(){
            $('#sidebar').css('height', $(window).height() + 10);
        }
        resize();

        $(window).bind('resize', resize);
    });

    app.initialize()
});