# Voice-Activated Personal Assistant 🎙️🤖

A **voice-activated personal assistant** designed to make your daily life easier by handling tasks such as setting reminders, checking the weather, reading news headlines, and more! 🌟 Powered by **speech recognition** and **text-to-speech** technologies, this project offers an interactive, hands-free experience.

---

## 🚀 Features

- **Voice Commands:** 🎤  
  - Understands and executes commands using Natural Language Processing (NLP).  

- **Supported Tasks:**  
  - 🕒 **Set Reminders** and manage personal tasks.  
  - 🌦️ **Get Weather Updates** for any city in real-time.  
  - 📰 **Read Top News Headlines** for staying informed.  
  - ✅ **Manage To-Do Lists** for better productivity.  
  - 💱 **Currency Conversion** (e.g., USD to EUR).  

- **Interactive and User-Friendly:**  
  - Listens to voice input and provides audible responses for a fully interactive experience.

---

## 🛠️ How It Works

1. **Speech Recognition:**  
   - Captures voice input using the `speech_recognition` library.  
   - Converts voice to text for further processing.

2. **Intent Classification:**  
   - Processes commands using NLP to classify intents with a Naive Bayes Classifier.

3. **Task Execution:**  
   - Handles requests like fetching weather data via APIs, managing tasks, and more.

4. **Text-to-Speech:**  
   - Responds audibly using the `pyttsx3` library.

---

## 🎯 Benefits

- **Automation:** Streamlines repetitive daily tasks.  
- **Productivity:** Quick and efficient reminders and task management.  
- **Real-Time Updates:** Stay informed with live weather and news.  
- **Hands-Free Use:** Perfect for multitasking or accessibility needs.

---

## 📦 Installation

1. **Clone the Repository:**
   ```
     git clone <repository_url>
     cd <repository_name>
2. **Install Dependencies:**
Ensure Python 3 is installed, then run:
```
  pip install -r requirements.txt
```
3. **Download NLTK Data:**
Install the necessary NLTK components:
```
    python -m nltk.downloader punkt
```
  Set Up API Keys:
        Weather API: Sign up at OpenWeatherMap and obtain your API key.
        News API: Sign up at NewsAPI for your API key.
        Replace the placeholders in the script with your API keys.

▶️ Usage

  Run the Assistant:

    python assistant.py

  Interact with the Assistant:
    Once running, the assistant will greet you and wait for commands like:
        🕒 "Set a reminder to drink water in 10 seconds."
        🌦️ "What's the weather like in New York?"
        📰 "Tell me the latest news."

  Stop the Assistant:
    Simply say "exit" to terminate the program.

🛠️ Requirements

  Python Version: 3.7 or higher
    Libraries:
        pyttsx3
        SpeechRecognition
        requests
        nltk
        pyautogui

🌟 Future Improvements

   Implement advanced NLP techniques for complex queries.
    Add integration with IoT devices for smart home control.
    Introduce context-aware conversation management.

🤝 Contributing

Contributions are welcome! 🎉

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -m "Add feature").
    Push to the branch (git push origin feature-branch).
    Open a pull request.

Enjoy your Voice-Activated Personal Assistant experience! 🎙️✨
