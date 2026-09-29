import numpy as np
import time
 
 
def get_sin_wave_amplitude(freq, current_time):
    return (np.sin(2 * np.pi * freq * current_time) + 1) / 2
 
 
def get_triangle_wave_amplitude(freq, current_time):
    return 2 * abs(0.5 - ((freq * current_time) % 1))
 
 
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)
