import subprocess

def get_system_info():
    """Retrieve system information from the emulator."""
    print("Fetching system information...")
    commands = {
        "OS Version": "adb shell getprop ro.build.version.release",
        "Device Model": "adb shell getprop ro.product.model",
        "Available Memory": "adb shell cat /proc/meminfo | grep MemAvailable"
    }
    for info, cmd in commands.items():
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"{info}: {result.stdout.strip()}")
        else:
            print(f"Error fetching {info}: {result.stderr.strip()}")

def install_apk(apk_path):
    """Install an APK on the emulator."""
    print(f"Installing APK from: {apk_path}")
    result = subprocess.run(["adb", "install", apk_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("APK installed successfully.")
    else:
        print(f"Error installing APK: {result.stderr.strip()}")

def main():
    """Main function to retrieve information from the running emulator."""
    print("Connecting to the emulator...")
    try:
        # Retrieve system information
        get_system_info()
        
        # Optionally, install an APK
        apk_path = "C:/Users/Dhruv Chaudhary/Desktop/android_system/sample.apk"  # Replace with your actual APK path
        install_apk(apk_path)
    except Exception as e:
        print(f"Error interacting with emulator: {str(e)}")

if __name__ == "__main__":
    main()
