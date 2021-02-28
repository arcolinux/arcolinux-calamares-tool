# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import os
import threading  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))

DEBUG = False

if DEBUG:
    config = "/home/bheffernan/Repos/GITS/HLWM/hefftor-calamares-config-herbstluftwm/calamares-basic/modules/partition.conf"  # noqa
else:
    config = "/etc/calamares/modules/partition.conf"

fs = [
    'btrfs',
    'xfs',
    'jfs',
    'reiser',
    'ext4',
]


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
