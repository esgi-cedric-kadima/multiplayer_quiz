const reponse = document.getElementById('answer1');
const socket = new WebSocket('ws://localhost:8765');

reponse.addEventListener('click', function () {
    console.log('clickChoice');
    socket.send('choicePlayer');
});

socket.onmessage = function (event) {
    console.log('Received message: ', event.data);
};
