import tkinter as tk
from dataclasses import dataclass

@dataclass
class AudioGUI:
    label: tk.Label = None
    root: tk.Tk = tk.Tk()
    title: str = "Pitch Detector"
    width: int = 800
    height: int = 400

    def run(self):
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.label = tk.Label(self.root, text="Hello, Python GUI!")
        self.label.pack(pady=20)

        button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        button.pack(pady=10)
        self.root.mainloop()

    def on_button_click(self):
        self.label.config(text="Button was clicked!")

        
temp = AudioGUI()
temp.run()
    