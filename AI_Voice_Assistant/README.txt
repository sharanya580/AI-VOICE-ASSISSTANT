AI-Based Voice Assistant using Python

Overview:
--------------------------------------------------------------------------------
This project is a real-time AI Voice Assistant system that listens to voice commands, converts speech to text, and executes a variety of commands (e.g., getting the time, opening applications, searching Wikipedia) while giving a spoken voice response.

Files in this Directory:
--------------------------------------------------------------------------------
1. voice_assistant.py - High-level Python wrapper executing the assistant loop.
2. generate_docs.py - Script to generate the project's PDF documentation.
3. requirements.txt - Required libraries to install using pip.
4. README.txt - This file.

Prerequisites:
--------------------------------------------------------------------------------
1. Windows OS
2. Python 3.x Installed
3. Internet connection
4. Active microphone

Installation Instructions:
--------------------------------------------------------------------------------
1. Open a terminal or command prompt inside this folder.
2. Install the required dependencies:
   pip install -r requirements.txt

Running the Program:
--------------------------------------------------------------------------------
1. To start the Voice Assistant, run:
   python voice_assistant.py
   
2. Speak your commands clearly when prompted "Listening...".

Supported Commands:
--------------------------------------------------------------------------------
- "hello"
- "what is the time" or "time"
- "open notepad"
- "open calculator"
- "open chrome"
- "open google"
- "open youtube"
- "open gmail"
- "search python" (or "search [any topic]")
- "exit", "quit" or "stop"

Generate Documentation:
--------------------------------------------------------------------------------
1. Run the documentation script:
   python generate_docs.py
2. Check for `Project_Documentation.pdf` in the folder.
