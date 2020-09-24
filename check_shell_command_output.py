import os
import traceback
import subprocess

ROOT_DIRECTORY = '/home/shadhini/dev'


if __name__ == "__main__":

    current_dir = subprocess.check_output('pwd', shell=True)

    os.system("cd {}".format(ROOT_DIRECTORY))

    try:

        print("1 current dir: ", current_dir)
        current_dir = subprocess.check_output('pwd', shell=True)
        print("2 current dir: ", current_dir)

    except Exception:
        traceback.print_exc()