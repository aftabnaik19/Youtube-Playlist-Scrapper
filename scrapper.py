import requests
from bs4 import BeautifulSoup
from pytube import Playlist,YouTube
import pandas as pd

# Replace 'YOUR_PLAYLIST_URL' with the actual URL of your YouTube playlist
p = '';
p = input();
vlinks=Playlist(p)
print("\n Playlist name=",vlinks.title)
print("\n No. of videos=",vlinks.length)
print("\n Playlist id=",vlinks._playlist_id)
print("\n Hello world")

dict={'Title':[] ,'Link':[]}
dataframe=pd.DataFrame(dict)

vtitles=[]
for link in vlinks:
    vtitles.append(YouTube(link).title)

print(*vlinks)
dataframe['Title']=vtitles
dataframe['Link']=vlinks
dataframe.to_excel("ytplaylist.xlsx")
print("Playlist extracted successfully");
