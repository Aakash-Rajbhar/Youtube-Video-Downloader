from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if (len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        
        else:
            ytdError.config(text="Paste Link Again!!",fg="red")

    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root= Tk()
root.title("YT VIDEO DOWNLOADER")
root.geometry("350x400")
root.columnconfigure(0,weight=1)
root.resizable(False, False)

ytdLabel= Label(root,text="Enter the URL of the Video", font=("jost",15))
ytdLabel.grid()

ytdEntryVar=StringVar()
ytdEntry=Entry(root, width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root, text="Error Msg", fg="red", font=("jost",10))
ytdError.grid()

saveLabel = Label(root,text="Save the Video File", font=("jost",15,"bold"))
saveLabel.grid()

saveEntry = Button(root, width=10, bg="red", fg="white", text="Choose Path", command=openLocation)
saveEntry.grid()

locationError = Label(root,text="Error Msg of Path", fg="red", font=("jost",10))
locationError.grid()

ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

choices = ["720p", "144p","Only Audio"]
ytdchoices= ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white", command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root, text="Developer : Aakash Rajbhar",font=("jost",15))
developerlabel.grid()

root.mainloop()