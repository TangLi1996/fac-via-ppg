import os
import subprocess

# Define input and output folder
input_folder = "/home/tang/PPG-Mel/fac-via-ppg/recordings/koren_YKWK"  # Change this to your recordings folder
output_folder = "/home/tang/PPG-Mel/fac-via-ppg/recordings/koren_YKWK_16k"  # Change this to your output folder

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each .wav file in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_path = os.path.join(input_folder, filename)
        # Keep the same filename
        output_path = os.path.join(output_folder, filename)

        # FFmpeg command to resample to 16kHz
        subprocess.run(["ffmpeg", "-i", input_path, "-ar", "16000", output_path])

print("✅ All recordings have been resampled to 16kHz!")