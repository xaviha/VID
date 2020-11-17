import pafy



url = input("INGRESA LA URL DEL VIDEO:> ")


video=pafy.new(url)

streams = video.streams

for i in streams:
    print(i)

best = video.getbest()
print(best.resolution, best.extension)

best.download(filepath="/home/xaviha/Desktop/")
print("Video Descargado para xaviha")
