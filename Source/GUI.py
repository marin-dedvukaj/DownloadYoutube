import tkinter as tk
from tkinter import filedialog
from BackEnd import DownloadYoutube
class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.YD = DownloadYoutube()
        self.root = root
        self.root.title("YouTube Downloader")

        self.url_var = tk.StringVar()
        self.path_var = tk.StringVar()

        tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(root, textvariable=self.url_var, width=40).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Save Path:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(root, textvariable=self.path_var, width=30).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        tk.Button(root, text="Browse", command=self.browse_path).grid(row=1, column=2, padx=5, pady=5)

        tk.Button(root, text="Download MP3", command=self.download_mp3).grid(row=2, column=0, padx=5, pady=10)
        tk.Button(root, text="Download MP4", command=self.download_mp4).grid(row=2, column=1, padx=5, pady=10)
    def DonePopUp(self):
        popup = tk.Toplevel(self.root)
        popup.title("Done")
        tk.Label(popup, text="Done Downloading").pack(padx=20, pady=20)
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=(0, 10))
    

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def download_mp3(self):
        self.YD.OutputPath = self.path_var.get()
        self.YD.downloadMp3(self.url_var.get())
        self.DonePopUp()

    def download_mp4(self):
        self.YD.OutputPath = self.path_var.get()
        self.YD.downloadMp4(self.url_var.get())
        self.DonePopUp()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()