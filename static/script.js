
const input = document.getElementById("message");
const chatBox = document.getElementById("chat-box");
const typing = document.getElementById("typing-indicator");
const sendButton = document.getElementById("send-btn");

let isSending = false;

window.addEventListener("load", () => {
    input.focus();
});

// Enter key
input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

// Quick buttons: Institutions, Courses, Fees, Admission etc.
function askQuestion(question) {
    if (isSending) return;

    input.value = question;
    sendMessage();
}

// Send question to existing Flask backend
async function sendMessage() {
    const message = input.value.trim();

    if (!message || isSending) {
        if (!isSending) input.focus();
        return;
    }

    isSending = true;
    sendButton.disabled = true;

    // Display user question
    chatBox.insertAdjacentHTML(
        "beforeend",
        `<div class="user-message">${escapeHtml(message)}</div>`
    );

    input.value = "";
    typing.style.display = "flex";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        if (!response.ok) {
            throw new Error("Server response error");
        }

        const data = await response.json();

        // Display the chatbot answer
        const row = document.createElement("div");
        row.className = "bot-row";

        const avatar = document.createElement("div");
        avatar.className = "avatar";
        avatar.textContent = "🤖";

        const area = document.createElement("div");
        area.className = "bubble-area";

        const bubble = document.createElement("div");
        bubble.className = "bot-bubble";
        bubble.textContent =
            data.response || "Sorry, I couldn't find an answer.";

        const time = document.createElement("div");
        time.className = "time";
        time.textContent = "Excel AI Assistant";

        area.appendChild(bubble);
        area.appendChild(time);
        row.appendChild(avatar);
        row.appendChild(area);
        chatBox.appendChild(row);

    } catch (error) {
        console.error("Chat error:", error);

        const row = document.createElement("div");
        row.className = "bot-row";

        const bubble = document.createElement("div");
        bubble.className = "bot-bubble";
        bubble.textContent =
            "Sorry, connection problem. Please try again.";

        const area = document.createElement("div");
        area.className = "bubble-area";
        area.appendChild(bubble);

        row.appendChild(area);
        chatBox.appendChild(row);

    } finally {
        typing.style.display = "none";
        isSending = false;
        sendButton.disabled = false;
        chatBox.scrollTop = chatBox.scrollHeight;
        input.focus();
    }
}

// Safely display user messages
function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}
