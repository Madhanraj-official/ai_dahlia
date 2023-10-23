import os

def open(result):
    
    
    result1=result.replace(' ','-')
    print(result1)
    os.popen(result1)
    if ' ' in result:
        print(result1)
        result1=result.replace(' ','')
        os.popen(result1)

