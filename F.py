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
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Friday import Ui_FRIDAY_UI

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
#     n = self.Take_Command().lower()
#     book = open(f'{n}.pdf', 'rb')
#     pdfReader = PyPDF2.PdfFileReader(book)
#     pages = pdfReader.numPages
#     speak(f'Total numbers of pages in this book {pages}')
#     speak('sir please enter the page number i have to read')
#     pg = int(input("Enter the page number : "))
#     page = pdfReader.getPage(pg)
#     text = page.extractText()
#     speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    # voice to text
    def Take_Command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            # audio = r.listen(source, timeout=1, phrase_time_limit=5)
            audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"user said : {query}")

        except Exception as e:
            speak('say that again please cant hear you')
            return 'none'
        return self.query

    def TaskExecution(self):
        # if __name__ == '__main__':
        wish()
        # Take_Command()
        # speak('hi i am friday sir')
        while True:
            self.query = self.Take_Command().lower()

            # logic building for task
            if "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")

            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")

            elif 'who am i' in self.query:
                speak("you are admin and creator")

            elif 'who are you' in self.query:
                speak("I am friday your own Ai")

            elif 'open notepad' in self.query:
                path = "C:\\Program Files\\WindowsApps\Microsoft.WindowsNotepad_11.2306.15.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
                os.startfile(path)

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, The time right now is {strTime}")

            elif 'open vmware' in self.query:
                speak("setting up your hacking setup ")
                path = "C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe"
                os.startfile(path)

            elif 'open code' in self.query:
                speak("opening vs code for you sir")
                path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif 'close notepad' in self.query:
                speak('ok sir, closing notepad')
                os.system('taskkill /f /im notepad.exe')

            elif 'open cmd' in self.query:
                path = "%windir%\\system32\\cmd.exe"
                os.startfile(path)

            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:  # esc
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'play music' in self.query:
                music_dir = ""
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                # for song in songs:
                #     if song.endswith('.mp3'):
                #         os.startfile(os.path.join(music_dir, song))
                os.startfile(os.path.join(music_dir, rd))

            elif 'ipAddress' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif 'wikipedia' in self.query:
                speak('searching wikipedia...')
                self.query = self.query.replace('wikipedia', '')
                result = wikipedia.summary(self.query, sentences=2)
                speak('according to wikipedia')
                # print(result)

            elif 'open youtube' in self.query:
                speak('opening youtube for you sir...')
                webbrowser.open('youtube.com')

            elif 'open google' in self.query:
                speak('opening google for you sir...')
                speak('what should i search for you sir')
                cm = self.Take_Command().lower()
                webbrowser.open(f'{cm}')

            elif 'send message on whatsapp' in self.query:
                speak('what message should i send for you sir')
                m = self.Take_Command().lower()
                kit.sendwhatmsg('+918249608898', f'{m}', 2, 25)
                # time.sleep(120)
                speak('message has been send')

            elif 'play video' in self.query:
                speak('what video should i play for you sir')
                y = self.Take_Command().lower()
                kit.playonyt(f'{y}')
                speak('playing video for you...')

            # to send email
            elif 'email' in self.query:
                try:
                    speak('To whom do you want to send this email')
                    e = self.Take_Command().lower()
                    to = f'{e}'
                    speak('what should i say ?')
                    content = self.Take_Command().lower()
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
            elif 'where am i' in self.query or 'where we are' in self.query:
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
            elif 'open instagram' in self.query:
                speak("opening instagram for you sir")
                speak('sir please enter the user name correctly.')
                name = input("Enter username here : ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account ")
                condition = self.Take_Command().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. Now i am ready")
                else:
                    pass

            # To take a screenshot
            elif 'take screenshot' in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.Take_Command().lower()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. Now i am ready for next one")
            # To read pdf
            elif 'read pdf' in self.query:
                # pdf_reader()
                speak('which book do you want to read : ')
                n = input("Enter name of book : ")
                # n = self.Take_Command().lower()
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
                # pg = int(self.Take_Command().lower())
                page = pdfReader.getPage(pg)
                text = page.extractText()
                speak(text)

            # to hide files using os module
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.Take_Command().lower()
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
            # elif 'hide all files' in self.query or 'hide this folder' in self.query or 'visible for everyone' in self.query:
            #     speak('sir please tell me you want to hide this folder or make it visible for everyone')
            #     condition = self.Take_Command().lower()
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

            # elif 'do some calculation' in self.query:

            # set alarm
            elif 'set alarm' in self.query:
                nm = int(datetime.datetime.now().hour)
                if nm == 22:
                    music_dir = ''
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'switch the window' in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')

            elif 'tell me news' in self.query:
                speak('please wait sir, fetching the latest news')
                news()

            # system calls
            elif 'shutdown the system' in self.query:
                os.system('shutdown /r /t 5')

            elif 'restart the system' in self.query:
                os.system('shutdown /r /t 5')

            elif 'sleep the system' in self.query:
                os.system('rundll32.exe powrprof.dll, SetSuspendState 0,1,1')

            elif 'no thanks' in self.query:
                speak('thanks for using me sir have a good day')
                sys.exit()

            # speak('sir, do you have any other work for me...')


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FRIDAY_UI()
        # gui pop up
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)

    def startTask(self):
        # for running gui
        self.ui.movie = QtGui.QMovie(
            "../Mycodes/BOOKS/PYTHON_MODULES/High_resolution_wallpaper_background_ID_77701852354.webp")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        curr_time = QTime.currentTime()
        curr_date = QDate.currentDate()
        now = QDate.currentDate()
        label_time = curr_time.toString('hh:mm:ss')
        label_date = curr_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser.setText(label_time)


app = QApplication(sys.argv)
f = Main()
f.show()
exit(app.exec_())