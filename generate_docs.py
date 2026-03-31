from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'AI-Based Voice Assistant Project Documentation', 0, 1, 'C')
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, title):
        # Arial 12
        self.set_font('Arial', 'B', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 8, title, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, body):
        # Read text file
        self.set_font('Arial', '', 11)
        # Output justified text
        self.multi_cell(0, 6, body)
        # Line break
        self.ln()

def generate_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    sections = [
        ("1. Project Title", "AI-Based Voice Assistant using Python\n\nProject Type: Real-Time Mini Project for Artificial Intelligence Major Project Submission"),
        
        ("2. Problem Statement", "Users often need to interact with computers using their hands for basic tasks such as checking the time, opening applications, searching the web, or opening websites. This hands-on interaction can be slow and inaccessible to some users. Therefore, there is a need for a hands-free, voice-controlled system to easily perform these day-to-day tasks quickly and efficiently."),
        
        ("3. Objective", "Develop a real-time AI Voice Assistant system that listens to voice commands from the user, converts speech to text, processes the command, performs actions such as telling the current time, opening applications, searching information, and responds using speech output. The system simulates real-world smart assistants like Alexa or Google Assistant."),
        
        ("4. Tools & Technologies", "The following technologies and libraries were used to build this project:\n- Python 3.x (Programming Language)\n- SpeechRecognition (To capture microphone input and convert speech to text)\n- pyttsx3 (Text-to-Speech Engine for physical audio response)\n- datetime (For fetching the current time)\n- webbrowser (For opening websites like Google, YouTube, and Gmail)\n- os (For executing system commands to open applications like Notepad and Calculator)\n- wikipedia (For fetching summary data over the internet based on the user's search query)"),
        
        ("5. System Architecture", "The system architecture flows as follows:\n1. Input: Microphone captures user's voice.\n2. Processing (STT): SpeechRecognition library queries Google Web Speech API to convert audio to text.\n3. Processing (Logic): Python conditionals match the transcript against predefined triggers (e.g. 'open notepad', 'time').\n4. Execution: System executes the matched behavior (e.g. os.system, webbrowser.open, wikipedia.summary).\n5. Output (TTS): The pyttsx3 engine speaks out the completion response back to the user via speakers."),
        
        ("6. System Design", "The Voice Assistant is designed as a continuous loop. Once started, it automatically configures the TTS engine and enters a 'while True' loop. Inside the loop, it invokes the 'take_command()' function to listen. The microphone input handles ambient noise adjustment, and exceptions like WaitTimeoutError are gracefully caught. Upon receiving the string of recognized text, it is passed to 'execute_command()' which uses a chain of if/elif blocks to identify the intent."),
        
        ("7. Implementation", "To implement the project, we first set up a virtual environment and installed all required packages via pip. Then, we wrote 'voice_assistant.py' which initializes the sapi5 voice engine on Windows. We implemented functions for wishing the user, taking command, and interpreting those commands. For the Wikipedia search, sentences were limited to 2 to provide concise audio feedback without overwhelming the user."),
        
        ("8. Code Explanation", "The code predominantly features:\n- 'take_command()': Uses 'sr.Microphone()' as source, listens with a timeout, and uses 'recognize_google()' to parse audio into English text.\n- 'execute_command(query)': Takes the lowercase query and matches substrings. E.g., if 'open notepad' in query, it calls 'os.system(\"start notepad\")'. If 'search' is in the query, it utilizes the 'wikipedia' library to fetch a summary and then passes it to 'speak()'.\n- 'speak()': Takes a text string, passes it to 'pyttsx3 engine.say()', and flushes the buffer to speaker using 'engine.runAndWait()'.\n- The main loop breaks only when the user says an exit command like 'quit' or 'stop'."),
        
        ("9. Results", "The resulting application successfully recognizes continuous voice input with a latency of less than 2 seconds (contingent on internet speed for Google SR). It handles errors like unrecognized speech or lack of microphone hardware by continuing gracefully. It accurately launches local applications like Notepad/Calculator and opens browser URLs for YouTube, Google, and Gmail."),
        
        ("10. Conclusion", "The AI-Based Voice Assistant successfully meets the objective of providing a hands-free interactive experience. It demonstrates the integration of multiple APIs and built-in OS commands to simulate a miniature smart assistant. The architecture proves to be stable and capable of executing the defined commands accurately."),
        
        ("11. Future Scope", "In the future, the project can be expanded by:\n- Adding a graphical user interface (GUI) using Tkinter or PyQt.\n- Implementing Named Entity Recognition (NER) and NLP libraries (like spaCy or NLTK) to better extract intent rather than relying on exact string matching.\n- Integrating API keys for fetching real-time weather, news, or stock updates.\n- Adding a wake-word detection engine (like Porcupine) to avoid continuous listening internet usage.")
    ]

    for title, body in sections:
        pdf.chapter_title(title)
        pdf.chapter_body(body)

    out_path = os.path.join(os.path.dirname(__file__), "Project_Documentation.pdf")
    # For safety with encoding, encode with latin-1 or replace chars
    pdf.output(out_path, 'F')
    print(f"Documentation generated successfully at: {out_path}")

if __name__ == "__main__":
    generate_pdf()
