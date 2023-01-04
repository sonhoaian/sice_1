import time
import os
import random, string
import webbrowser, platform

#chrome_exe = "chrome.exe "
default_text = "checkine kite"
google_search = ["https://www.google.com/search?q=", 
" https://www.bing.com/search?q=", " https://vn.search.yahoo.com/search?p=",
" https://yandex.com/search/?text=", " https://coccoc.com/search?query="]

#strg = a.split()
#print(type(strg))
length = 8
platform = platform.platform()

if ("linux" in platform) | ("Linux" in platform):
    chrome_exe = "google-chrome-unstable"
    taskkill = "pkill -x "+chrome_exe
else:
    chrome_exe = "chrome.exe "
    taskkill = "taskkill /F /IM  chrome.exe"

os.system(taskkill)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = result_str +" "+''.join(random.choice(string.digits) for i in range(length))
    return result_str

counta = 0
for i in range(1,100000000):
    if counta%20 == 0:        
        os.system(taskkill)    
    google_URL = google_search[i%5] + str(get_random_string(length))
    print(google_URL);
    webbrowser.register(chrome_exe,
	None,
	webbrowser.BackgroundBrowser(chrome_exe))
    webbrowser.get(chrome_exe).open(google_URL)    
    time.sleep(45)
    counta+=1
    
os.system(taskkill)

###########






