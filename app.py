from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot(message):
    message = message.lower().strip()

    replies = {
    "hi": "Hello! 👋",
    "hello": "Hi! Nice to meet you.",
    "hey": "Hey! How can I help you?",
    "how are you": "I am fine. Thank you!",
    "i am fine": "That's great to hear!",
    "what is your name": "My name is AI Chatbot.",
    "who are you": "I am a chatbot created using Python and Flask.",
    "who created you": "I was created by Prachi using Python.",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI.",
    "what is flask": "Flask is a Python web framework.",
    "what can you do": "I can answer simple questions and chat with you.",
    "good morning": "Good Morning! 🌞",
    "good afternoon": "Good Afternoon! 😊",
    "good evening": "Good Evening! 🌇",
    "good night": "Good Night! 🌙",
    "thanks": "You're welcome!",
    "thank you": "My pleasure!",
    "bye": "Goodbye! Have a wonderful day!",
    "tell me a joke": "Why do programmers love Python? Because it's easy to read!",
    "how old are you": "I don't have an age like humans.",
    "where are you from": "I live inside this Flask application.",
    "are you human": "No, I am an AI chatbot.",
    "what is your favourite color": "I like blue because it looks cool!",
    "do you like music": "Yes! Music is amazing.",
    "who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
    "what is your favourite food": "I don't eat, but pizza sounds delicious! 🍕",
    "help": "You can ask me about AI, Python, Flask, greetings, jokes and more."
}

    return replies.get(message, "Sorry, I don't understand.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_message = request.form["message"]
    return jsonify({"reply": chatbot(user_message)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)