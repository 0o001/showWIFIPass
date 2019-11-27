import os
import re

__author__ = "mustafauzun0"

"""
SHOWWIFIPASS
"""

if __name__ == "__main__":
    readWIFIProfiles = os.popen("netsh wlan show profiles").read()

    for profile in re.findall(r"All User Profile\s+:\s(.*)", readWIFIProfiles):
        readWIFIProfile = os.popen("netsh wlan show profile name=" + profile + " key=clear").read()
        showWIFIPassword = re.search(r"Key Content\s+:\s(.*)", readWIFIProfile).groups()[0]

        print("Name:", profile)
        print("Password:", showWIFIPassword)