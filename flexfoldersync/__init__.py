__author__ = 'tmc'

import os

def getFilesInfo(dirStr, mask=None):
    """
    Get all files and information used to compare the files

    Will use os.walk to iterate all the files, ignoring the directories.
    :param dirStr:
    :return:
        array containing the path, file name, size, modification time and creation time.
    """
    result = []
    for root, dirs, files in os.walk(dirStr):
        # ignoring directories
        for f in files:
            stats = os.stat(os.path.join(root,f))
            result.append([root, f, stats.st_size, stats.st_mtime, stats.st_ctime])
    return result