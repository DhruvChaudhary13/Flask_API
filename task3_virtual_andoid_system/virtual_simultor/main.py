import os
import shutil
import subprocess
import time
import sys
import requests
import json

# Function to check dependencies (adb, emulator)
def check_dependencies():
    """Check if required tools (adb, emulator) are installed."""
    tools = ["adb", "emulator"]
    for tool in tools:
        if not shutil.which(tool):
            print(f"Error: {tool} is not installed or not in PATH.")
            sys.exit(1)
    print("All dependencies are satisfied.")

# Function to start the Android emulator
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

# Function to wait for the emulator to finish booting
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

# Function to get system information from the emulator
def get_system_info():
    """Retrieve system information from the emulator."""
    print("Fetching system information...")
    commands = {
        "OS Version": "adb shell getprop ro.build.version.release",
        "Device Model": "adb shell getprop ro.product.model",
        "Available Memory": "adb shell cat /proc/meminfo | grep MemAvailable"
    }
    
    system_info = {}
    for info, cmd in commands.items():
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            system_info[info] = result.stdout.strip()
        else:
            system_info[info] = f"Error fetching {info}: {result.stderr.strip()}"
    
    return system_info

# Function to send the system info to the Flask API
def send_data_to_server(system_info):
    """Send the fetched system info to the Flask API."""
    api_url = "http://127.0.0.1:5000/add-data"  # Replace with your Flask server URL
    device_data = {
        "device_id": "12345",  # You can customize this as needed
        "system_info": system_info
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(api_url, json=device_data, headers=headers)
    if response.status_code == 200:
        print("Data sent to the server successfully.")
    else:
        print(f"Error sending data: {response.status_code} - {response.text}")

# Main function to simulate the virtual Android system and send data to Flask API
def main():
    """Main function to simulate the virtual Android system."""
    # Check for dependencies
    check_dependencies()

    # Start emulator
    emulator_process = start_emulator("test_emulator")  # Replace with your AVD name
    try:
        print("Waiting for emulator to boot...")
        wait_for_device()
        print("Emulator is ready. Fetching system information...")

        # Fetch system information
        system_info = get_system_info()
        print("System Info:", system_info)

        # Send system information to Flask API
        send_data_to_server(system_info)
        
    finally:
        print("Emulator is running. Use `access_emulator_info.py` to interact with it.")

def kill_emulator():
    """Kill the running emulator."""
    print("Attempting to stop the running emulator...")
    try:
        # Run the adb command to kill the emulator
        result = subprocess.run(
            ["adb", "emu", "kill"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the command was successful
        if result.returncode == 0:
            print("Emulator stopped successfully.")
        else:
            print("Error stopping emulator:")
            print(result.stderr.strip())
    except Exception as e:
        print(f"Error killing emulator: {str(e)}")

# Run the main function
if __name__ == "__main__":
    main()
    # kill_emulator() ## enable it if you want to end the process
    
