from vosk import Model, KaldiRecognizer
import pyaudio
import json

def recognize_speech():
    model_en = Model("models/vosk-model-small-en-us-0.15")
    model_hi = Model("models/vosk-model-small-hi-0.22")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, frames_per_buffer=8000)
    stream.start_stream()

    rec_en = KaldiRecognizer(model_en, 16000)
    rec_hi = KaldiRecognizer(model_hi, 16000)

    for _ in range(80):  # listen ~5 seconds
        data = stream.read(4000, exception_on_overflow=False)

        if rec_hi.AcceptWaveform(data):
            result = json.loads(rec_hi.Result())
            text = result.get("text", "")
            if text:
                return text, "hi-IN"

        if rec_en.AcceptWaveform(data):
            result = json.loads(rec_en.Result())
            text = result.get("text", "")
            if text:
                return text, "en-IN"

    return "", "en-IN"
