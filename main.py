from audio_handler_package.audio_handler import AudioHandler
from gui_package.gui import AudioGUI

def main():
    audio_handler = AudioHandler()
    gui = AudioGUI(audio_handler=audio_handler)
    gui.run()

if __name__ == "__main__":
    main()
