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

import os, time
from inference import separate

os.makedirs("outputs", exist_ok=True)

results = []

for mixture, prompt, ptype in EXPERIMENTS:
    slug = prompt.replace(" ", "_")[:30]
    mix_name = os.path.splitext(os.path.basename(mixture))[0]
    out_path = f"outputs/{mix_name}__{slug}.wav"

    print(f"Running: {mix_name} | {prompt}")
    t0 = time.time()
    separate(mixture, prompt, out_path)
    elapsed = round(time.time() - t0, 1)

    results.append((mix_name, prompt, ptype, elapsed, out_path))
    print(f"  -> saved to {out_path} ({elapsed}s)")

# SDR scoring — only if a reference clean file exists at samples/<mix>_ref.wav
from metrics import compute_sdr

for i, (mix_name, prompt, ptype, elapsed, out_path) in enumerate(results):
    ref_path = f"samples/{mix_name}_ref.wav"
    sdr = compute_sdr(ref_path, out_path) if os.path.exists(ref_path) else "N/A"
    results[i] = (mix_name, prompt, ptype, elapsed, out_path, sdr)

# Write to experiments.md
with open("experiments.md", "w") as f:
    f.write("| mixture | prompt | prompt_type | SDR | runtime (s) | quality (1-5) | observations |\n")
    f.write("|---------|--------|-------------|-----|-------------|---------------|--------------|\n")
    for mix_name, prompt, ptype, elapsed, out_path, sdr in results:
        sdr_str = f"{sdr:.2f}" if isinstance(sdr, float) else sdr
        f.write(f"| {mix_name} | {prompt} | {ptype} | {sdr_str} | {elapsed} | | |\n")

print("\nexperiments.md updated.")
