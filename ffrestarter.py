# FirefoxRestarter 0.01
# https://github.com/leszek9/FirefoxRestarter/

import subprocess
import time
import os

browserExe = "firefox.exe"


def ffrestart():
    while True:
        print("\nClosing Firefox...\n")
        os.system("taskkill /f /im "+browserExe)
        print("\nWaiting 5 seconds...\n")
        time.sleep(5)
        p = subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe'], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, bufsize=0)
        print(p)
        print("\nWait 1 hour for next Restart...\n")
        time.sleep(3600)


ffrestart()