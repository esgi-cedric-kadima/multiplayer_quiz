// Client JavaScript
const socket = new WebSocket('ws://localhost:8765');

socket.onopen = function (event) {
    socket.send('startGame');
};

socket.onmessage = function (event) {
    console.log('Received message: ', event.data);
    question = JSON.parse(event.data);
    console.log(question);
};

function makeChoice(choice) {
    socket.send(choice);
}