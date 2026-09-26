EXPERIMENTS = [
    # (mixture_path, prompt, prompt_type)
    ("samples/speech_music.wav", "speech",                                        "short"),
    ("samples/speech_music.wav", "a person talking clearly in the foreground",    "detailed"),
    ("samples/speech_music.wav", "music",                                         "short"),
    ("samples/speech_music.wav", "instrumental background music, no vocals",      "detailed"),
    ("samples/rain_speech.wav",  "rain",                                          "short"),
    ("samples/rain_speech.wav",  "heavy rainfall with no human voices",           "detailed"),
    ("samples/traffic_birds.wav","bird chirping",                                 "short"),
    ("samples/traffic_birds.wav","birds chirping clearly above traffic noise",    "detailed"),
]
