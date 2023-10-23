from gtts import gTTS
from playsound import playsound
import wikipedia
import speech_recognition as sr
import os
import openai
import webbrowser
import pywhatkit as youtube



key='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'
openai.api_key=key
#user=b.hai()
n=open('name.txt','r')
name=n.read()
n.close()





messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]


language='en-in'
def hai():
    r = sr.Recognizer()
    r.energy_threshold=4000
    with sr.Microphone() as source:                
        print("listenning...")
        audio = r.listen(source)
        try:
            cammand = r.recognize_google(audio,language=language)
            cammand = cammand.lower()
            print(cammand)
        except LookupError:
            print("Could not understand your voice")
        except sr.exceptions.UnknownValueError:
            print("Could not understand your voice")
        except UnboundLocalError:
            print("Could not understand your voice")
    return cammand

def ai():
    n=open("name.txt","rt")
    name=n.read()
    n.close()
    j="hai i'm "+name+". your personal voice  assistant. "+name+" is now online.which help would you want sir! "
    speech = gTTS(text=j,lang=language,slow=False,tld="com.au")

    speech.save("no.mp3")
    playsound("no.mp3")

    
def chatgpt_in(result):
    message = result
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
      
    reply = chat.choices[0].message.content 
    print(f"{name}: {reply}") 
    messages.append({"role": "assistant", "content": reply})

def say(result):
    print(result)
    speech = gTTS(text=result,lang=language,slow=False,tld="com.au")
    speech.save('my.mp3')
    playsound('my.mp3')  
def playing(result):
    result="playing "+result+" on youtube"
    saying(result)
def saying(result):
    result=result
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
        result=res
        url='https://www.'+result+'.com'
        if 'google'  == result:
            webbrowser.open(url)
        elif  result == 'youtube':
            webbrowser.open(url)
        elif  result == 'facebook':
            webbrowser.open(url)
        elif  result == 'instragram' :
            webbrowser.open(url)
        elif  result == 'twitter' :
            webbrowser.open(url)
        elif 'whatsapp' == result:
            webbrowser.open('https://web.whatsapp.com/')
        elif 'organisation' in result:
            result=res.replace(' organisation','')
            site=result
            url1='https://www.'+site+'.org'
            webbrowser.open(url1)
        elif 'poki game' == result:
            webbrowser.open('https://www.poki.com')
        elif 'website' in result:
            result=res.replace(' website','')
            site=result
            url1='https://www.'+site+'.com'
            webbrowser.open(url1)
        
        
        result=res.replace(' ','')
        result1=result
        print(result1)
            
        os.popen(result1)
            
        if  ' ' in result:
            result=res.replace(' ','-')
            os.popen(result1)
        saying('openning '+result)
        break
    if 'search in google' in cammand1:
        result=cammand1.replace(' search in google','')
        url='https://www.google.com/search?q='+result
        webbrowser.open(url)
    if 'play on youtube' in cammand1:
        result=cammand1.replace(' play on youtube','')
        youtube.playonyt(result)
        playing(result)
        break
    if  'write'or 'chatgpt'in cammand1:
        cammand1=cammand1.replace(' chatgptpt','')
        result = cammand1
        chatgpt_in(result)
        continue
    if 'wikipedia' in cammand1:
        three()
        continue
    
    
    
    
    
        
        