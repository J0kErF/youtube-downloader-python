from pytube import YouTube
from colored import fg

dd=r"'download destination'"
f = open("links.txt", "r")
c=0
for link in f:
    try:
        print(fg('blue')+"Getting: "+link)
        yt = YouTube(link)
        print(fg('blue')+"Downloading: "+link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(dd)
        print(fg('green')+"Download accomplished :) ")
    except:
        c=c+1
        print(fg('red')+"$Error: "+link)
    

if c==(len(f.readlines())-1):
    color = fg('red')
else:
    if c==0:
        color =fg('green')
    else: color =fg('yellow')
print(color+'Task Completed!') 
f.close()