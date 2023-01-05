import time
import os
import random, string
import webbrowser, platform

file = open("text.txt","r")
#chrome_exe = "chrome.exe "
strg = str(file.read())
file.close()

strg_list=strg.split()


#strg = a.split()
#print(type(strg))
length = 8
platform = platform.platform()

if ("linux" in platform) | ("Linux" in platform):
    chrome_exe = "google-chrome-unstable"
    taskkill = "pkill -x chrome"
else:
    chrome_exe = "chrome.exe "
    taskkill = "taskkill /F /IM  chrome.exe"

os.system(taskkill)

counta = 0
for i in range(1,len(strg_list)):
    if counta%20 == 0:        
        os.system(taskkill)  
    rand = random.randint(0, i) 
    google_URL = strg_list[rand]
    strg_list.pop(rand)
    print(google_URL);
    webbrowser.register(chrome_exe,
	None,
	webbrowser.BackgroundBrowser(chrome_exe))
    webbrowser.get(chrome_exe).open(google_URL)    
    time.sleep(80)
    counta+=1
    print(counta)
    
os.system(taskkill)

###########







