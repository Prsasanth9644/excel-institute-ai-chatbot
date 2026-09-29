const input = document.getElementById("message");
const chatBox = document.getElementById("chat-box");

window.addEventListener("load", () => {
    input.focus();
});

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

    chatBox.innerHTML += `
        <div class="user-message">
            ${escapeHtml(message)}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";
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

        chatBox.innerHTML += `
            <div class="bot-message">
                ${escapeHtml(data.response).replace(/\n/g, "<br>")}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;
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

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}
