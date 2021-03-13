from pydub import AudioSegment
import typing

def mananger_sounds(sounds:typing.List[str]):
    file_ready = []
    for place_in_list, file_path in enumerate(sounds):

        song = AudioSegment.from_mp3(file_path)

        # validacion if its the last file
        if place_in_list == len(sounds) - 1:
            last_sound = song.reverse()  # put the soudn in reverse
            file_ready.append((file_path, last_sound))
            continue

        duration = len(song)  # this bring me lenght the firts sound

        # slice audio, pydub does things in milliseconds
        half_duration = duration // 2
        add_two = half_duration + 2000

        # start manipulation the songs
        beginning_of_song = song[:half_duration]  # vamos a tomar la mitad
        two_seconds = song[half_duration: add_two]  # toma solo los siguente 2 segundo
        end_of_song = song[add_two:]

        # Make the beginning quieter and the end normal
        beginning = beginning_of_song - 40  # reduce volume by 40dB make quieter
        middle = two_seconds.silent()  # reduce volume for be silence

        combined_sounds = beginning + middle + end_of_song
        file_ready.append((file_path, combined_sounds))

        for file in file_ready:
            audiosegment = file[1]
            audio_name = file[0]
            audiosegment.export(audio_name,
                                format='mp3')
