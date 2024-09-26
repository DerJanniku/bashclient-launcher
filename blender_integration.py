import os
import subprocess

def start_blender():
    try:
        blender_path = "blender"  # Assuming Blender is in the system PATH
        subprocess.Popen([blender_path])
        print("Blender started successfully!")
    except Exception as e:
        print(f"Failed to start Blender: {e}")

if __name__ == "__main__":
    start_blender()
