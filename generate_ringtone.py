import wave
import math
import struct
import os

def generate_ringtone(filename, duration=3.0):
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # Ringing parameters
    freq1 = 840.0 # Standard Phone Ring Freq 1
    freq2 = 1020.0 # Standard Phone Ring Freq 2
    mod_freq = 20.0 # Ringer modulation (trill)
    
    # Intermittent ringing (2 sec ring, 4 sec silence - looping handled by game? No, let's make a seamless loop of "ring-ring")
    # Actually, standard US ring is 2s ring, 4s silent.
    # UK is double ring.
    # Let's make a 3 second loop: Ring (1.5s) - Silence (1.5s) for faster feedback
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1) # Mono
        wav_file.setsampwidth(2) # 16-bit
        wav_file.setframerate(sample_rate)
        
        for i in range(num_samples):
            t = i / sample_rate
            
            # Simple envelope: Ring for 0-1.5s, Silence 1.5-3.0s
            if t < 1.5:
                # Modulate amplitude for "ringing" effect (20Hz)
                mod = 0.5 + 0.5 * math.sin(2 * math.pi * mod_freq * t)
                
                # Combine two frequencies
                val = 0.5 * math.sin(2 * math.pi * freq1 * t) + \
                      0.5 * math.sin(2 * math.pi * freq2 * t)
                
                sample_val = val * mod * 32767 * 0.5 # 50% volume
            else:
                sample_val = 0
            
            wav_file.writeframes(struct.pack('h', int(sample_val)))

if __name__ == "__main__":
    output_path = "assets/sounds/phone_ring.wav"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_ringtone(output_path)
    print(f"Generated {output_path}")
