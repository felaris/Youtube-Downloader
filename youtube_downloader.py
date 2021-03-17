from pytube import YouTube


link = input("Type in your Youtube link ")
video = YouTube(video)
stream = video.streams.get_highest_resolution()
stream.download()
