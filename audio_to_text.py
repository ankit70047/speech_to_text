import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("search your query")
    print('speak now')
    audio = r3.listen(source)

    if 'edureka' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = 'https://www.edureka.co'
        with sr.Microphone() as source:
            print('search your query')
            audio = r2.listen(source)


            try:

                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:


                print('error')
            except  sr.RequestError as e:

                print('failed'.format(e))

    if 'video' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = 'https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            print('search for a video')
            audio = r2.listen(source)


            try:

                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:


                print('error')
            except  sr.RequestError as e:

                print('failed'.format(e))     


