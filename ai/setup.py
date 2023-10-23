import requests
import time
from playsound import playsound
def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        print("Error: No internet connection.")
        return False
    except requests.Timeout:
        print("Error: Request timed out. Please check your internet connection.")
        return False
    except requests.RequestException:
        print("Error: Unable to establish a connection. Please check your internet connection.")
        return False

def inte ():
    n=0
    a=True
    while a:
        
        if check_internet_connection():
            print("Internet connection is active. Performing actions...")
            

            if n==0:
                    import ai
                    ai.inter()
                        
                    
            if n==1:
                    import ai
                    ai.bo()
                    ai.inter()
        elif n==0:
            playsound('internet_except.mp3')
            n=1
        
        else:
            a=True
            time.sleep(5)
    
inte()    
