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
        print("Starting audio handler...")
        self.stream = self.audio.open(format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            output=False,
            stream_callback=self.callback,
            frames_per_buffer=self.chunk)
        self.stream.start_stream()

    def stop(self):
        self.stream.close()
        self.audio.terminate()

    def freq_to_note(self, freq):
        A4 = 440.0
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F',
            'F#', 'G', 'G#', 'A', 'A#', 'B']

        n = int(round(12 * np.log2(freq / A4)))
        note_index = (n + 9) % 12
        octave = 4 + (n + 9) // 12

        return f"{note_names[note_index]}{octave}"

    def callback(self, in_data, frame_count, time_info, flag):
        audio = np.frombuffer(in_data, dtype=np.float32)
        if np.sqrt(np.mean(audio**2)) < 0.01:
            return None, pyaudio.paContinue

        f0 = librosa.yin(
            audio,
            fmin=50,
            fmax=2000,
            sr=self.rate
        )

        pitch_hz = np.median(f0[f0 > 0]) if np.any(f0 > 0) else None

        if pitch_hz:
            note = self.freq_to_note(pitch_hz)
            print(f"{pitch_hz:.1f} Hz → {note}")

        return None, pyaudio.paContinue
