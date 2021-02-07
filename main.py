from pytube import YouTube, Playlist

Choose = input("Enter your Choose : ")
if Choose == "v":
    link = input("Enter The link Video : ")
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path="D:\Download Video")

elif Choose == "p":
    link = input("Enter The link playlist_Video : ")
    v = Playlist(link)
    for video in v.videos:
        video.streams.get_highest_resolution.download(output_path="D:\Download Video")
