# Virtual Android System Simulator

This project simulates a virtual Android system using an emulator and sends system information to a Flask API.

## Requirements

- **Python 3.6+**
- Android SDK tools installed (including `adb` and `emulator`)
- Flask server running on `http://127.0.0.1:5000/add=data`
- `requests` Python library

## Installation

1. Install the required tools:
   - Ensure `adb` and `emulator` are in your system's PATH.
   - Install the `requests` library using pip:
     ```bash
     pip install requests
     ```



## Usage

1. **Run the main script:**
   ```bash
   python main.py



Replace "test_emulator" in the start_emulator function with your AVD name. **in my case emulator name is test_emulator**
Ensure your Flask API server is running before executing the script.


**script workin process**

The script checks for dependencies.
It starts the Android emulator with the specified AVD name (default: test_emulator).
Waits for the emulator to boot.
Fetches system information (OS version, device model, available memory).
Sends the information to the Flask API




**Example Output:**

{
  "OS Version": "11",
  "Device Model": "Pixel 4",
  "Available Memory": "2048000 kB"
}

