import scipy.io.wavfile as wavf
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Read and Generate Signals
CLEAN_AUDIO_FILE_PATH='./MT1_speech_clean.wav'

sample_rate, clean_audio_signal = wavf.read(CLEAN_AUDIO_FILE_PATH)
clean_audio_no_samples = clean_audio_signal.size

# Thanks to https://stackoverflow.com/a/53688043 for relating SNR to parameters of Gaussian noise
TARGET_SNR_DB = 2000 # Adjust this parameter to adjust strength of noise VS pure audio signal. Note I think the calculations below have incorrectly used this parameter. Hence it does not truely represent SNR DB

clean_audio_avg_db = 10 ** (np.log10(np.mean(clean_audio_signal)))
noise_avg_db = clean_audio_avg_db - TARGET_SNR_DB
noise_avg_power = 10 ** (noise_avg_db / 10)

noise_signal = np.random.normal(0, np.sqrt(noise_avg_power), clean_audio_no_samples)

noisy_audio_signal = np.add(clean_audio_signal, noise_signal)

# Play Noisy Audio Signal
sd.play(noisy_audio_signal, sample_rate)

# Write Noisy Audio Signal to file
NOISE_SIGNAL_FILE_NAME='MT1_speech_noisy.wav'
wavf.write(NOISE_SIGNAL_FILE_NAME, sample_rate, noisy_audio_signal)

# Prepare Plot of Signals
fig, axs = plt.subplots(3)

fig.tight_layout(pad=2.0, h_pad=3)

axs[0].plot(clean_audio_signal)
axs[0].set_title('Clean Audio Signal (Time-Domain)')

axs[1].plot(noise_signal)
axs[1].set_title('AWGN Noise Signal (Time-Domain)')

axs[2].plot(noisy_audio_signal)
axs[2].set_title('Noisy Audio Signal (Clean Audio + AWGN Noise) (Time-Domain)')

for ax in axs.flat:
    ax.set(xlabel='Sample Number (n)', ylabel='Amplitude')

# Plot Signals
plt.show()
