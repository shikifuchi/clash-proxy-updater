#!/usr/bin/python

import psutil
import utils


# Step 1 Check if clash is running
def clash_running():
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if "clash".lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


clash_exists = clash_running()

# Step 2 request for the fastest prxy from url test
if clash_exists:
    suggest = utils.request_suggested()
    if suggest is not None:
        result = utils.select_global_proxy(suggest)
        print("Proxy update with result code ", result)

# Step 3 Update the GLOBAL proxy using the fastest
