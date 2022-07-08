import pyttsx3
engine = pyttsx3.init()

def findIndex(itemId, items):
    for index, item in enumerate(items):
        if item.id == itemId:
            return index
    return -1

def findElement(itemId, items):
    index = findIndex(itemId, items)
    index = 0 if index == -1 else index
    return items[index]

def initEngine():
    voices = engine.getProperty("voices")
    voice = findElement("com.apple.speech.synthesis.voice.lekha.premium", voices)
    engine.setProperty("voice", voice.id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    initEngine()
    speak("नमस्ते, आप कैसे हैं? ")