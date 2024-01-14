# write a function which will be able to shutdown your system.
# /s - shutdown
# /r - restart
# /t - time in second
import os


def shutdown_sys():
    shtdn = os.system("shutdown /r /t 5")
    return shtdn


shutdown_sys()