const reponse = document.getElementById('answer1');
const start = document.getElementById('start');
const socket = new WebSocket('ws://localhost:8765');

start.addEventListener('click', function () {
        console.log('clickStart');
        socket.send('startGame');
        start.style.display = 'none';
    }
);
reponse.addEventListener('click', function () {
    console.log('clickChoice');
    socket.send('choicePlayer');
});

socket.onmessage = function (event) {
    console.log('Received message: ', event.data);
};
