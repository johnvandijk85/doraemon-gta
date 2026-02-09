import wave
import struct
import math
import os
import subprocess
import random

def generate_radio_voice(text, filename):
    print(f"Generating: '{text}' -> {filename}")
    
    # 1. Use 'say' to generate WAV directly
    # 'Cellos' is a good weird voice, but 'Alex' or 'Samantha' at high speed is better for "radio chatter"
    # -r 200 = fast speaking
    temp_wav = "temp_voice.wav"
    subprocess.call(['say', '-o', temp_wav, '--data-format=LEI16@22050', '-r', '220', text])
    
    if not os.path.exists(temp_wav):
        print("Failed to generate wav with say")
        return

    # 2. Post-Process (Lo-Fi Radio Effect)
    with wave.open(temp_wav, 'rb') as w_in:
        params = w_in.getparams()
        frames = w_in.readframes(params.nframes)
        samples = struct.unpack(f"{params.nframes}h", frames)
        
    processed_samples = []
    
    # Filter states
    low_pass_val = 0
    high_pass_val = 0
    
    for s in samples:
        # 1. Pre-Gain / Drive
        val = s * 5.0 
        
        # 2. Crossover gate (reduce background silence noise if any, though 'say' is clean)
        # Actually for 'radio', we WANT noise in silence.
        
        # 3. Hard Clip (Distortion)
        val = max(-25000, min(25000, val))
        
        # 4. Bandpass Filter (Telephone EQ)
        # Simple Low Pass
        low_pass_val += 0.4 * (val - low_pass_val)
        # Simple High Pass
        high_pass_val = 0.8 * (high_pass_val + low_pass_val - (processed_samples[-1] if processed_samples else 0))
        
        val = high_pass_val * 1.5 # Makeup gain
        
        # 5. Bitcrush (Low Res Digital Radio)
        # Quantize to steps
        step_size = 1500
        val = round(val / step_size) * step_size
        
        # 6. Add White Noise / Static
        noise = random.randint(-1500, 1500)
        
        final = val + noise
        final = max(-32767, min(32767, int(final)))
        processed_samples.append(final)

    # 3. Save Final
    with wave.open(filename, 'w') as w_out:
        w_out.setparams(params)
        w_out.writeframes(struct.pack(f"{len(processed_samples)}h", *processed_samples))
        
    os.remove(temp_wav)

if __name__ == "__main__":
    os.makedirs("assets/sounds", exist_ok=True)
    
    # Kill Mission
    generate_radio_voice("I want you to neutralize the enemies.", "assets/sounds/mission_kill.wav")
    
    # Steal Mission
    generate_radio_voice("I need you to steal some cars for me.", "assets/sounds/mission_steal.wav")
    
    print("Batch generation complete.")
