const API_URL = "http://127.0.0.1:8000";

const input = document.getElementById("userInput");
const responseBox = document.getElementById("response");

function setLoading() {
    responseBox.textContent = "EduGenie is thinking...";
}

function showResponse(data) {
    const content =
        data.answer ||
        data.explanation ||
        data.quiz ||
        data.summary ||
        data.learning_path ||
        "No response received.";

    responseBox.innerHTML = marked.parse(content);
}

function showError(error) {
    responseBox.textContent = "Something went wrong: " + error;
}

async function callAPI(endpoint, parameter, value) {
    setLoading();

    try {
        const url =
            `${API_URL}${endpoint}?${parameter}=${encodeURIComponent(value)}`;

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        showResponse(data);

    } catch (error) {
        showError(error.message);
    }
}

function askAI() {
    const question = input.value.trim();

    if (!question) {
        responseBox.textContent = "Please enter a question.";
        return;
    }

    callAPI("/ask", "question", question);
}

function explainTopic() {
    const topic = input.value.trim();

    if (!topic) {
        responseBox.textContent = "Please enter a topic.";
        return;
    }

    callAPI("/explain", "topic", topic);
}

function generateQuiz() {
    const topic = input.value.trim();

    if (!topic) {
        responseBox.textContent = "Please enter a topic.";
        return;
    }

    callAPI("/quiz", "topic", topic);
}

function summarizeText() {
    const text = input.value.trim();

    if (!text) {
        responseBox.textContent = "Please enter some text.";
        return;
    }

    callAPI("/summarize", "text", text);
}

function learningPath() {
    const topic = input.value.trim();

    if (!topic) {
        responseBox.textContent = "Please enter a topic.";
        return;
    }

    callAPI("/learning-path", "topic", topic);
}