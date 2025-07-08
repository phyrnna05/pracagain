import subprocess
import os

PIPER_BIN = os.path.expanduser("~/piper_install/piper")
VOICE_EN = os.path.expanduser("~/piper_install/voice_en.onnx")
VOICE_HI = os.path.expanduser("~/piper_install/voice_hi.onnx")

def speak_with_piper(text, lang="en-IN"):
    # Choose model based on language
    model = VOICE_HI if lang.startswith("hi") else VOICE_EN
    # Generate a temporary WAV file
    out_file = "/tmp/tts_out.wav"
    cmd = f'echo "{text}" | "{PIPER_BIN}" --model "{model}" --output_file "{out_file}"'
    subprocess.run(cmd, shell=True, check=True)
    subprocess.run(['aplay', out_file], check=True)
