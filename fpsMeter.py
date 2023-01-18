import subprocess
import adbutils

def getGfxinfo(targetPackage): 
    rawData = subprocess.run(["adb", "shell", "dumpsys", "gfxinfo", targetPackage], capture_output=True, text=True)
    