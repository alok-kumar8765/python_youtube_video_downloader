from pytube import YouTube

link = 'https://www.youtube.com/watch?v=EAYlckSaviI'
youtube_link = YouTube(link)

##*****************  Check Tile And Thumbnail Of Video *******************
# print(youtube_link.title)
# print(youtube_link.thumbnail_url)

##***************** Create Video Quality List So that Download According to That Quality of Single Video
videos = youtube_link.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

streaming = int(input('enter : '))
videos[streaming].download()
print("Downloaded Successfully!!")

##*****************  Download Audio Only
videos = youtube_link.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

streaming = int(input('enter : '))
videos[streaming].download()
print("Downloaded Successfully!!")

##*************** Download A Play list of a channel
#Step 1- first open the playlist on youtube, where playlist name display
#Step 2- after open playlist on title of playlist you find 3dots click on them
#Step 3- now copy url
from pytube import Playlist
playlist = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg")
print(f'Downloading :  {playlist.title}')
for video in playlist.videos:
    video.streams.first().download()