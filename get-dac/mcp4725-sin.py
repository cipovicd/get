import mcp4725_driver as mcp
import signal_generator as sg
import time
 
amplitude = 5.0
signal_frequency = 10
sampling_frequency = 1000
 
try:
    dac = mcp.MCP4725(5.0, 0x61, False)
    start_time = time.time()
 
    while True:
        t = time.time() - start_time
        normalized = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = amplitude * normalized
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
 
finally:
    dac.deinit()
