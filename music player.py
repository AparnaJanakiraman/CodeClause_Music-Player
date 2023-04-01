import os
import tkinter as tk
import tkinter.filedialog as filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        
        pygame.mixer.init()

       
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="No song selected")
        self.label.pack()

        self.select_button = tk.Button(self.frame, text="Select Song", command=self.select_song)
        self.select_button.pack()

        self.play_button = tk.Button(self.frame, text="Play", command=self.play_song, state=tk.DISABLED)
        self.play_button.pack()

        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause_song, state=tk.DISABLED)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop_song, state=tk.DISABLED)
        self.stop_button.pack()

    def select_song(self):
        
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            
            song_name = os.path.basename(song_path)
            self.label.config(text=song_name)

            # Load the song
            pygame.mixer.music.load(song_path)

           
            self.play_button.config(state=tk.NORMAL)

    def play_song(self):
     
        pygame.mixer.music.play()

       
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def pause_song(self):
        
        pygame.mixer.music.pause()

    def stop_song(self):
        
        pygame.mixer.music.stop()

 
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)


root = tk.Tk()
music_player = MusicPlayer(root)


root.mainloop()
