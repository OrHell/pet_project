import moviepy.editor as mp
import shutil
import os
import pip
import threading

def music_convert(music):
    clip = mp.VideoFileClip(music+".mp4")
    clip.audio.write_audiofile(music+".mp3")


music =[]
folder = os.path.abspath(os.curdir)
for folder, subfolder, files in os.walk(folder):
    for file in files:
        if file.endswith(".mp4"):
            music.append(file)
iterat = 0
count = len(music)
music_format = []
for iterat in range(0, count):
    music_format.append(music[iterat])
    music_format[iterat].replace(' ','_')
    os.rename(music[iterat], music_format[iterat])
    music[iterat] = music_format[iterat][:-4]

    threading.Thread(target = music_convert, args = [music[iterat]]).start()
    #music_convert(music[iterat])
#print(timeit('music_convert(music[iterat])',globals = globals(),number =1))

