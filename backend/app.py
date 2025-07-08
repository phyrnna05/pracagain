from flask import Flask, jsonify
from flask_cors import CORS
from vosk_stt import recognize_speech
from tts import speak_with_piper
import requests

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_llama(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    res = requests.post(OLLAMA_URL, json=payload)
    return res.json().get("response", "")

@app.route("/voice-chat", methods=["GET"])
def voice_chat():
    print("Listening...")
    input_text, lang = recognize_speech()
    print("User:", input_text)

    if not input_text:
        return jsonify({"error": "No input"}), 400

    reply = query_llama(input_text)
    print("LLaMA:", reply)

    speak_with_piper(reply, lang)
    return jsonify({"input": input_text, "reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
