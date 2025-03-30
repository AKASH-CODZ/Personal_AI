from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    """ Simple test AI: Replies to known inputs, else says 'I don't know.' """
    responses = {
        "hello": "Hi there! How can I help?",
        "how are you": "I'm good! What about you?",
        "bye": "Goodbye! Have a great day!"
    }

    return responses.get(user_input.lower(), "I don't know.")  # Default reply

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get("message")  # Get message from frontend
    bot_reply = chatbot_response(user_message)  # Get AI response
    return jsonify({"reply": bot_reply})  # Return response as JSON

if __name__ == '__main__':
    app.run(debug=True)
