import pyttsx3

def announce(announcement):
    '''This announces'''
    engine = pyttsx3.init()
    try:
        engine.endLoop()
    except:
        pass
    engine.say(announcement)
    engine.runAndWait()

