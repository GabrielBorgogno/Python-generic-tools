from pytube import YouTube
link = ''
yt = YouTube("https://www.youtube.com/watch?v=BsTu17RmQAk&list=RDBsTu17RmQAk&start_radio=1") #Patrick Bateman Theme Song

#Title of video
print("Title:",yt.title)#Number of views of video
print("Number of views: ",yt.views)#Length of the video
print("Length of video:",yt.length,"seconds")#Description of video
print("Description: ",yt.description)#Rating
print("Ratings: ",yt.rating)
print(yt.streams)
ys = yt.streams.get_highest_resolution()
ys.download()