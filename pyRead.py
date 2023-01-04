import time
import os
import random
import webbrowser, platform

file = open("text.txt", "r")
#os.system("cmd.exe taskkill /F /IM chrome.exe")
strg = str(file.read())
file.close()
#chrome_exe = "chrome.exe "
default_text = "checkine kite"
google_search = ["https://www.google.com/search?q=", 
" https://www.bing.com/search?q=", " https://vn.search.yahoo.com/search?p=",
" https://yandex.com/search/?text=", " https://coccoc.com/search?query="]

#strg = a.split()
#print(type(strg))
strg_len = 251
#random seed


platform = platform.platform()

if ("linux" in platform) | ("Linux" in platform):
    chrome_exe = "google-chrome-unstable"
    taskkill = "pkill -x "+chrome_exe
else:
    chrome_exe = "chrome.exe "
    taskkill = "taskkill /F /IM  chrome.exe"

os.system(taskkill)
counta = 0
for i in range(1,strg_len):
    if counta%20 == 0:        
        os.system(taskkill)
    seed = (int) (time.time() % strg_len)
    while seed-1 == 0 | seed - 1 == -1:
        time.sleep(time.time() % 11)	
        seed = (int) (time.time() % strg_len)
    print(seed)
    rand =  random.randint(0, seed-1)
    print(rand)
    google_URL = google_search[i%5] + strg[0:rand] + " " +default_text
    print(google_URL);
    webbrowser.register(chrome_exe,
	None,
	webbrowser.BackgroundBrowser(chrome_exe))
    webbrowser.get(chrome_exe).open(google_URL)    
    time.sleep(45)
    counta+=1
os.system(taskkill)
