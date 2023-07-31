function connect() {
    var url = prompt('URL', 'localhost:8080');
    var socket = io(url, {
        // path: "/socketio",
        transports: ["websocket",],
        // transports: ["polling"],
    });
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
    socket.on('echo', function(msg) {
        console.log('<p>Received: ' + JSON.stringify(msg) + '</p>');
    });
}