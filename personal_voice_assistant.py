import os
import webbrowser
import datetime
import wikipedia
import pywhatkit
import pyjokes
import win32com.client

# ===========================================
# PERSONAL VOICE ASSISTANT
# Author : Dev Setia
# Version : 2.0
# ===========================================

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def speak(text):
    print(f"\nAssistant : {text}")
    speaker.Speak(text)


def banner():
    print("=" * 60)
    print("        PERSONAL VOICE ASSISTANT")
    print("=" * 60)
    print("Author      : Dev Setia")
    print("Language    : Python")
    print("Version     : 2.0")
    print("=" * 60)


def greet():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your Personal Voice Assistant.")
    speak("How may I help you today?")


def show_help():

    print("\n============== AVAILABLE COMMANDS ==============\n")

    print("hello")
    print("how are you")
    print("time")
    print("date")
    print("joke")
    print("who is <person>")
    print("play <song>")
    print("open google")
    print("open youtube")
    print("open github")
    print("open calculator")
    print("open notepad")
    print("open explorer")
    print("help")
    print("exit")

    print("\n===============================================\n")


def main():

    os.system("cls")

    banner()

    greet()

    show_help()

    while True:

        command = input("\nYou : ").lower().strip()

        if command == "hello":

            speak("Hello! Nice to meet you.")

        elif command == "how are you":

            speak("I am doing great. Thank you for asking.")

        elif command == "time":

            current_time = datetime.datetime.now().strftime("%I:%M %p")

            speak(f"The current time is {current_time}")

        elif command == "date":

            current_date = datetime.datetime.now().strftime("%d %B %Y")

            speak(f"Today's date is {current_date}")

        elif command == "joke":

            speak(pyjokes.get_joke())

        elif command.startswith("who is"):

            person = command.replace("who is", "").strip()

            if person:
                try:
                    info = wikipedia.summary(person, sentences=2)
                    speak(info)
                except Exception:
                    speak("Sorry, I could not find information.")
            else:
                speak("Please enter a person's name.")

        elif command.startswith("play"):

            song = command.replace("play", "").strip()

            if song:
                speak(f"Playing {song} on YouTube.")
                pywhatkit.playonyt(song)
            else:
                speak("Please enter a song name.")

        elif command == "open google":

            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif command == "open youtube":

            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif command == "open github":

            speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        elif command == "open calculator":

            speak("Opening Calculator.")
            os.system("calc")

        elif command == "open notepad":

            speak("Opening Notepad.")
            os.system("notepad")

        elif command == "open explorer":

            speak("Opening File Explorer.")
            os.system("explorer")

        elif command == "help":

            show_help()

        elif command == "exit":

            speak("Thank you for using Personal Voice Assistant.")
            speak("Goodbye!")
            break

        else:

            speak("Sorry, I did not understand that command.")


if __name__ == "__main__":
    main()