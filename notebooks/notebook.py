from what2_dsp import gen, analyze, plot

sine = gen.sine_wave(
    power=1.0,
    samples=300,
)

display(plot.wave(sine))

# What's wrong with the below spectrogram?

display(plot.spectrum(sine))

noise = gen.white_noise(
    power=1.0,
    samples=300,
)

display(plot.wave(noise))

display(plot.spectrum(noise))


# +
def mk_noisy_sine(rel_power: float = 0.1):
    noise = gen.white_noise(
        power=rel_power,
        samples=300,
    )
    sine = gen.sine_wave(
        power=1.0,
        samples=300,
    )

    return noise + sine

noisy_signal = mk_noisy_sine()

# -

display(plot.wave(noisy_signal))
display(plot.wave(mk_noisy_sine(0.5)))

display(plot.spectrum(noisy_signal))
display(plot.spectrum(mk_noisy_sine(0.5)))
