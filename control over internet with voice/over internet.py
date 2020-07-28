import pyttsx3
import speech_recognition as sr 
import serial
import time
import urllib.request, urllib.parse, urllib.error

print ("Hi!")
print ("Say turn ON light to light ON and turn OFF light to light off")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hi!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Listening...")
        audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
            return query
            
        except sr.UnknownValueError:
            print("I didn't hear your voice sir\n")
            return ""

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == '__main__':
    while True:
        query = takecommand()
        if query == "turn on light":
            data = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=3RRK24AR99TIRNOQ&field1=" + str(1));
            print("LED turned ON")
            speak("LED turned ON")
            time.sleep(1)

        if query == 'turn off light':
            data = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=3RRK24AR99TIRNOQ&field1=" + str(0));
            print("LED turned OFF")
            speak("LED turned OFF")
            time.sleep(1)
