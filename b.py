import no
import speech_recognition as sr

    
def hai():
    r = sr.Recognizer()
   
    with sr.Microphone() as source:                
        print("listenning...")
        audio = r.listen(source)
        cammand = r.recognize_google(audio)
        cammand = cammand.lower()
        print(cammand) 
   
    return cammand
result=hai()
no.open(result)
