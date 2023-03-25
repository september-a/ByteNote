class Metronome:
    def __init__(self,app,t=60):
        tempo = t
        app.addCanvas("c1")
    
    def update():
        pass




import simpleaudio, time
strong_beat = simpleaudio.WaveObject.from_wave_file('strong_beat.wav')
weak_beat = simpleaudio.WaveObject.from_wave_file('weak_beat.wav')

beats_per_min = 120
accent_note = 4
beats_per_beat = 2
dummyvariable = 0

while True:
    strong_beat.play()
    time.sleep(60/beats_per_min/beats_per_beat)
    for k in range(beats_per_beat - 1):
        weak_beat.play()
        time.sleep(60/beats_per_min/beats_per_beat)
    for i in range(accent_note - 1):
        for j in range(beats_per_beat):
            weak_beat.play()
            time.sleep(60/beats_per_min/beats_per_beat)