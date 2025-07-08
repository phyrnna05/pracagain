import subprocess
import os

# Correct path to the actual Piper binary
PIPER_BIN = os.path.expanduser("~/piper/piper/piper")

VOICE_EN = os.path.expanduser("~/piper/voice_en.onnx")
VOICE_HI = os.path.expanduser("~/piper/voice_hi.onnx")


def speak_with_piper(text, lang="en-IN"):
    model = VOICE_HI if lang.startswith("hi") else VOICE_EN
    out_file = "/tmp/tts_out.wav"
    
    cmd = f'echo "{text}" | "{PIPER_BIN}" --model "{model}" --output_file "{out_file}"'
    
    # Run the Piper TTS command
    subprocess.run(cmd, shell=True, check=True)
    
    # Play the generated audio
    subprocess.run(['aplay', out_file], check=True)
