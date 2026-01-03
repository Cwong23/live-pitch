import numpy as np
import pyaudio
import time
import librosa
from dataclasses import dataclass


@dataclass
class AudioHandler(object):
    format: int = pyaudio.paFloat32
    channels: int = 1
    rate: int = 44100
    chunk: int = 1024 * 2
    audio: pyaudio.PyAudio = pyaudio.PyAudio()
    stream: pyaudio.Stream = None

    def start(self):
        self.stream = self.audio.open(format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            output=False,
            stream_callback=self.callback,
            frames_per_buffer=self.chunk)

    def stop(self):
        self.stream.close()
        self.audio.terminate()

    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        librosa.feature.mfcc(numpy_array)
        return None, pyaudio.paContinue

    def mainloop(self):
        while (self.stream.is_active()):
            time.sleep(2.0)