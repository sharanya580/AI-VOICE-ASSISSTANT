import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import sys
import io

# Initialize the text-to-speech engine
try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Choose default voice
except Exception as e:
    print(f"Error initializing TTS engine: {e}")
    engine = None

def speak(audio):
    """Function to convert text to speech"""
    print(f"Assistant: {audio}")
    if engine:
        engine.say(audio)
        engine.runAndWait()

def wish_me():
    """Greet the user based on the current time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your AI Voice Assistant. How can I help you today?")

def take_command():
    """Listen to user voice commands using sounddevice and convert speech to text"""
    print("\nListening (5s)...")
    fs = 44100
    duration = 5  # seconds
    try:
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
    except Exception as e:
        print(f"Error accessing microphone: {e}")
        return "None"

    try:
        print("Recognizing...")
        byte_io = io.BytesIO()
        sf.write(byte_io, myrecording, fs, format='WAV', subtype='PCM_16')
        byte_io.seek(0)
        
        r = sr.Recognizer()
        with sr.AudioFile(byte_io) as source:
            audio = r.record(source)

        # Use Google Web Speech API for recognition (requires internet)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Unknown Command... Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("I am having trouble connecting to the internet.")
        return "None"
    except Exception as e:
        print(f"Speech recognition error: {e}")
        return "None"

    return query.lower()

def execute_command(query):
    """Identify command using conditional logic and perform actions"""
    
    if 'hello' in query:
        speak("Hello! How are you doing?")

    elif 'what is the time' in query or 'time' in query:
        str_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {str_time}")

    elif 'open ' in query:
        app_name = query.replace('open ', '').strip()
        if not app_name:
            speak("What do you want me to open?")
            return True

        
        # Check if it's a known website first
        websites = {
            'google': 'https://www.google.com',
            'youtube': 'https://www.youtube.com',
            'gmail': 'https://mail.google.com',
            'instagram': 'https://www.instagram.com'
        }
        
        if app_name in websites:
            speak(f"Opening {app_name.title()}...")
            webbrowser.open(websites[app_name])
        else:
            speak(f"Attempting to open {app_name}...")
            try:
                from AppOpener import open as appopen
                appopen(app_name, match_closest=True, throw_error=True)
            except Exception as e:
                # Reply not found as requested
                speak(f"I could not find the application {app_name} on your system.")

    elif 'search' in query:
        search_query = query.replace("search", "").strip()
        if search_query:
            speak(f"Searching Wikipedia for {search_query}...")
            try:
                results = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are multiple results for {search_query}. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"I could not find any information about {search_query} on Wikipedia.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
        else:
            speak("What do you want me to search for?")

    elif 'exit' in query or 'quit' in query or 'stop' in query:
        speak("Goodbye! Have a great day.")
        return False
        
    else:
        speak(f"Searching the web for {query}")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        
    return True

def main():
    print("================================")
    print("   AI Voice Assistant System    ")
    print("================================")
    
    try:
        wish_me()
    except Exception as e:
        print("Initialization error. Check audio devices.")
        sys.exit(1)
    
    # Continuous listening system
    while True:
        command = take_command()
        
        if not command or command.lower() == "none":
            continue
            
        continue_running = execute_command(command)
        
        if not continue_running:
            break

if __name__ == "__main__":
    main()
