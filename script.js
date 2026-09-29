const input = document.getElementById("message");
const sendButton = document.getElementById("send-btn");
const chatBox = document.getElementById("chat-box");

// Page open ஆனவுடன் input box focus
window.addEventListener("load", () => {
    input.focus();
});

// Enter press = Send
input.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

async function sendMessage() {
    const message = input.value.trim();

    if (!message) {
        input.focus();
        return;
    }

    // User message display
    chatBox.innerHTML += `
        <div class="user-message">
            ${escapeHtml(message)}
        </div>
    `;

    // Scroll down
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input immediately
    input.value = "";

    // Keep focus on input
    input.focus();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        // Bot response
        chatBox.innerHTML += `
            <div class="bot-message">
                ${escapeHtml(data.response).replace(/\n/g, "<br>")}
            </div>
        `;

        // Scroll to latest message
        chatBox.scrollTop = chatBox.scrollHeight;

        // Automatically focus input again
        input.focus();

    } catch (error) {
        console.error(error);

        chatBox.innerHTML += `
            <div class="bot-message">
                Sorry, something went wrong. Please try again.
            </div>
        `;

        input.focus();
    }
}


// Prevent HTML injection
function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}