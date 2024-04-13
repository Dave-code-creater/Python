import time
from openai import OpenAI
from pathlib import Path
from pygame import mixer
import pyaudio
import wave
import RPi.GPIO as GPIO

import os
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
openai_client = os.getenv("OPENAI_API_KEY")

ledPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=button_pressed, bouncetime=300)

def record_voice_input(filename: str):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()

    frames = []

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    # Turn on the LED to indicate recording
    GPIO.output(ledPin, GPIO.HIGH)

    # Record audio until the button is released
    while GPIO.input(buttonPin) == GPIO.LOW:
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    # Turn off the LED after recording is done
    GPIO.output(ledPin, GPIO.LOW)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def button_pressed(channel):
    print("Button pressed")
    record_voice_input("user_input.wav")

def transcribe_audio(audio_file_path: str) -> str:
    # Transcribe the audio file using OpenAI Speech to Text API
    with open(audio_file_path, "rb") as audio_file:
        transcription = openai_client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcription.text

def speak(text: str):
    # Generate speech file using OpenAI API
    response = openai_client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    # Save speech file to disk
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response.stream_to_file(speech_file_path)

    # Play speech file using Pygame mixer
    mixer.init()
    mixer.music.load(str(speech_file_path))
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)
    mixer.quit()

    # Delete speech file after playing
    speech_file_path.unlink()

def get_openai_reply(message: str):
    try:
        # Send message to OpenAI chatbot
        response = openai_client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            model="gpt-3.5-turbo-0125"
        )

        # Get reply from OpenAI chatbot
        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        print("Error occurred during OpenAI conversation:", e)
        return "I'm sorry, I couldn't understand that."

def destroy():
    GPIO.cleanup()

def main():
    try:
        setup()
        print("Welcome! I'm your helpful assistant. Please press the button to start speaking.")
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("\nGoodbye! Have a great day.")
    finally:
        destroy()

if __name__ == "__main__":
    main()
