import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from BackEnd import DownloadYoutube

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.YD = DownloadYoutube()
        self.root = root
        self.root.title("YouTube Downloader")

        # Set theme to something styleable
        style = ttk.Style()
        style.theme_use("clam")

        # Styling
        style.configure("TFrame", background="#f5f6fa")
        style.configure("TLabel", background="#f5f6fa", font=("Segoe UI", 11))
        style.configure("TEntry", relief="flat", padding=5)
        
        # Custom button style
        style.configure("Custom.TButton",
                        font=("Segoe UI", 11, "bold"),
                        foreground="#ffffff",
                        background="#273c75",
                        borderwidth=0)
        style.map("Custom.TButton",
                  background=[("active", "#40739e"), ("!disabled", "#273c75")],
                  foreground=[("active", "#ffffff")])

        main_frame = ttk.Frame(root, padding=20, style="TFrame")
        main_frame.pack(fill="both", expand=True)

        self.url_var = tk.StringVar()
        self.path_var = tk.StringVar()

        ttk.Label(main_frame, text="YouTube URL:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(main_frame, textvariable=self.url_var, width=40).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Save Path:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(main_frame, textvariable=self.path_var, width=30).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Button(main_frame, text="Browse", command=self.browse_path, style="Custom.TButton").grid(row=1, column=2, padx=5, pady=5)

        ttk.Button(main_frame, text="Download MP3", command=self.download_mp3, style="Custom.TButton").grid(row=2, column=0, padx=5, pady=10)
        ttk.Button(main_frame, text="Download MP4", command=self.download_mp4, style="Custom.TButton").grid(row=2, column=1, padx=5, pady=10)

    def DonePopUp(self):
        popup = tk.Toplevel(self.root)
        popup.title("Done")
        ttk.Label(popup, text="Done Downloading").pack(padx=20, pady=20)
        ttk.Button(popup, text="OK", command=popup.destroy, style="Custom.TButton").pack(pady=(0, 10))

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
