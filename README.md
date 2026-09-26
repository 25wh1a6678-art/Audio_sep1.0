# Audio_sep1.0

A web application for text-guided audio source separation using AudioSep. Upload a mixed audio file, enter a natural-language prompt (e.g. `"human speech"`, `"background music"`), and get the separated target sound.

---

## How to Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## How to Reproduce Experiments

```bash
python run_experiments.py
```

Results are saved to `outputs/` and logged to `experiments.md`.

---

## Project Structure

```
/
├── README.md
├── inference.py          # shared separation function
├── metrics.py            # SDR scoring via mir_eval
├── run_experiments.py
├── app.py                # Streamlit interface
├── samples/              # input mixtures
├── outputs/              # separated results
├── report/               # 2-page write-up
├── experiments.md        # results table
└── requirements.txt
```

---

## Prompt Wording Findings

_To be filled after experiments._

---

## Screenshots

_To be added._
