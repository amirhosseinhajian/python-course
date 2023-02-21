import pysynth_b as psb

song = (('d', 4), ('d', 4), ('c', 4), ('c', 4), 
        ('b', 4), ('a', 4), ('g', 4), ('g5', 4),
        ('g5*', 4), ('e5', 4),  ('d5', 4), ('e5*', 2))
psb.make_wav(song, fn = "danube.wav", leg_stac = .7, bpm = 180)