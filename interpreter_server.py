from flask import Flask, request, jsonify
from interpreter import interpreter
import os

app = Flask(__name__)

interpreter.llm.model = "gpt-4o"
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.auto_run = True

@app.route('/run_interpreter', methods=['POST'])
def run_interpreter():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    result = interpreter.chat(prompt)

    return jsonify({"response": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)