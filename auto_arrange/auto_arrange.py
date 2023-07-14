import imp
import os
import shutil
import pywintypes
from time import sleep
from win10toast import ToastNotifier

toast = ToastNotifier()

sleep(3)
path = 'C:/Users/USER/Downloads'
toast.show_toast("Auto arranger app","The App has started ", duration=20)
os.chdir("H:/Codes/python projects/auto_arrnge")


#guides
#music .mp3 .webm
music = ['.mp3']
#images .jpg .png
img = ['.jpg','.png','jfif']
#vids .mp4
vids = ['.mp4','.webm']
#docs .pdf .doc .txt .pptx .html .ics
docs = ['.pdf', '.doc' ,'.txt', '.pptx', '.html' ,'.ics']
#zips .zip .rar .iso
zips = ['.zip','.rar', '.iso']
#incomplete .crdownload
incomplete = ['.crdownload']
#executables .exe 
exe = ['.exe']
#themes .deskthemepack
themes = ['.deskthemepack']



for f in os.listdir(path):
    f_name, f_ext = os.path.splitext(f)
    #print(f_name + " " + f_ext)

    #docs
    if f_ext in docs:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/docs')
    elif f_ext in exe:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/executables')
    elif f_ext in img:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/images')
    elif f_ext in incomplete:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/incomplete')
    elif f_ext in music:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/music')
    elif f_ext in zips:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/zips')
    elif f_ext in vids:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/videos')
    elif f_ext in themes:
        shutil.move('C:/Users/USER/Downloads/' + f, 'C:/Users/USER/Downloads/themes')
    