import datetime as dt
import requests, json
import time
import datetime
import webbrowser
from requests_html import HTMLSession


s = HTMLSession()

def tempo():
        
    url = f'https://www.google.com/search?q=weather+s%C3%A3o+vicente'

    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})

    tempo = r.html.find('span#wob_dc', first=True).text 

    if tempo == "Chuva":
        print("Está chovendo")
    else:
        print("Tempo aberto")

def hora():
    
    tempo()

    local_time = datetime.datetime.now()
    localConvert = str(local_time)
    intConv = localConvert[11:13]
    dayTime = int(intConv)

    if dayTime >= 6 and dayTime < 12: #manhã
        webbrowser.open_new("https://www.youtube.com/watch?v=htgr3pvBr-I")
        print(dayTime)
    elif dayTime >= 6 and dayTime < 12 and tempo == "Chuva":
        webbrowser.open_new("https://www.youtube.com/watch?v=LBt60dfwEBY")
        print(dayTime)
    elif dayTime >= 12 and dayTime < 19: #tarde
        webbrowser.open_new("https://www.youtube.com/watch?v=mMfxI3r_LyA")
        print(dayTime)
    elif dayTime >= 12 and dayTime < 19 and tempo == "Chuva": 
        webbrowser.open_new("https://www.youtube.com/watch?v=lKBQ6UXJaQ0")
        print(dayTime)
    elif dayTime >= 19: #noite
        webbrowser.open_new("https://www.youtube.com/watch?v=ZiRuj2_czzw")
        print(dayTime)
    elif dayTime >= 19 and tempo == "Chuva":
        webbrowser.open_new("https://www.youtube.com/watch?v=Hx5ZlTyzU-k")
        print(dayTime)
    elif dayTime < 6: #madrugada
        webbrowser.open_new("https://www.youtube.com/watch?v=DaVLZptddm8")
        print(dayTime)
    elif dayTime < 6 and tempo == "Chuva":
        webbrowser.open_new("https://www.youtube.com/watch?v=NlwIDxCjL-8")    
        print(dayTime)

hora()


