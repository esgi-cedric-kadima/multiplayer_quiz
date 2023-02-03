const socket = new WebSocket("ws://localhost:8000");

socket.onopen = function (event) {
    console.log("WebSocket is open now.");
    socket.send(JSON.stringify({ type: "start" }));
};

socket.onmessage = function (event) {
    console.log("Received message: " + event.data);
    const data = JSON.parse(event.data);
    if (data.type === "question") {
        const question = data.question;
        const answers = data.answers;
        // display the question and answers to the user here
    }
    if (data.type === "result") {
        const result = data.result;
        // display the result to the user here
    }
};

socket.onclose = function (event) {
    console.log("WebSocket is closed now.");
};
