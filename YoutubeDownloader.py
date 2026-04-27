import tkinter as tk
from tkinter import * 
from pytubefix import YouTube
from tkinter import messagebox, filedialog

import ctypes #set the icon 
myapp = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp)


root = tk.Tk()
root.geometry("800x300")
root.resizable(False,False)
root.title("Youtube Downloader")
root.config(background="#36454F")
img = PhotoImage(file="Youtube.png")
root.iconphoto(False,img)


video_link = StringVar()
download_path = StringVar()

def Functionality():
    title_label = Label(root, text='Youtube Video Downloader', padx=15, pady=15, font="Arial 14", bg= "Gray", fg= "white")
    title_label.grid(row=1,column=1,padx=15,pady=15,columnspan=3)


    link_label = Label(root, text="Youtube URL: ", bg="Gray")
    link_label.grid(row=2,column=0,padx=15,pady=15)

    root.linktext = Entry(root, width=40, textvariable=video_link, font="Arial 14")
    root.linktext.grid(row=2,column=1,padx=15,pady=15,columnspan=3)


def Browse2Location():
    download_Directory = filedialog.askdirectory(initialdir="YOUR PATH", title="Save Video")
    download_path.set(download_Directory)


def DownloadVideo():
    Youtube_link = video_link.get()
    download_folder = download_path.get()

    getVid = YouTube(Youtube_link)
    videoStream = getVid.streams.get_highest_resolution() # with pytube bakage you can do some changes in it like get_lowest_resolution() and other things 
    videoStream.download(download_folder)
    messagebox.showinfo("Success", "The Video Downloaded Successfully to \n" +download_folder) 

destination_label = Label(root, text="Select Path: ", bg= "Gray")
destination_label.grid(row=3, column=0, padx=15, pady=15)

root.destinationtext = Entry(root, width=40, textvariable=download_path, font="Arial 14")
root.destinationtext.grid(row=3, column=1, padx=15, pady=15, columnspan=3)

browse_btn = Button(root, text="Browse", command=Browse2Location, width=20, bg="Gray", relief=GROOVE)
browse_btn.grid(row=4, column=2, padx=15, pady=15)

download_btn = Button(root, text="Download Video", command=DownloadVideo, width=50, bg="Gray", relief=GROOVE)
download_btn.grid(row=4, column=1, padx=15, pady=15)


Functionality()
root.mainloop()



    
    
