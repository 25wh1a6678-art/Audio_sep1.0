# AudioSep 5-Hour Build Spec

**Goal:** Compress the full month-long plan into a single 5-hour execution pass that produces a working, demo-able deliverable.

**Ground rule:** Prioritize a *working end-to-end pipeline* over completeness. If something doesn't fit in time, cut it — never leave the core pipeline broken to add polish.

---

## Hour 0:00–1:00 — Setup & Pretrained Model Running

1. Clone AudioSep repo (`https://github.com/Audio-AGI/AudioSep`).
2. Create a virtualenv, install dependencies from `requirements.txt`. Note Python/CUDA version constraints if GPU is available; fall back to CPU inference if not (accept slower runtime).
3. Download the pretrained checkpoint per the repo's instructions.
4. Run the repo's own example/inference script on one provided sample mixture + text prompt to confirm the environment works before writing any new code.
5. **Checkpoint:** one separated `.wav` file produced from a known-good example. If this fails, debug before proceeding — nothing downstream matters until inference works once.

---

## Hour 1:00–2:00 — Test Mixtures & Prompt Runs

1. Assemble 3–5 short (5–15s) audio mixtures. Fastest path: download or synthesize (e.g. overlay two clips with `pydub`/`ffmpeg`). Suggested set:
   - Speech + music → prompt: `"human speech"`
   - Speech + music → prompt: `"background music"`
   - Rain + speech → prompt: `"rain"`
   - Traffic + bird sounds → prompt: `"bird chirping"`
2. Write `run_experiments.py` that loops over (mixture, prompt) pairs, runs inference, and saves outputs to `outputs/<mixture_name>__<prompt_slug>.wav`.
3. Log each run's runtime and any errors to a CSV/markdown table — this becomes the experiment record for Hour 4.

---

## Hour 2:00–3:30 — Streamlit App

Build `app.py`:
- File uploader for a mixed audio file (`.wav`/`.mp3`)
- Text input for the extraction prompt
- "Separate" button that calls the same inference function used in `run_experiments.py` (factor it into a shared `inference.py` module — don't duplicate logic)
- `st.audio` playback for both the original upload and the separated output
- Download button for the separated output
- Basic error handling (no file, empty prompt, inference failure) shown as `st.error`, not a crash

Keep styling minimal — functionality over design.

---

## Hour 3:30–4:15 — The Extension: Prompt Wording Effect

1. For 3 mixtures, run each with a short prompt vs. a detailed/descriptive prompt:
   - Short: `"speech"` vs. detailed: `"a person talking clearly in the foreground"`
   - Short: `"music"` vs. detailed: `"instrumental background music, no vocals"`
   - Short: `"rain"` vs. detailed: `"heavy rainfall with no human voices"`
2. Compute SDR (Signal-to-Distortion Ratio) using `mir_eval` in `metrics.py` — even on 2 mixtures this gives a quantitative result.
3. Compare outputs qualitatively too — note differences (cleaner separation, more bleed-through, prompt ignored, etc.).
4. Record both SDR scores and qualitative notes directly in the experiment table.

---

## Hour 4:15–5:00 — Repo Organization, Write-up, Demo

1. Final repo structure:
   ```
   /
   ├── README.md
   ├── inference.py          # shared separation function
   ├── metrics.py            # SDR computation via mir_eval
   ├── run_experiments.py
   ├── app.py                # Streamlit interface
   ├── samples/              # input mixtures
   ├── outputs/              # separated results
   ├── report/               # short 2-page PDF write-up
   ├── experiments.md        # results table with SDR + qualitative notes
   └── requirements.txt
   ```
2. `experiments.md` table columns: `mixture | prompt | prompt_type | SDR | result quality (1–5) | observations`
3. `README.md`: what the project does, how to run `app.py`, how to reproduce `run_experiments.py`, and a 3–5 sentence summary of prompt-wording findings.
4. `report/` — a short 2-page write-up (abstract, method, results table, conclusion). This is what makes it IEEE-noticeable.
5. If time allows, record a short screen capture — otherwise screenshots in the README is acceptable.

---

## Non-negotiables if time runs out

Cut in this order, stopping as soon as you're within budget:
1. Extra mixtures beyond 3
2. Screen recording (keep screenshots)
3. Streamlit polish (keep it ugly but functional)
4. Detailed observations in the experiment table (keep them terse)
5. report/ PDF (keep the experiments.md at minimum)

**Never cut:** a working inference pipeline, the Streamlit "Separate" button actually working end-to-end, and the README explaining how to run it.

---

## Commit Plan (push after every commit)

| # | Commit Message | What's Included |
|---|---------------|-----------------|
| 1 | `chore: init repo structure` | `samples/.gitkeep`, `outputs/.gitkeep`, `report/.gitkeep` |
| 2 | `chore: add .gitignore` | ignore `__pycache__`, `*.pyc`, `venv/`, checkpoints, large `.wav` outputs |
| 3 | `chore: add requirements.txt` | all dependencies incl. `streamlit`, `mir_eval`, `pydub`, `torch` |
| 4 | `docs: add README skeleton` | title, sections stubbed, badges placeholder |
| 5 | `docs: add DOC.md build spec` | this file |
| 6 | `feat: inference.py — model loading` | checkpoint load logic only |
| 7 | `feat: inference.py — separate() function` | separation call, input/output handling |
| 8 | `feat: metrics.py — compute_sdr()` | SDR via `mir_eval`, takes reference + estimated wav paths |
| 9 | `data: add mixture 1 — speech + music` | `samples/speech_music.wav` |
| 10 | `data: add mixture 2 — rain + speech` | `samples/rain_speech.wav` |
| 11 | `data: add mixture 3 — traffic + birds` | `samples/traffic_birds.wav` |
| 12 | `feat: run_experiments.py — define pairs config` | mixture/prompt pairs list |
| 13 | `feat: run_experiments.py — inference loop` | loop, saves to `outputs/` |
| 14 | `feat: run_experiments.py — SDR scoring` | calls `compute_sdr()` per run |
| 15 | `feat: run_experiments.py — log to experiments.md` | appends rows with SDR + runtime |
| 16 | `docs: add experiments.md table header` | empty table with all columns defined |
| 17 | `feat: app.py — file uploader + prompt input` | input widgets only |
| 18 | `feat: app.py — separate button wired to inference.py` | button calls `separate()` |
| 19 | `feat: app.py — audio playback` | `st.audio` for original and output |
| 20 | `feat: app.py — download button` | `st.download_button` for separated output |
| 21 | `feat: app.py — error handling` | `st.error` for no file / empty prompt / inference failure |
| 22 | `results: short prompt runs + outputs` | `outputs/` files from short prompts, partial `experiments.md` |
| 23 | `results: detailed prompt runs + outputs` | `outputs/` files from detailed prompts, remaining rows |
| 24 | `results: complete experiments.md` | SDR scores, quality ratings, observations for all runs |
| 25 | `docs: add report write-up` | `report/` 2-page PDF — abstract, method, results, conclusion |
| 26 | `docs: update README — run instructions + findings` | how to run app + reproduce experiments + prompt-wording summary |
| 27 | `docs: add screenshots to README` | Streamlit app screenshots embedded |

**Total: 27 commits, push after each one.**
