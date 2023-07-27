function toast(msg) {
    alert(msg);
}

function connect() {
    var url = prompt('URL', 'localhost:8080');
    var socket = io(url);
    // , {
    //     path: "/socketio",
    // });
    //transports: ["websocket", "polling"]
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
}