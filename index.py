import pyttsx3
import customtkinter
import pyjokes
# import speech_recognition as sr
# from PIL import Image, ImageTK
import tkinter as tk
from tkinter import *
from pytube import YouTube
from googlesearch import search
# import webbrowser
# from tkhtmlview import HTMLLabel
from win10toast import ToastNotifier
import time


#Initialize sab modules here
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 140) 
toaster = ToastNotifier()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()
root.geometry("720x480")

#functionalities UwU
def intro():
    namee = e.get()
    engine.say("Hello" + namee + "! I am Luna, your personal assistant!")
    engine.runAndWait()

def jokies():
    jokieee = pyjokes.get_joke(language = 'en', category = 'neutral')
    print(jokieee)
    e.delete(0, END)
    e.insert(0, jokieee)
    engine.say(jokieee)
    engine.runAndWait()

def startDownload():
    try:
        ytLink = e.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        name.configure(text = ytObject.title)
        video.download()
        e.delete(0, END)
        e.insert(0, 'Download Complete!')
        engine.say('Download complete!')
        engine.runAndWait()
    except:
        e.delete(0, END)
        e.insert(0, 'Invalid Link buddy')
        engine.say('Invalid Link buddy')
        engine.runAndWait()


# def on_progress(stream, chunk, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage = bytes_downloaded / total_size * 100
#     print (percentage)
#     per = str(int(percentage))
#     pPercentage.configure(text = per + '%')
#     pPercentage.update





def GSearch():
    search_query = e.get()
    e.delete(0, END)
    for i in search(search_query,
        tld="co.in",
        lang="en", 
        num=1, 
        stop=1,
        pause=2.0):
        linkk = i
        print(i)
        e.insert(0, i)
    engine.say('Here are your search results')
    engine.runAndWait()
    # tag = '<a href ="' + linkk + '">SEARCH RESULTS</a>'
    # tag2 = "'" + tag + "'"
    # link = HTMLLabel(root, html = tag2)
    # link.pack()

def clear():
    e.delete(0, END)
    name.pack()
    e.pack()    
    rem.delete(0, END)
    mesg.delete(0, END)
    timer.delete(0, END)
    clr.forget()
    rem.forget()
    mesg.forget()
    lesgo.forget()
    timer.forget()
    button_1.pack(pady = 10, padx = 20)
    button_2.pack(pady = 10, padx = 20)
    button_3.pack(pady = 10, padx = 20)
    button_4.pack(pady = 10, padx = 20)
    button_5.pack(pady = 10, padx = 20)
    clr.pack(pady = 10, padx = 20)
    # pPercentage.forget()
    # progressBar.forget()

def new_interface():
    button_1.forget()
    button_2.forget()
    button_3.forget()
    button_4.forget()
    button_5.forget()
    e.forget()
    clr.forget()
    name.forget()
    rem.pack(pady = 10, padx = 30)
    rem.insert(0, 'Enter a title')
    mesg.pack(pady = 10, padx = 30)
    mesg.insert(0, 'Enter a message')
    timer.pack(pady = 10, padx = 30)
    timer.insert(0, 'Enter time duration in minutes')
    lesgo.pack(pady = 10, padx = 20)
    # Success.pack(padx = 20, pady = 10)
    clr.pack(pady = 10, padx = 20)

def reminder():
    Toasttitle = rem.get()
    msg = mesg.get()
    minutes = float(timer.get())
    min = str(minutes)
    seconds = minutes * 60
    # Success.configure(text = "Remainder set suceesfully")
    print("Reminder set successfully")
    engine.say('Reminder to' + msg + 'in' + min + 'minutes has been set successfully')
    engine.runAndWait()
    time.sleep(seconds)
    toaster.show_toast(Toasttitle, msg, duration=10, threaded=True)

    while toaster.notification_active:
        time.sleep(0.1)



###

root.title("LUNA!(. ❛ ᴗ ❛.)")

#Defining images idk why T__T
#STUPID PIL DOESN'T WORK. WHAT DID I DO TO DESERVE THIS BC

intropew = customtkinter.CTkLabel(root, text = "****************************************************************************************")
intropew.pack()

name = customtkinter.CTkLabel(root, text="Enter your name:")
name.pack()

e = customtkinter.CTkEntry(root, width = 600, height= 30)
e.pack(pady = 0, padx = 50)

# pPercentage = customtkinter.CTkLabel(root, text="0%")

# progressBar = customtkinter.CTkProgressBar(root, width = 300)
# progressBar.set(0)




button_1 = customtkinter.CTkButton(root, text = 'intro', command = intro)
button_1.pack(pady = 10, padx = 20)

button_3 = customtkinter.CTkButton(root, text = 'jokes', command = jokies)
button_3.pack(pady = 10, padx = 20)

button_2 = customtkinter.CTkButton(root, text = 'download', command = startDownload)
button_2.pack(pady = 10, padx = 20)

button_4 = customtkinter.CTkButton(root, text = 'google search', command = GSearch)
button_4.pack(pady = 10, padx = 20)

button_5 = customtkinter.CTkButton(root, text = 'Set a Reminder!!', command = new_interface)
button_5.pack(pady = 10, padx = 20)

clr = customtkinter.CTkButton(root, text ="clear", command = clear)
clr.pack(pady = 10, padx = 20)

rem = customtkinter.CTkEntry(root, width = 600, height= 30)

mesg = customtkinter.CTkEntry(root, width = 600, height= 30)

timer = customtkinter.CTkEntry(root, width = 600, height= 30)

lesgo = customtkinter.CTkButton(root, text='lessgoooo', command=reminder)


root.mainloop()


# yt link for download demonstration
# https://www.youtube.com/watch?v=d95PPykB2vE