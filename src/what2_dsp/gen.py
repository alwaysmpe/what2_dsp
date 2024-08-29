import numpy as np

from what2_dsp.common import mk_seed
from what2_dsp.types import FloatArr


def white_noise(power: float, samples: int) -> FloatArr:
    gen = np.random.default_rng(mk_seed())

    scale = power ** 0.5

    return gen.normal(
        loc=0.0,
        scale=scale,
        size=samples,
    )


def sine_wave(power: float, samples: int, wave_length: float | None = None) -> FloatArr:
    idx = np.linspace(
        0,
        samples-1,
        samples,
    )

    if wave_length is None:
        wave_length = samples / 10
    
    phase: FloatArr = idx / wave_length

    angle: FloatArr = phase * np.pi

    magnitude = np.sin(angle)

    scale = (power * 2) ** 0.5

    return magnitude * scale
