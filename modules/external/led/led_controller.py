import subprocess
import sys

LED_ON_SCRIPT = r"C:\Scripts\led\led_on.py"
LED_OFF_SCRIPT = r"C:\Scripts\led\led_off.py"

def run_script(script_path: str, action: str):
    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )

    if result.returncode == 0 :
        print(f"Action '{action}' executed succesfully.")
        if result.stdout:
            print(result.stdout.strip())
    else:
        print(f"Action '{action}' failed.")
        if result.stderr:
            print(result.stderr.strip())
        elif result.stdout:
            print(result.stdout.strip())

def main():
    if len(sys.argv) < 2:
        print("Missing action: on/off")
        sys.exit(1)
    action = sys.argv[1].lower()

    if action == "on":
        run_script(LED_ON_SCRIPT, "on")
    elif action == "off":
        run_script(LED_OFF_SCRIPT, "off")
    else:
        print("Invalid command. Use on/off")
        sys.exit(1)

if __name__ == "__main__":
    main()