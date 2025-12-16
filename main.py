import platform
import shutil
import subprocess

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ignored non-critical error: {e}")

while True:
    user_input = str(input(">>>"))
    if user_input == "bye bye":
        exit
    else:
        run(user_input)