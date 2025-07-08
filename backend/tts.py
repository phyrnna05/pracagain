import pyttsx3

# Make the engine global so it doesn’t get garbage collected
engine = pyttsx3.init()

def speak_text(text, lang="en-IN"):
    voices = engine.getProperty("voices")

    selected_voice = None
    for voice in voices:
        if lang in voice.id:
            selected_voice = voice.id
            break

    if selected_voice:
        engine.setProperty("voice", selected_voice)

    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
