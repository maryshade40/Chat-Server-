from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return "📡 Chat server is running!"

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get("message")
    if message:
        messages.append(message)
        return jsonify({"status": "Message received"}), 200
    return jsonify({"error": "No message provided"}), 400

@app.route('/receive', methods=['GET'])
def receive():
    return jsonify({"messages": messages}), 200

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=10000)