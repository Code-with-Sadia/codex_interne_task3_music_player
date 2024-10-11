from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
from pathlib import Path

volume_val = 0.5
global paused 
paused= False
playlist = []
c_song=""
mixer.init()

def add_song():
  global c_song
  window.directory = filedialog.askdirectory()
  for song in os.listdir(window.directory):
       name,ext = os.path.splitext(song)
       if ext == ".mp3" or ext ==".mpeg":
           playlist.append(song)
  
  for song in playlist:
        playbox.insert(END,song)
        
  playbox.selection_set(0)
  c_song = playlist[playbox.curselection()[0]]


def play_func():
    global c_song
    try:
      file=os.path.join(window.directory,c_song)
      mixer.music.load(file)
      print(c_song)
      mixer.music.play()
    except Exception as e:
        print(e)
            
def stop_func():
    try:
        mixer.music.stop()
    except Exception as e:
        print(e) 

def prev_func():
    global c_song
    try:
      playbox.select_clear(0,END)
      playbox.selection_set(playlist.index(c_song)-1)
      print(playlist.index(c_song))
      c_song= playlist[playbox.curselection()[0]]
    except Exception as e:
        print(e)

def next_func():
    global c_song
    try:
      playbox.select_clear(0,END)
      playbox.selection_set(playlist.index(c_song)+1)
      c_song= playlist[playbox.curselection()[0]]
      
    except Exception as e:
        print(e)

def inc_volume():
    try:
        global volume_val
        if volume_val >=5:
            return
        volume_val = volume_val + float(0.9)
        volume_val = round(volume_val,1)
        mixer.music.set_volume(volume_val)
        print(volume_val)
    except Exception as e:
        print(e)
        
def dec_volume():
    try:
        global volume_val
        if volume_val <=0:
            return
        volume_val = volume_val - float(0.1)
        volume_val = round(volume_val,1)
        mixer.music.set_volume(volume_val)
        print(volume_val)
    except Exception as e:
        print(e)

def pause_func(is_pause):
    global paused
    paused= is_pause
    try:
       if paused:
        mixer.music.unpause()
        paused=False
        Button(window,image=pause_symbol,bg="white",command=lambda: pause_func(paused)).grid(row=5,column=2,sticky="nsew")

       else:
        mixer.music.pause()
        paused=True
        Button(window,image=resume_symbol,bg="white",command=lambda: pause_func(paused)).grid(row=5,column=2,sticky="nsew")

    except Exception as e:
        print(e)



window = Tk()
window.title('Music Player')
window.configure(background="black")
window.iconbitmap("logo.ico")
window.geometry("630x360")
window.resizable(width=False, height=False)


Label(window, text="Audio Player", font=("Times new roman", 30, "bold"),bg="black", fg="Red").grid(row=0,columnspan=7,padx=170)
display_song_name = Label(window,font=("Times new roman", 10),bg="white",fg="green")
playbox= Listbox(window,width=100,bg="white",fg="red")
playbox.grid(row=1,columnspan=7,sticky="nsew",padx=10)

play_symbol = PhotoImage(file="play.png")
pause_symbol = PhotoImage(file="pause.png")
resume_symbol = PhotoImage(file="resume.png")
back_symbol = PhotoImage(file="previous.png")
forward_symbol = PhotoImage(file="forward.png")
stop_symbol = PhotoImage(file="stop.png")
vol_up_symbol = PhotoImage(file="inc_vol.png")
vol_down_symbol = PhotoImage(file="dec_vol.png")

Button(window,text="Search Song",command=add_song).grid(row=2,columnspan=7,pady=20)
Button(window,image=play_symbol,bg="white",command=play_func).grid(row=5,column=0,sticky="nsew")
Button(window,image=stop_symbol,bg="white",command=stop_func).grid(row=5,column=1,sticky="nsew")
Button(window,image=pause_symbol,bg="white",command=lambda: pause_func(paused)).grid(row=5,column=2,sticky="nsew")
Button(window,image=back_symbol,bg="white",command=prev_func).grid(row=5,column=3,sticky="nsew")
Button(window,image=forward_symbol,bg="white",command=next_func).grid(row=5,column=4,sticky="nsew")
Button(window,image=vol_up_symbol,bg="white",command=inc_volume).grid(row=5,column=5,sticky="nsew")
Button(window,image=vol_down_symbol,bg="white",command=dec_volume).grid(row=5,column=6,sticky="nsew")


window.mainloop()