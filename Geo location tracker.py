import requests
import json 
from win32com.client import Dispatch
import gmplot
import webbrowser 
import os


def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


res=requests.get('https://ipinfo.io/')
data=res.json()

location=data['loc'].split(",")

latitude=location[0]

longitude=location[1]

country=data['country']
city=data['city']

print("Latitude: {}".format(latitude))
speak("Latitude: {}".format(latitude))

print("Longitude: {}".format(longitude))
speak("Longitude: {}".format(longitude))

print("Country: {}".format(country))
speak("Country: {}".format(country))

print("City: {}".format(city))
speak("City: {}".format(city))

gmap=gmplot.GoogleMapPlotter(latitude,longitude,15)

gmap.draw("GoogleMap.html")

speak("GoogleMap html file is created")

path=os.path.abspath('GoogleMap.html')

url='file://'+path

webbrowser.open(url) 

speak("In Opening webbrowser....")