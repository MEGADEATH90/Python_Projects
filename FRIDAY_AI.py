import smtplib
import sys
import time
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
from instaloader import instaloader
from requests import get
import webbrowser
import pywhatkit as kit
import secure_smtplib
import pyjokes
import PyPDF2
import subprocess

# text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)  # 180-200


# print(voices[1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# wish me
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 & hour <= 12:
        speak('good morning')
    elif hour >= 12 & hour < 18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('hi i am friday sir. please tell how may i help you.')


# voice to text
def Take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        speak('say that again please cant hear you')
        return 'none'
    return query


# to send email
def sendEmail(t, c):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kaibalyapreetambalrj@gmail.com', 'your password')
    server.sendmail('kaibalyapreetambalrj@gmail.com', t, c)
    server.close()


# news
def news():
    # 78ba0dd85c3844838ed3ca982748fced
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=78ba0dd85c3844838ed3ca982748fced'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page['articles']
    # print(articles)
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


# def pdf_reader():
#     # n = input("Enter name of book : ")
#     speak('which book do you want to read : ')
#     n = Take_Command().lower()
#     book = open(f'{n}.pdf', 'rb')
#     pdfReader = PyPDF2.PdfFileReader(book)
#     pages = pdfReader.numPages
#     speak(f'Total numbers of pages in this book {pages}')
#     speak('sir please enter the page number i have to read')
#     pg = int(input("Enter the page number : "))
#     page = pdfReader.getPage(pg)
#     text = page.extractText()
#     speak(text)


if __name__ == '__main__':
    wish()
    # Take_Command()
    # speak('hi i am friday sir')
    while True:
        query = Take_Command().lower()

        # logic building for task
        if 'open notepad' in query:
            path = "C:\\Program Files\\WindowsApps\Microsoft.WindowsNotepad_11.2306.15.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(path)

        elif 'close notepad' in query:
            speak('ok sir, closing notepad')
            os.system('taskkill /f /im notepad.exe')

        elif 'open cmd' in query:
            path = "%windir%\\system32\\cmd.exe"
            os.startfile(path)

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:  # esc
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'play music' in query:
            music_dir = ""
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            # for song in songs:
            #     if song.endswith('.mp3'):
            #         os.startfile(os.path.join(music_dir, song))
            os.startfile(os.path.join(music_dir, rd))

        elif 'ipAddress' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            # print(result)

        elif 'open youtube' in query:
            speak('opening youtube for you sir...')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('opening google for you sir...')
            speak('what should i search for you sir')
            cm = Take_Command().lower()
            webbrowser.open(f'{cm}')

        elif 'send message on whatsapp' in query:
            speak('what message should i send for you sir')
            m = Take_Command().lower()
            kit.sendwhatmsg('+918249608898', f'{m}', 2, 25)
            # time.sleep(120)
            speak('message has been send')

        elif 'play video' in query:
            speak('what video should i play for you sir')
            y = Take_Command().lower()
            kit.playonyt(f'{y}')
            speak('playing video for you...')

        # to send email
        elif 'email' in query:
            try:
                speak('To whom do you want to send this email')
                e = Take_Command().lower()
                to = f'{e}'
                speak('what should i say ?')
                content = Take_Command().lower()
                speak('sir do you want to attach any file to this email')
                yn = input('(y/n) : ')
                if yn == 'y':
                    speak('sir please enter the correct path of the file into the shell')
                    file_loc = input("please enter the path here : ")
                else:
                    speak('sending email, please wait...')
                    sendEmail(to, content)
                    speak(f'Email has been sent to {e}')
            except Exception as e:
                print(e)
                speak('sorry sir, i am not able to send this email...')

        # To find location using ipAddress
        elif 'where am i' in query or 'where we are' in query:
            speak('wait sir, let me check')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'http://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f'sir i am not sure, but i think we are in {city} city of {state} state of {country} country')
            except Exception as e:
                speak('sorry sir, due to network issue i am unable to find our location')
                pass

        # To check the instagram profile
        elif 'open instagram' in query:
            speak("opening instagram for you sir")
            speak('sir please enter the user name correctly.')
            name = input("Enter username here : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account ")
            condition = Take_Command().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. Now i am ready")
            else:
                pass

        # To take a screenshot
        elif 'take screenshot' in query:
            speak("sir, please tell me the name for this screenshot file")
            name = Take_Command().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. Now i am ready for next one")

        # To read pdf
        elif 'read pdf' in query:
            # pdf_reader()
            speak('which book do you want to read : ')
            n = input("Enter name of book : ")
            # n = Take_Command().lower()
            book = open(f'{n}.pdf', 'rb')
            speak('sir please wait')
            pdfReader = PyPDF2.PdfFileReader(book)
            time.sleep(2)
            pages = pdfReader.numPages
            speak(f'Total numbers of pages in this book {pages}')
            time.sleep(1)
            speak('sir please tell the page number i have to read')
            time.sleep(1)
            pg = int(input("Enter the page number : "))
            # pg = int(Take_Command().lower())
            page = pdfReader.getPage(pg)
            text = page.extractText()
            speak(text)

        # to hide files using os module
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = Take_Command().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")  # os module
                speak("sir, all the files in this folder are now hidden.")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone. i wish you are taking this "
                      "decision in your own peace.")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")

        # using subprocess module
        # elif 'hide all files' in query or 'hide this folder' in query or 'visible for everyone' in query:
        #     speak('sir please tell me you want to hide this folder or make it visible for everyone')
        #     condition = Take_Command().lower()
        #
        #     if 'hide' in condition:
        #         try:
        #             subprocess.run(['attrib', '+h', '/s', '/d'], shell=True, check=True)
        #             speak('sir, all the files in this folder are now hidden.')
        #         except subprocess.CalledProcessError as e:
        #             print(f'Command failed with return code {e.returncode}')
        #
        #     elif 'visible' in condition:
        #         try:
        #             subprocess.run(["attrib", "-h", "/s", "/d"], shell=True, check=True)
        #             speak('sir, all the files in this folder are now visible to everyone. i wish you are taking this '
        #                   'decision in your own peace.')
        #         except subprocess.CalledProcessError as e:
        #             print(f'Command failed with return code {e.returncode}')
        #
        #     elif 'leave it' in condition or 'leave for now' in condition:
        #         speak('Ok sir')

        # elif 'do some calculation' in query:

        # set alarm
        elif 'set alarm' in query:
            nm = int(datetime.datetime.now().hour)
            if nm == 22:
                music_dir = ''
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'tell me news' in query:
            speak('please wait sir, fetching the latest news')
            news()

        # system calls
        elif 'shutdown the system' in query:
            os.system('shutdown /r /t 5')

        elif 'restart the system' in query:
            os.system('shutdown /r /t 5')

        elif 'sleep the system' in query:
            os.system('rundll32.exe powrprof.dll, SetSuspendState 0,1,1')

        elif 'no thanks' in query:
            speak('thanks for using me sir have a good day')
            sys.exit()

        speak('sir, do you have any other work for me...')
