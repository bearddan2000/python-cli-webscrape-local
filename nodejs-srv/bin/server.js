var app = require('express')();
var server = require('http').Server(app);

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

server.listen(8000);
