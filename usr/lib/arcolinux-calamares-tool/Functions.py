# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import os
import threading  # noqa
import subprocess

base_dir = os.path.dirname(os.path.realpath(__file__))

proc = subprocess.Popen(["who"], stdout=subprocess.PIPE, shell=True, executable='/bin/bash') # noqa
users = proc.stdout.readlines()[0].decode().strip().split(" ")[0]
print(users)
DEBUG = False

if DEBUG:
    config = "/home/bheffernan/Repos/GITS/HLWM/hefftor-calamares-config-herbstluftwm/calamares-basic/modules/partition.conf"  # noqa
    liveuser = users
else:
    config = "/etc/calamares/modules/partition.conf"
    liveuser = "liveuser"

fs = [
    'btrfs',
    'ext4',
    'f2fs',
    'jfs'
]

message = "Sorry, This tool is only for the live ISO to make changes to Calamares Installer"  # noqa


def __get_position(lists, string):
    data = [x for x in lists if string in x]
    pos = lists.index(data[0])
    return pos


def set_config(string):
    with open(config, "r") as f:
        lines = f.readlines()
        f.close()

    pos = __get_position(lines, "defaultFileSystemType:")

    lines[pos] = "defaultFileSystemType:  \"" + string + "\"\n"

    with open(config, "w") as f:
        f.writelines(lines)
        f.close()
