from flask import Flask, render_template, request, jsonify
from chatbot import get_response


app = Flask(__name__)


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# CHAT API
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "response": "Please enter a question."
            })

        user_message = data.get(
            "message",
            ""
        )

        if not user_message.strip():

            return jsonify({
                "response": "Please enter a question."
            })

        response = get_response(
            user_message
        )

        return jsonify({
            "response": response
        })

    except Exception as error:

        print("ERROR:", error)

        return jsonify({
            "response": (
                "Sorry, something went wrong. "
                "Please try again."
            )
        })


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
