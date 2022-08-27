from tkinter import*
from tkinter import ttk, filedialog
import os
from pygame import mixer


def open_folder():
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END,song)


def play_song():
        mixer.music.load(play_list.get(ACTIVE))
        mixer.music.play()


def set_vol(val):
        mixer.music.set_volume(float(val)/100)


root = Tk()
mixer.init()
root.geometry("400x200")
root.resizable(0,0)
root.config(bg="white")
s = ttk.Style(root)
s.theme_use('vista')


#adding button....

ttk.Button(root,text='Play',width=10,command=play_song).place(x=10,y=10)
ttk.Button(root,text='Stop',width=10,command=mixer.music.stop).place(x=10,y=40)
ttk.Button(root,text='Pause',width=10,command=mixer.music.pause).place(x=10,y=70)
ttk.Button(root,text='UnPause',width=10,command=mixer.music.unpause).place(x=10,y=100)
ttk.Button(root,text='Open',width=10,command=open_folder).place(x=10,y=130)


music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=90,y=10,width=300,height=150)


scroll_y = ttk.Scrollbar(music_frame)
play_list = Listbox(music_frame,width=49,yscrollcommand=scroll_y.set)
scroll_y.config(command=play_list.yview)
scroll_y.pack(side=RIGHT,fill=Y)
play_list.pack(side=LEFT,fill=BOTH)


#volume..
vol = ttk.Scale(root,from_=0,to_=100,length=180,command=set_vol)
vol.set(50)
vol.place(x=130,y=165)


root.mainloop()