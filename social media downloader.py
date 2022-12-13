from pytube import YouTube




def py_download(youtube_link):
    YouTube_Download = YouTube(youtube_link).streams.get_highest_resolution()
    
    try:
        print(f" {YouTube_Download} is downloading..... ")
        YouTube_Download.download("video/")
        print(f" {YouTube_Download} is downloaded ")

    except:
        print("error ")



        





    
youtube_link =  str(input("Enter your Youtube download link : "))
py_download(youtube_link)