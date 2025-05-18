from pydub import AudioSegment

# Load songs
song1 = AudioSegment.from_file("song1.mp3")
song2 = AudioSegment.from_file("song2.mp3")

# Duration of crossfade (in milliseconds)
crossfade_duration = 5000

# Combine with crossfade
mixed = song1.append(song2, crossfade=crossfade_duration)

# Export result
mixed.export("seamless_mix.mp3", format="mp3")
print("Finsished")
