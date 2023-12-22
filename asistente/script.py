import numpy as np
import os
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
import transformers


class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.text = ""
        self.name = name
    
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Escuchando...")
            audio = recognizer.listen(mic, timeout=5)
            try:
                self.text = recognizer.recognize_google(audio, language="es-ES")
                print("Has dicho:", self.text)
            except sr.UnknownValueError:
                print("Lo siento, no te he entendido")
            except sr.RequestError as e:
                print("Error en la solicitud del servicio de reconocimiento de voz: {0}".format(e))
    
    def wake_up(self, text):
        '''self.speech_to_text()
        if "Jimeno" in self.text:
            self.text = ""
            self.speak("Hola, ¿en qué puedo ayudarte?")
            self.speech_to_text()
            self.chat()
        else:
            self.wake_up()'''
        return True if self.name in text.lower() else False
    
    @staticmethod
    def text_to_speech(self, text):
        print("Jimeno:", text)
        engine = gTTS(test=text, lang="es", slow=False)
        engine.save("res.mp3")
        os.system("start res.mp3")
        os.remove("res.mp3")

    @staticmethod
    def action_time(self):
        return datetime.datetime.now().strftime("%H:%M")
    
    def chat(self):
        while True:
            self.speech_to_text()
            if self.wake_up():
                res = "Hola ¿qué tal? Soy " + self.name + " tu asistente personal ¿en qué puedo ayudarte?"
                self.text_to_speech(res)
            elif "hora" in self.text:
                self.action_time()
            elif any(i in self.text for i in ["adiós", "hasta luego", "hasta pronto"]):
                res = "Hasta luego"
                self.text_to_speech(res)
                break
            elif any(i in self.text for i in ["gracias", "gracias por tu ayuda"]):
                res = "No hay de qué"
                self.text_to_speech(res)

if __name__ == "__main__":
    ai = ChatBot(name="jimeno")

    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    nlp(transformers.Conversation("Hola"))
    nlp(transformers.Conversation("Hola"))
    chat = nlp(transformers.Conversation(ai.text))
    res = str(chat)
    res = res[res.find("bot >> ")+6:].strip()

    while True:
        ai.speech_to_text()
        if ai.wake_up(ai.text) is True:
            res = "Hola ¿qué tal? Soy " + ai.name + " tu asistente personal ¿en qué puedo ayudarte?"
        elif "hora" in ai.text:
            res = ai.action_time()
        elif any(i in ai.text for i in ["adiós", "hasta luego", "hasta pronto"]):
            res = np.random.choice(["Hasta luego", "Hasta pronto", "Adiós"])
            ai.text_to_speech(res)
        elif any(i in ai.text for i in ["gracias", "gracias por tu ayuda"]):
            res = np.random.choice(["No hay de qué", "De nada"])
            ai.text_to_speech(res)