# Clash Proxy Updater

## Description

This script will 

1. check if clash is running or not
2. If it is running, request its restful api to get the fastest
3. Apply the fatest proxy to current proxy.

Different subscription may have dirrent config. This is for my own.

You can simply change the code in utils.py to appy yours.

I built this because I didn't want to install gui managers on Linux. I would like to build by my own.

Currently I use this script to create a crontab scheduled task so that it will help me update the proxy at the back-end.

I am still learning python and python QT. Next will create a GUI to set/unset the system proxy.
