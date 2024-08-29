from what2_dsp import gen
from what2_dsp.analyze import compute_power
from what2_dsp.common import mk_seed
import numpy as np

import pytest
from _pytest.python_api import ApproxScalar
from what2 import dbg
type RandGen = np.random.Generator

@pytest.fixture
def rng(request: pytest.FixtureRequest) -> RandGen:
    return np.random.default_rng(mk_seed())


def test_power_measured_matches_power_generated_whitenoise(rng: RandGen):
    sig_size = 100000

    for _ in range(1000):
        power = rng.uniform(
            low=0,
            high=100,
        )

        signal = gen.white_noise(
            power,
            sig_size,
        )

        measured_power = compute_power(signal)

        expected_power = ApproxScalar(
            power,
            rel=0.01,
        )

        assert measured_power == expected_power


def test_power_measured_matches_power_generated_sinewave(rng: RandGen):
    sig_size = 100000

    for _ in range(100):
        power = rng.uniform(
            low=0,
            high=100,
        )

        signal = gen.sine_wave(
            power,
            sig_size,
        )

        measured_power = compute_power(signal)

        expected_power = ApproxScalar(
            power,
            rel=0.01,
        )

        dbg(power)
        assert measured_power == expected_power
