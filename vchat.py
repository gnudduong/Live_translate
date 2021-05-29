# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:50:00 2021

@author: slims
"""

# voicechat

import speech_recognition as sr
from googletrans import Translator
from tkinter import *

# from PIL import ImageTk,Image


p = Translator() 
r =sr.Recognizer()


"""UI"""
root = Tk()
root.title('Voice chat')
root.geometry('400x200')

lang={
  "Afrikaans": [
    ["South Africa", "af-ZA"]
  ],
  "Arabic" : [
    ["Algeria","ar-DZ"],
    ["Bahrain","ar-BH"],
    ["Egypt","ar-EG"],
    ["Israel","ar-IL"],
    ["Iraq","ar-IQ"],
    ["Jordan","ar-JO"],
    ["Kuwait","ar-KW"],
    ["Lebanon","ar-LB"],
    ["Morocco","ar-MA"],
    ["Oman","ar-OM"],
    ["Palestinian Territory","ar-PS"],
    ["Qatar","ar-QA"],
    ["Saudi Arabia","ar-SA"],
    ["Tunisia","ar-TN"],
    ["UAE","ar-AE"]
  ],
  "Basque": [
    ["Spain", "eu-ES"]
  ],
  "Bulgarian": [
    ["Bulgaria", "bg-BG"]
  ],
  "Catalan": [
    ["Spain", "ca-ES"]
  ],
  "Chinese Mandarin": [
    ["China (Simp.)", "cmn-Hans-CN"]
  ],
  "Chinese Cantonese": [
    ["Hong Kong", "yue-Hant-HK"]
  ],
  "Croatian": [
    ["Croatia", "hr_HR"]
  ],
  "Czech": [
    ["Czech Republic", "cs-CZ"]
  ],
  "Danish": [
    ["Denmark", "da-DK"]
  ],
  "English": [

    ["United States", "en-US"]
  ],
  "Farsi": [
    ["Iran", "fa-IR"]
  ],
  "French": [
    ["France", "fr-FR"]
  ],
  "Filipino": [
    ["Philippines", "fil-PH"]
  ],
  "Galician": [
    ["Spain", "gl-ES"]
  ],
  "German": [
    ["Germany", "de-DE"]
  ],
  "Greek": [
    ["Greece", "el-GR"]
  ],
  "Finnish": [
    ["Finland", "fi-FI"]
  ],
  "Hebrew" :[
    ["Israel", "he-IL"]
  ],
  "Hindi": [
    ["India", "hi-IN"]
  ],
  "Hungarian": [
    ["Hungary", "hu-HU"]
  ],
  "Indonesian": [
    ["Indonesia", "id-ID"]
  ],
  "Icelandic": [
    ["Iceland", "is-IS"]
  ],
  "Italian": [
    ["Italy", "it-IT"]
  ],
  "Japanese": [
    ["Japan", "ja-JP"]
  ],
  "Korean": [
    ["Korea", "ko-KR"]
  ],
  "Lithuanian": [
    ["Lithuania", "lt-LT"]
  ],
  "Malaysian": [
    ["Malaysia", "ms-MY"]
  ],
  "Dutch": [
    ["Netherlands", "nl-NL"]
  ],
  "Norwegian": [
    ["Norway", "nb-NO"]
  ],
  "Polish": [
    ["Poland", "pl-PL"]
  ],
  "Portuguese": [
    ["Portugal", "pt-PT"]
  ],
  "Romanian": [
    ["Romania", "ro-RO"]
  ],
  "Russian": [
    ["Russia", "ru-RU"]
  ],
  "Serbian": [
    ["Serbia", "sr-RS"]
  ],
  "Slovak": [
    ["Slovakia", "sk-SK"]
  ],
  "Slovenian": [
    ["Slovenia", "sl-SI"]
  ],
  "Spanish": [
    ["Spain", "es-ES"]
  ],
  "Swedish": [
    ["Sweden", "sv-SE"]
  ],
  "Thai": [
    ["Thailand", "th-TH"]
  ],
  "Turkish": [
    ["Turkey", "tr-TR"]
  ],
  "Ukrainian": [
    ["Ukraine", "uk-UA"]
  ],
  "Vietnamese": [
    ["Viet Nam", "vi-VN"]
  ],
  "Zulu": [
    ["South Africa", "zu-ZA"]
  ]
}
mic_list=sr.Microphone.list_microphone_names()
i_source={}
for i,input in enumerate(mic_list):
    if input.startswith('Microsoft')==False:
        i_source[input]=i
    if input.startswith('Stereo'):
        break
#i_source={'Microphone':1,'PC':3}

LANGUAGES = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

lang_in=StringVar()
lang_in.set('English')
drop_1 = OptionMenu(root, lang_in, *lang)
drop_1.grid(row=1, column=0)

lang_label= Label(text='Input language:')
lang_label.grid(row=0,column=0)

lang_out=StringVar()
lang_out.set('english')
drop = OptionMenu(root, lang_out, *LANGUAGES)
drop.grid(row=1, column=1)

lang2_label= Label(text='Output language:')
lang2_label.grid(row=0,column=1)

mic_in=StringVar()
mic_in.set('Microphone')
drop_2 = OptionMenu(root, mic_in, *i_source)
drop_2.grid(row=1, column=2)

lang2_label= Label(text='Source:')
lang2_label.grid(row=0,column=2)


"""cc"""
def display(text):
    top=Toplevel()
    label =Label(top,text=text, font=('Times','30'), fg='black',bg='white',borderwidth=0)
    label.master.overrideredirect(True)
    ws = label.winfo_screenwidth() # width of the screen
    hs = label.winfo_screenheight() # height of the screen
    x=ws/2
    y=int(hs/10*9)
    label.master.geometry(('+%d+%d' % (x, y)))
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()
    label.after(1500, lambda: label.master.destroy()) # Destroy the widget after 30 seconds
    label.mainloop()

    
"""Start func"""    
def get_info():
    input_lang=lang[lang_in.get()][0][1]
    output_lang=LANGUAGES[lang_out.get()]
    input_source=i_source[mic_in.get()]
    print(input_lang,output_lang,input_source)

    trans(input_lang,output_lang,input_source)
def close():
    global gate
    gate= False
    root.destroy()






"""Recognition and translate"""
def trans(input_lang,output_lang,input_source):
    global gate
    gate=True

    while gate:

        
        with sr.Microphone(device_index=input_source) as source:
            print('Listening...')
            audio = r.listen(source,phrase_time_limit=5)
            try:
                text=r.recognize_google(audio,language=input_lang)
                # print(text)
                if text == 'stop listening':
                    gate= False
                else:    
                    k = p.translate(text, dest=output_lang)
                    # trans_label= Label(text=k.text)
                    # trans_label.grid(row=3,column=0,columnspan=2)
                    # print(k.text)
                    display(k.text)
            except:
                print('...')

start_butt=Button(root, text='Start',command=get_info)
start_butt.grid(row=2,column=0,columnspan=2)

close_butt=Button(root, text='Close',command=close)
close_butt.grid(row=2,column=1,columnspan=1)


root.mainloop()