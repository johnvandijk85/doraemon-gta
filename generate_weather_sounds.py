import numpy as np
import scipy.io.wavfile as wavfile
import random
import os

# Create directory if it doesn't exist
output_dir = "assets/sounds"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

sample_rate = 44100

def generate_noise(duration, amp=0.1):
    t = np.linspace(0, duration, int(sample_rate * duration))
    noise = np.random.normal(0, 1, len(t))
    return noise * amp

def low_pass_filter(data, alpha=0.1):
    # Simple low pass filter
    filtered = np.zeros_like(data)
    filtered[0] = data[0]
    for i in range(1, len(data)):
        filtered[i] = filtered[i-1] + alpha * (data[i] - filtered[i-1])
    return filtered

def generate_rain(duration=5.0):
    # Pink-ish noise for rain
    noise = generate_noise(duration, amp=0.15)
    # Apply simple low pass to make it less harsh (more like rain, less like static)
    filtered = low_pass_filter(noise, alpha=0.2)
    return np.int16(filtered * 32767)

def generate_thunder(duration=3.0):
    # Explosion-like burst with decay
    t = np.linspace(0, duration, int(sample_rate * duration))
    noise = np.random.normal(0, 1, len(t))
    
    # Envelope: Sharp attack, long exponential decay
    envelope = np.exp(-3 * t) 
    
    # Add some rumble (low frequency modulation)
    rumble = np.sin(2 * np.pi * 50 * t) * 0.5 + 0.5
    
    thunder = noise * envelope * rumble * 0.8
    
    # Low pass heavilly for distant thunder
    filtered = low_pass_filter(thunder, alpha=0.05)
    
    return np.int16(filtered * 32767)

# Generate Rain
print("Generating Rain...")
rain_data = generate_rain(duration=10.0) # 10 seconds loop
wavfile.write(f"{output_dir}/rain.wav", sample_rate, rain_data)
print(f"Saved {output_dir}/rain.wav")

# Generate Thunder
print("Generating Thunder...")
thunder_data = generate_thunder(duration=4.0)
wavfile.write(f"{output_dir}/thunder.wav", sample_rate, thunder_data)
print(f"Saved {output_dir}/thunder.wav")
