from pydub import AudioSegment
import csv

with open('niujin.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        word = row[1].strip()
        words = []
        if word.find(' ') != -1:
            words = word.split(' ')
        elif word.find('-') != -1:
            words = word.split('-')

        if words:
            combine = None
            for w in words:
                waveFileName = "../../../../Downloads/voice/" + w[0].lower() + "/" + w + ".wav"
                try:
                    sound = AudioSegment.from_file(waveFileName, format="wav")
                except FileNotFoundError:
                    print(waveFileName)
                    continue
                if combine:
                    combine = combine + AudioSegment.silent(duration=50) + sound
                else:
                    combine = sound

            file_handle = combine.export('../voices/' + '-'.join(words) + '.mp3', format="mp3", bitrate="32k")
        else:
            waveFileName = "../../../../Downloads/voice/" + word[0].lower() + "/" + word + ".wav"
            try:
                sound = AudioSegment.from_file(waveFileName, format="wav")
            except FileNotFoundError:
                print(waveFileName)
                continue
            file_handle = sound.export("../voices/" + word + ".mp3", format="mp3", bitrate="32k")
