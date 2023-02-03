const reponse = document.getElementById('answer1');
const start = document.getElementById('start');
const socket = new WebSocket('ws://localhost:8765');

const question = document.getElementById('question');
const answer1 = document.getElementById('answer1');
const answer2 = document.getElementById('answer2');
const answer3 = document.getElementById('answer3');
const answer4 = document.getElementById('answer4');

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
    questionData = JSON.parse(event.data);
    console.log(questionData.question);

    question.innerHTML = questionData.question;
    answer1.innerHTML = questionData.options[0];
    answer2.innerHTML = questionData.options[1];
    answer3.innerHTML = questionData.options[2];
    answer4.innerHTML = questionData.options[3];
};
