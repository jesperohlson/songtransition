from pydub import AudioSegment

# Audio Normalization Function
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Load songs
song1 = AudioSegment.from_file("lilbaby-grace.mp3")
song2 = AudioSegment.from_file("playboicarti-location.mp3")

#Target Normalization
target_dBFS = -20.0  # Good starting point
song1 = match_target_amplitude(song1, target_dBFS)
song2 = match_target_amplitude(song2, target_dBFS)

# Duration of crossfade (in milliseconds)
crossfade_duration = 5000

# Combine with crossfade
mixed = song1.append(song2, crossfade=crossfade_duration)

# Export result
mixed.export("seamless_mix.mp3", format="mp3")
print("Finsished")
