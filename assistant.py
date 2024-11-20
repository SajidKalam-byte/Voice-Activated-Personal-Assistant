import pyttsx3
import speech_recognition as sr
import requests
import datetime
import os
import nltk
import time
import subprocess
import json
import random
import pyautogui
import webbrowser
from nltk.classify import NaiveBayesClassifier

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)

# Load user preferences
def load_preferences():
    try:
        with open("user_preferences.json", "r") as file:
            preferences = json.load(file)
        return preferences
    except FileNotFoundError:
        return {"voice_gender": "female"}

# Set voice properties
def set_voice(gender="female"):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id if gender == "female" else voices[0].id)

# Text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greeting based on time of day
def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How may I assist you today?")

# Take voice command
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except Exception:
        speak("Could you please repeat that?")
        return "None"

# Load training data
def load_training_data(file="training_data.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

training_data = load_training_data()

# Extract features for intent recognition
def extract_features(sentence):
    words = nltk.word_tokenize(sentence)
    bigrams = nltk.bigrams(words)
    features = {word: True for word in words}
    features.update({"_".join(bigram): True for bigram in bigrams})
    return features

# Train the intent classifier
def train_classifier():
    feature_set = [(extract_features(item["text"]), item["intent"]) for item in training_data]
    return NaiveBayesClassifier.train(feature_set)

classifier = train_classifier()

# New features
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid="YourApiKey"&units=metric"
        response = requests.get(url, timeout=10)
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The current temperature in {city} is {temperature}°C with {description}.")
    except Exception as e:
        speak("Unable to fetch weather information.")
        print(e)

def get_news():
    api_key = "your_api_key"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        response = requests.get(url)
        articles = response.json()["articles"]
        for i, article in enumerate(articles[:5]):
            speak(f"News {i+1}: {article['title']}")
    except Exception as e:
        speak("Unable to fetch news.")
        print(e)

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
        response = requests.get(url)
        rates = response.json()["rates"]
        converted = float(amount) * rates[to_currency.upper()]
        speak(f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}.")
    except Exception as e:
        speak("Unable to convert currency.")
        print(e)

def set_reminder(task, duration):
    speak(f"Reminder set for {duration} seconds.")
    time.sleep(int(duration))
    speak(f"Reminder: {task}")

tasks = []

def manage_tasks(action, task=None):
    if action == "add":
        tasks.append(task)
        speak(f"Task '{task}' added.")
    elif action == "view":
        if tasks:
            speak("Your tasks are:")
            for i, t in enumerate(tasks):
                speak(f"Task {i+1}: {t}")
        else:
            speak("No tasks found.")

# Main function
def main():
    preferences = load_preferences()
    set_voice(gender=preferences["voice_gender"])
    wishMe()

    while True:
        query = take_command().lower()
        if "exit" in query:
            speak("Goodbye!")
            break

        intent = classifier.classify(extract_features(query))
        if intent == "get_weather":
            speak("Which city?")
            city = take_command()
            get_weather(city)
        elif intent == "get_news":
            get_news()
        elif intent == "convert_currency":
            speak("Amount?")
            amount = take_command()
            speak("From which currency?")
            from_currency = take_command()
            speak("To which currency?")
            to_currency = take_command()
            convert_currency(amount, from_currency, to_currency)
        elif intent == "set_reminder":
            speak("What should I remind you about?")
            task = take_command()
            speak("After how many seconds?")
            duration = take_command()
            set_reminder(task, duration)
        elif intent == "add_task":
            speak("What task would you like to add?")
            task = take_command()
            manage_tasks("add", task)
        elif intent == "view_tasks":
            manage_tasks("view")
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    nltk.download('punkt')
    main()
