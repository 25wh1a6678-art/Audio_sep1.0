import numpy as np
import soundfile as sf
import mir_eval


def compute_sdr(reference_path: str, estimated_path: str) -> float:
    ref, sr_r = sf.read(reference_path)
    est, sr_e = sf.read(estimated_path)

    # mono, same length
    if ref.ndim > 1:
        ref = ref.mean(axis=1)
    if est.ndim > 1:
        est = est.mean(axis=1)
    min_len = min(len(ref), len(est))
    ref, est = ref[:min_len], est[:min_len]

    sdr, _, _, _ = mir_eval.separation.bss_eval_sources(
        ref[np.newaxis, :], est[np.newaxis, :]
    )
    return float(sdr[0])
