import simpleaudio, time



class Meternome:
    

    def __init__(self, beats_per_minute):
        self.beats_per_min = beats_per_minute
        self.accent_note = 1
        self.beats_per_beat = 1
    
    def update():
        pass

    def bpmtoString(self):
        beatsPM = self.beats_per_minute
        beatsString = ["Grave", "Largo", "Adagio", "Andante", "Moderato", "Allegro", "Presto", "Prestissimo"]
        if beatsPM < 40:
            return beatsString[0]
        elif beatsPM < 66:
            return beatsString[1]
        elif beatsPM < 76:
            return beatsString[2]
        elif beatsPM < 108:
            return beatsString[3]
        elif beatsPM < 120:
            return beatsString[4]
        elif beatsPM < 168:
            return beatsString[5]
        elif beatsPM < 200:
            return beatsString[6]
        else:
            return beatsString[7]
        
    def meternomeClick(self):
        thirdTone = simpleaudio.WaveObject.from_wave_file('weak_beat.wav')
        strong_beat = simpleaudio.WaveObject.from_wave_file('strong_beat.wav')
        weak_beat = simpleaudio.WaveObject.from_wave_file('weak_beat.wav')
        
        while True:
            strong_beat.play()
            time.sleep(60/self.beats_per_min/self.beats_per_beat)
            for l in range(self.beats_per_beat - 1):
                thirdTone.play()
                time.sleep(60 / self.beats_per_min / self.beats_per_beat)
            for i in range(self.accent_note - 1):
                weak_beat.play()
                time.sleep(60 / self.beats_per_min / self.beats_per_beat)
                for j in range(self.beats_per_beat - 1):
                    thirdTone.play()
                    time.sleep(60/self.beats_per_min/self.beats_per_beat)

