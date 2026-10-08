const input = document.getElementById("message");
const chatBox = document.getElementById("chat-box");
const typing = document.getElementById("typing-indicator");


// Auto focus
window.addEventListener("load", () => {
    input.focus();
});


// Enter key
input.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        sendMessage();

    }

});


// Quick buttons
function askQuestion(question) {

    input.value = question;

    sendMessage();

}


// Focus
function focusChat() {

    input.focus();

}


// Send message
async function sendMessage() {

    const message = input.value.trim();

    if (!message) {

        input.focus();

        return;
    }


    // User bubble
    chatBox.innerHTML += `

        <div class="user-message">

            ${escapeHtml(message)}

        </div>

    `;


    chatBox.scrollTop =
        chatBox.scrollHeight;

    input.value = "";

    input.focus();


    // Typing
    typing.style.display = "flex";


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


        typing.style.display = "none";


        // Bot bubble
        chatBox.innerHTML += `

            <div class="bot-row">

                <div class="avatar">
                    🤖
                </div>

                <div class="message-area">

                    <div class="bot-message">

                        ${escapeHtml(
                            data.response
                        ).replace(/\n/g, "<br>")}

                    </div>

                </div>

            </div>

        `;


        chatBox.scrollTop =
            chatBox.scrollHeight;

        input.focus();

    }

    catch (error) {

        console.error(error);

        typing.style.display = "none";


        chatBox.innerHTML += `

            <div class="bot-row">

                <div class="avatar">
                    🤖
                </div>

                <div class="message-area">

                    <div class="bot-message">

                        Sorry, something went wrong.
                        Please try again.

                    </div>

                </div>

            </div>

        `;

        input.focus();
    }

}


// Prevent HTML injection
function escapeHtml(text) {

    const div =
        document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}
