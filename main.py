from audio_handler_package.audio_handler import AudioHandler

def main():
    audio_handler = AudioHandler()
    audio_handler.start()
    audio_handler.mainloop()
    audio_handler.stop()

if __name__ == "__main__":
    main()
