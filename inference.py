import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "AudioSep"))

from pipeline import build_audiosep, inference as _audiosep_inference
import torch

CHECKPOINT_PATH = "AudioSep/checkpoint/audiosep_base_4M_steps.ckpt"
CONFIG_PATH = "AudioSep/config/audiosep_base.yaml"

_model = None
_device = None


def load_model():
    global _model, _device
    if _model is None:
        _device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        _model = build_audiosep(
            config_yaml=CONFIG_PATH,
            checkpoint_path=CHECKPOINT_PATH,
            device=_device,
        )
    return _model, _device


def separate(audio_path: str, prompt: str, output_path: str) -> str:
    model, device = load_model()
    _audiosep_inference(model, audio_path, prompt, output_path, device)
    return output_path
