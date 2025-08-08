const API_URL = "http://127.0.0.1:5000/predict";

function appendMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");
    msgDiv.className = sender === "user" ? "user-msg" : "agent-msg";
    msgDiv.innerText = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("symptom-input");
    const symptoms = input.value.trim();
    if (!symptoms) return;

    appendMessage("user", symptoms);
    input.value = "";

    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symptoms })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("agent", `${data.text} (Confidence: ${data.confidence}%)`);
        if (data.tips) {
            appendMessage("agent", "Tips: " + data.tips.join(", "));
        }
    })
    .catch(err => {
        appendMessage("agent", "Error contacting AI agent.");
    });
}
