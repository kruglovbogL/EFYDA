import pyttsx3                                    # converts text to speech
import datetime                                   # required to resolve any query regarding date and time
import speech_recognition as sr                   # required to return a string output by taking microphone input from the user
import wikipedia                                  # required to resolve any query regarding wikipedia
import os.path                                    # required to fetch the contents from the specified folder/directory
import browsers                                   
#import smtplib                                    # required to work with queries regarding e-mail
import winsound
from random import randint
import parselmouth
from IPython.display import Audio
import numpy as np
import matplotlib.pyplot as plt
from parselmouth.praat import call





#winsound.Beep(1010, 110)

engine = pyttsx3.init()
rate = engine.getProperty('rate') #Скорость произношения
engine.setProperty('rate', rate-1)

volume = engine.getProperty('volume') #Громкость голоса
engine.setProperty('volume', volume+0.9)



voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\VE_Russian_Milena_22kHz"

engine.setProperty('voice', voice_id)

voices = engine.getProperty('voices')


#----------------------------

#browsers.launch("brave", url="https://www.youtube.com/")

def speak(audio):                                # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()                          # without this command, the assistant won't be audible to us


def wishme():                                    # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine.save_to_file("Доброе утро", "sound.wav")                                            #--------------------morning
        engine.runAndWait()
        get_pich()

    elif hour>12 and hour<18:
        engine.save_to_file("Приятного аппетита!! семпай", "sound.wav") #--------------------------------lunch
        engine.runAndWait()
        get_pich()
        

    else:
        engine.save_to_file("Добрый вечер!", "sound.wav")
        engine.runAndWait()
        get_pich()


    engine.save_to_file("Привет Хозяин! Я Эфида, твой помощник пожалуйста скажи мне чем тебе помочь....", "sound.wav") #-----------------------hello
    engine.runAndWait()
    get_pich()


def get_pich():
    # Plot nice figures using Python's "standard" matplotlib library
    morning = "D:\EFYDA\sound.wav"
    snd = parselmouth.Sound(morning)
    # If desired, pre-emphasize the sound fragment before calculating the spectrogram
    pre_emphasized_snd = snd.copy()
    pre_emphasized_snd.pre_emphasize()

    Audio(data=snd.values, rate=snd.sampling_frequency)
    manipulation = call(snd, "To Manipulation", 0.01, 75, 800)   #0.01 75 600
    pitch_tier = call(manipulation, "Extract pitch tier")
    call(pitch_tier, "Multiply frequencies", snd.xmin, snd.xmax, 1.12)  #2 it number pitch 
    call([pitch_tier, manipulation], "Replace pitch tier")
    sound_octave_up = call(manipulation, "Get resynthesis (overlap-add)")
    type(sound_octave_up)
    Audio(data=sound_octave_up.values, rate=sound_octave_up.sampling_frequency)
    sound_octave_up.save("4_b_octave_up.wav", "WAV")
    up_sound = "4_b_octave_up.wav"
    winsound.PlaySound(up_sound, winsound.SND_FILENAME)




def takecommand():                               # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        a = randint(1, 4)
        if a == 2:
            engine.save_to_file("Так. чегоо?", "sound.wav") #-----------------------microphone
            engine.runAndWait()
            get_pich()
            r.pause_threshold = 2
            audio = r.listen(source)
        if a == 3:
            engine.save_to_file("чегоо?", "sound.wav") #-----------------------microphone
            engine.runAndWait()
            get_pich()
            r.pause_threshold = 2
            audio = r.listen(source)
        if a == 1:
            engine.save_to_file("Пытаюсь услышать...", "sound.wav") #-----------------------microphone
            engine.runAndWait()
            get_pich()
            r.pause_threshold = 2
            audio = r.listen(source)
        if a == 4:
            engine.save_to_file("говори внятнее бака!", "sound.wav") #-----------------------microphone
            engine.runAndWait()
            get_pich()
            r.pause_threshold = 2
            audio = r.listen(source)

    try:
        b = randint(1, 5)
        if b == 1:
            engine.save_to_file("Чтоб сказать то тебе...", "sound.wav") #-----------------------what???
            engine.runAndWait()
            get_pich()
            query = r.recognize_google(audio,language = 'ru')  # using google for voice recognition
            engine.save_to_file(f"Ты сказал: {query}\n", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich

        if b == 4:
            engine.save_to_file("ня..", "sound.wav") #-----------------------what???
            engine.runAndWait()
            get_pich()
            query = r.recognize_google(audio,language = 'ru')  # using google for voice recognition
            engine.save_to_file(f"вроде ты сказал: {query}\n", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
        if b == 2:
            engine.save_to_file("чтоб ответить...", "sound.wav") #-----------------------what???
            engine.runAndWait()
            get_pich()
            query = r.recognize_google(audio,language = 'ru')  # using google for voice recognition
            engine.save_to_file(f"Ты сказал: {query}\n", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
        if b == 3:
            engine.save_to_file("м? что??", "sound.wav") #-----------------------what???
            engine.runAndWait()
            get_pich()
            query = r.recognize_google(audio,language = 'ru')  # using google for voice recognition
            engine.save_to_file(f"Ты сказал: {query}\n", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
        if b == 5:
            engine.save_to_file("ну поговори со мною!!", "sound.wav") #-----------------------what???
            engine.runAndWait()
            get_pich()
            query = r.recognize_google(audio,language = 'ru')  # using google for voice recognition
            engine.save_to_file(f"Ты сказал: {query}\n", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()

    except Exception as e :
                
        engine.save_to_file("Еще раз? чтоо", "sound.wav")    # 'say that again' will be printed in case of improper voice
        engine.runAndWait()
        get_pich()
        return 'None' 
    return query

#def sendemail(to,content):                       # function to send email
 #   server = smtplib.SMTP('smtp.gmail.com',587)
 #   server.ehlo()
 #   server.starttls()
 #   server.login('senders_eamil@gmail.com','senders_password')
 #   server.sendmail('senders_email@gmail.com',to,content)
 #   server.close()


if __name__ == '__main__' :                      # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        # The whole logic for execution of tasks based on user asked query

        if 'википедия' in query :
            engine.save_to_file("Ищу в википедии", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            query = query.replace(f'wikipedia','')
            results = wikipedia.summary(query, sentences = 5)
            print(results)
            engine.save_to_file(results, "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()

        elif 'youtube' in query :
            engine.save_to_file("слушаюсь хозяин!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            browsers.launch("brave", url="https://www.youtube.com/")

        elif 'google' in query :
            engine.save_to_file("опять!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            browsers.launch("brave", url="https://www.google.com/")

        elif 'музыка' in query :
            engine.save_to_file("хорошо семпай!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            #music_dir = 'music_dir_of_the_user'
            #songs = os.listdir(music_dir)
            #os.startfile(os.path.join(music_dir,songs[0]))
            browsers.launch("brave", url="https://www.vk.com/audios643683559/")


        elif 'время' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            engine.save_to_file(f"Время сейчас {strtime}", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            
        elif 'хабр' in query:
            engine.save_to_file("Не забывай обо мне!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            browsers.launch("brave", url="https://www.habr.com/")
            
        elif 'браузер' in query:
            engine.save_to_file("Не забывай обо мне!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            browsers.launch("brave", url="https://www.vk.com/")

        elif 'открой stack overflow' in query :
            engine.save_to_file("Снова не знаешь как кодить???", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            browsers.launch("brave", url="https://www.hstackoverflow.com/")

        elif 'open free code camp' in query :
            engine.save_to_file("Это насколько ты отчаялся что смог сюда достучаться???", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            browsers.launch("brave", url="https://www.freecodecamp.org/")

        elif 'кодинг' in query :
            engine.save_to_file("Я помогу", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            codepath = 'D:\Microsoft Visual Studio\Common7\IDE/devenv.exe'
            os.startfile(codepath)

        #elif 'email' in query :
            #try:
              #  content = takecommand()
              #  to = 'reciever_email@gmail.com'
             #   sendemail(to, content)
             #   
          #  except Exception as e:
          #      print(e)
          #      speak('Sorry, I am not able to send this email')

#------------------------------------------------------------------------------exit that program----------------------------------------------------------------------------

        elif 'exit' in query:
            engine.save_to_file("What? Ok, bue", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            quit()
        
        elif 'выход' in query:
            engine.save_to_file("Пока, пока!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            quit()
        
        elif 'пока' in query:
            engine.save_to_file("Хорошо я приду тогда когда ты попросишь", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            quit()
            
        elif 'хватит' in query:
            engine.save_to_file("Ну и ладно!", "sound.wav") #-----------------------recognize
            engine.runAndWait()
            get_pich()
            quit()