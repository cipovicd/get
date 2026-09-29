import pwm_dac as pwm
import signal_generator as sg
import time
 
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
 
try:
    dac = pwm.PWM_DAC(12, 500, 3.290)
    start_time = time.time()
 
    while True:
        t = time.time() - start_time
        normalized = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = amplitude * normalized
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
 
finally:
    dac.deinit()
