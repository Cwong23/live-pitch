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
        self.label = tk.Label(self.root, text="Pitch Detector GUI")
        self.label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start Audio", command=self.start_audio)
        start_button.pack(pady=10)

        end_button = tk.Button(self.root, text="Stop Audio", command=self.end_audio)
        end_button.pack(pady=10)
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
