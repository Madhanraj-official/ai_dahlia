from gtts import gTTS
from playsound import playsound
import wikipedia
import speech_recognition as sr
import no

language='en-in'


    
def hai():
    r = sr.Recognizer()
   
    with sr.Microphone() as source:                
        print("listenning...")
        audio = r.listen(source)
        cammand = r.recognize_google(audio)
        cammand = cammand.lower()
        print(cammand) 
   
    return cammand

def ai():
    n=open("name.txt","rt")
    name=n.read()
    n.close()
    j="hai i'm "+name+". your personal voice  assistant. "+name+" is now online.which help would you want sir! "
    speech = gTTS(text=j,lang=language,slow=False,tld="com.au")
    speech.save("no.mp3")
    playsound("no.mp3")

def say(result):
    print(result)
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    speech.save('my.mp3')
    playsound('my.mp3')  
def saying(result):
    result='openning '+result
    print(result)
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    speech.save('my.mp3')
    playsound('my.mp3')
def one():
            
    she='agalya is your dream girl real life character,you have love this girl one side and you have love on the girl mostly'
    speech = gTTS(text=she,lang=language,slow=False,tld="com.au")
    print(speech)
    speech.save("my.mp3")
    playsound("my.mp3")
        
   # elif "what's your name" or "what is your name" in cammand1:
def two():
    n=open("name.txt","rt")
    name=n.read()
    result= 'my name is'+name
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    print(speech)
    speech.save('my.mp3')
    playsound('my.mp3')
#    elif 'search'or'wikipedia':
def three():
    result=wikipedia.summary(cammand1,sentences=2)
    print(result)
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    speech.save('my.mp3')
    playsound('my.mp3')
    
def four():
    result= 'yes sir ,what is my new name'
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    print(speech)
    speech.save('my.mp3')
    playsound('my.mp3')
    result= hai()
    result=result.replace('your new name is ','')
    n=open("name.txt","w")
    name=n.write(result)
    n.close
    n=open("name.txt","r")
    name=n.read()
    n.close()
    result='my new name is'+name
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    print(speech)
    speech.save('my.mp3')
    playsound('my.mp3')
def five():
    result="This is one of things that we'd both have to agree on. I'd prefer to keep our relationship friendly. Romance makes me incredibly awkward"
    say(result)


ai()
while True:
    cammand1=hai()
    if 'who is agalya' in cammand1:
        one()
        continue
    if 'what is your name' in cammand1:
        two()
        continue
    if 'can you change your name' in cammand1:
        four()
        continue
    if 'can you marry me' in cammand1:
        five()
        continue
    if 'open' in cammand1:
        res=cammand1.replace("open ",'')
        res1=res
        if True:
            no.open(res1)
        saying(res)
        break
        
        result=result.replace('open','')
        print(result)
        no.open(result)
        break
    if 'search'or'wikipedia' in cammand1:
        three()
        continue
    
    
    
    
    
        
        