import tkinter as tk
from dataclasses import dataclass
from audio_handler_package.audio_handler import AudioHandler

@dataclass
class AudioGUI:
    audio_handler: AudioHandler
    label: tk.Label = None
    root: tk.Tk = tk.Tk()
    title: str = "Pitch Detector"
    width: int = 800
    height: int = 400

    def run(self):
        
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        
        self.note = tk.StringVar()
        self.note.set("Play a note...")
        self.label = tk.Label(self.root, textvariable=self.note)
        self.label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start Audio", command=self.start_audio)
        start_button.pack(pady=10)

        end_button = tk.Button(self.root, text="Stop Audio", command=self.end_audio)
        end_button.pack(pady=10)

        self.poll_audio()
        self.root.mainloop()

    def start_audio(self):
        try:
            self.audio_handler.start()
        except Exception as e:
            print(f"Error starting audio handler: {e}")

    def end_audio(self):
        try:
            self.audio_handler.stop()
        except Exception as e:
            print(f"Error stopping audio handler: {e}")

    def poll_audio(self):
        try:
            while True:
                text = self.audio_handler.note_queue.get_nowait()
                self.update_note(text)
        except Exception:
            pass

        self.root.after(50, self.poll_audio)

    def update_note(self, text):
        self.note.set(text)