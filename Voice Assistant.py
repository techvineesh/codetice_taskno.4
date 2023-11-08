import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    # Create a recognizer object.
    recognizer = sr.Recognizer()

    # Start listening for speech.
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    # Try to recognize the speech.
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand.")
        return None

def process_voice_command(text):
    # If the user says "hello", say hello back.
    if "hello" in text:
        engine.say("Hello! vineesh")
        engine.runAndWait()

    # If the user asks for the time, tell them the time.
    if "time" in text:
        current_time = datetime.datetime.now().strftime("%H:%M")
        engine.say(f"The current time is {current_time}")

    # If the user asks for the weather, tell them the weather.
    if "weather" in text:
        engine.say("The weather is currently cloudy and clear.")

    # If the user asks to open a website, open the website.
    if "open Google" in text:
        webbrowser.open("https://www.google.com")

def main():
    # Create a while loop to run the assistant continuously.
    while True:
        # Listen for voice input.
        text = listen()

        # If the user said something, process the voice command.
        if text is not None:
            process_voice_command(text)
            engine.runAndWait()  # Speak the response

if __name__ == "__main__":
    main()
