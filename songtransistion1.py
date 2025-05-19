from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import librosa

# Audio Normalization Function
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Beat Detection Function
def get_beats(file):
    y, sr = librosa.load(file)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    return tempo, beat_times

# Trimming silence function
def trim_silence(sound, silence_thresh=-40, min_silence_len=1000):
    nonsilent = detect_nonsilent(sound, min_silence_len, silence_thresh)
    if nonsilent:
        start_trim = nonsilent[0][0]
        end_trim = nonsilent[-1][1]
        return sound[start_trim:end_trim]
    return sound

# Load songs
song1 = AudioSegment.from_file("lilbaby-grace.mp3")
song2 = AudioSegment.from_file("playboicarti-location.mp3")

#Target Normalization
target_dBFS = -20.0  # Good starting point
song1 = match_target_amplitude(song1, target_dBFS)
song2 = match_target_amplitude(song2, target_dBFS)

# Trimming the silence
song1 = trim_silence(song1)
song2 = trim_silence(song2)

song1.export("song1_audio.mp3", format="mp3")
song2.export("song2_audio.mp3", format="mp3")

# Duration of crossfade (in milliseconds)
crossfade_duration = 5000

# Combine with crossfade
mixed = song1.append(song2, crossfade=crossfade_duration)

# Export result
mixed.export("seamless_mix.mp3", format="mp3")
print("Finsished")
