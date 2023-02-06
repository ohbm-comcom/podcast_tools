"""Read sound file to generate an animation."""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from scipy.io import wavfile
from scipy.ndimage import zoom
import cv2

# Absolute path to a wav file
FILE = "/path/to/guest.wav"
OUTDIR = "/path/to/frames"

DURATION = 120  # seconds
FPS = 25
BINS = 100

ROWS_2D = 300
COLS_2D = 400

# =============================================================================
# Read file
fs, data = wavfile.read(FILE)

# Get the first channel
if len(data.shape) > 1:
    data = data.T[0]

# Normalize to -1 to +1 range
data = data // (2**16) * 2 - 1

f = 0
for f in range(FPS * DURATION):
    start = fs//FPS * f
    end = start + fs//FPS

    # Sample one visual frame long audio data
    a = data[start:end]

    # FFT
    b = fft(a)
    c = fftshift(b)

    # Downsample the spectrum for visual simplicity
    d = zoom(abs(c), 1 / (fs/FPS/BINS), prefilter=False)

    # Amplify for visual
    d *= 100.

    # Normalize
    d = d / (2**16) * ROWS_2D//2
    d = d.astype(np.uint32)

    # Convert to 2D numpy array
    arr = np.zeros((ROWS_2D//2, BINS), dtype=np.uint8)
    for i, j in enumerate(d):
        arr[0:j, i] = 255

    # Match desired 2Dwidth
    arr2 = np.repeat(arr, COLS_2D // BINS, axis=1)

    # Mirror reverse over X axis
    arr3 = np.zeros((ROWS_2D, COLS_2D), dtype=np.uint8)
    arr3[:ROWS_2D//2, :] = arr2[::-1, :]
    arr3[ROWS_2D//2:, :] = arr2

    # Save as jpeg
    outpath = os.path.join(OUTDIR, "frame-{}.jpeg".format(str(f).zfill(6)))
    cv2.imwrite(outpath, arr3)

print("Finished.")
