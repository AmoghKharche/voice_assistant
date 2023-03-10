from tracemalloc import stop
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import os
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
 
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
 
    else:
        speak("Good Evening!")  
 
    speak("I am Ultron. Please tell me how may I help you?")       
 
def takeCommand():
    #It takes microphone input from the user and returns string output
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        time.sleep(1)
        
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
 
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aditya5092008@gmail.com', 'superrock509')
    server.sendmail('aditya5092008@gmail.com', to, content)
    server.close()
 
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
 
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'youtube' in query: 
            opt = Options()
            driver = webdriver.Chrome(options=opt, executable_path=r"G:\Chrome Downloads\chromedriver.exe")
            opt.add_argument("--disable-infobars")
            opt.add_argument("start-maximized")
            opt.add_argument("--disable-extensions")
            opt.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver.get('https://www.youtube.com/')
            time.sleep(0.5)
            speak('what would u like to watch')
            input_search1=takeCommand()
            driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(str(input_search1))
            driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon').click()
        elif 'close browser' in query:
            os.system('TASKKILL /F /IM chrome.exe')  
 
        elif 'search' in query:
            opt = Options()
            driver = webdriver.Chrome(options=opt, executable_path=r"G:\Chrome Downloads\chromedriver.exe")
            opt.add_argument("--disable-infobars")
            opt.add_argument("start-maximized")
            opt.add_argument("--disable-extensions")
            opt.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver.get('https://www.google.com/')
            time.sleep(0.5)
            speak('what would u like to search')
            input_search=takeCommand()
            driver.find_element_by_css_selector('input.gLFyf.gsfi').send_keys(str(input_search))
            driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
        elif 'close browser' in query:
                 os.system('TASKKILL /F /IM chrome.exe')  
 
        elif 'open stack overflow' in query:
            opt = Options()
            driver = webdriver.Chrome(options=opt, executable_path=r"G:\Chrome Downloads\chromedriver.exe")
            driver.get('https://stackoverflow.com/')
        elif 'close browser' in query:
            os.system('TASKKILL /F /IM chrome.exe')  
 
 
        elif 'play music' in query:
            music_dir = 'G:\Chrome Downloads\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'close song' in query:
            os.system('TASKKILL /F /IM vlc.exe')
            
 
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
 
        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%m/%d/%Y")    
            speak(f"Sir, the Date is {strDate}")
 
        elif 'open code' in query:
            codePath = "C:\\Users\\Amogh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            if 'close code' in query:
                 os.system('TASKKILL /F /IM Code.exe')
       
                 
                 
        elif 'game' in query:
            GamePath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(GamePath)
            if 'close game' in query:
             os.system('TASKKILL /F /IM RiotClientServices.exe')  
            
              
        elif 'spotify' in query:
            SpotifyPath = "C:\\Users\\Amogh\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(SpotifyPath)
            if 'close spotify' in query:
                 os.system('TASKKILL /F /IM Spotify.exe')
 
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sagediff2@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")  
 
        elif 'bye' in query:
            speak('see you later')
            quit()