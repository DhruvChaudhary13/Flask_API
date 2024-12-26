import subprocess
import time
import sys
import shutil

def check_dependencies():
    """Check if required tools (adb, emulator) are installed."""
    tools = ["adb", "emulator"]
    for tool in tools:
        if not shutil.which(tool):
            print(f"Error: {tool} is not installed or not in PATH.")
            sys.exit(1)
    print("All dependencies are satisfied.")

def start_emulator(avd_name="test_emulator"):
    """Launch the Android Emulator."""
    print(f"Attempting to start emulator with AVD name: {avd_name}...")
    emulator_cmd = ["emulator", "-avd", avd_name, "-no-snapshot-load", "-no-audio", "-no-boot-anim"]
    
    try:
        emulator_process = subprocess.Popen(
            emulator_cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("Emulator process started. Waiting for boot...")
        return emulator_process
    except Exception as e:
        print(f"Error launching emulator: {str(e)}")
        sys.exit(1)

def wait_for_device():
    """Wait for the emulator to finish booting."""
    print("Waiting for emulator to boot completely...")
    while True:
        result = subprocess.run(
            ["adb", "shell", "getprop", "sys.boot_completed"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0 and result.stdout.strip() == "1":
            print("Emulator boot completed.")
            break
        else:
            print("Emulator not ready yet. Retrying...")
        time.sleep(2)  # Retry every 2 seconds

def main():
    """Main function to start the emulator."""
    check_dependencies()
    emulator_process = start_emulator("test_emulator")  # Replace with your AVD name
    
    try:
        print("Waiting for emulator to boot...")
        wait_for_device()
        print("Emulator is ready. You can now run the second script to access information.")
    finally:
        print("Emulator is running. Use `access_emulator_info.py` to interact with it.")

if __name__ == "__main__":
    main()
