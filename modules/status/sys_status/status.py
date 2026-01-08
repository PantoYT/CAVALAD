import platform
import psutil
import subprocess
import wmi

def get_system_info():
    print("=== System Information ===")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")

def get_disk_info():
    print("\n=== Disk Information ===")
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"{partition.device} ({partition.fstype}): {round(usage.total / (1042**3), 2)} GB total, {round(usage.used / (1042**3), 2)} GB used")

def get_drivers_info():
    print("\n=== Drivers ===")
    try:
        output = subprocess.check_output("driverquery", shell=True, text=True)
        print(output)
    except Exception as e:
        print(f"Error getting drivers: {e}")

def get_gpu_info():
    print("\n=== GPU Information ===")
    try: 
        c = wmi.WMI()
        for gpu in c.Win32_VideoController():
            print(f"{gpu.Name} - {gpu.DriverVersion}")
    except Exception as e:
        print(f"Error getting GPU info: {e}")

if __name__ == "__main__":
    get_system_info()
    get_disk_info()
    get_gpu_info()
    get_drivers_info()