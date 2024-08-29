import numpy as np

from what2_dsp.types import FloatArr
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import gaussian


def power_ratio(power: float, db: float) -> float:
    pass


def compute_power(signal: FloatArr) -> float:
    """
    Compute average power in watts of a signal.
    """

    return float(np.mean(signal ** 2))


def compute_spectrum(signal: FloatArr, scale: float | None = None):
    if scale is None:
        scale = len(signal) / 10
    g_std = 12  # standard deviation for Gaussian window in samples
    win = gaussian(50, std=g_std, sym=True)  # symmetric Gaussian wind.
    SFT = ShortTimeFFT(win, hop=2, fs=1/scale, mfft=800, scale_to='psd')

    return SFT.spectrogram(signal)
