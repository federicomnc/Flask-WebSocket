$(document).ready(function() {

    var socket = io.connect('http://127.0.0.1:5000');

    $('#inizia').on('click', function() {

        socket.emit('inizia il gioco');
        /*var message = $('#message').val();

        socket.emit('message from user', message);*/
    });

     $('#Submit').on('click', function() {

        socket.emit('nome');
        /*var message = $('#message').val();

        socket.emit('message from user', message);*/
    });

/*

    socket.on('from Flask', function(msg) {

        alert(msg);
    });

    socket.on('server orginated', function(msg) {
        alert(msg)
    });

*/
    socket.on('redirect', function (data) {
        window.location = 'chivuolgiocare'
    });


})


/*
socket.on('connect', function() {
    socket.send('I am now connected!');

    socket.emit('custom event', {'nome' : 'Federico'});

    socket.on('from Flask', function(msg) {
        alert(msg['extension']);
    });

    socket.on('message', function(msg) {
        alert(msg);
    });
});
*/