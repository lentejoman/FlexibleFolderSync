__author__ = 'tmc'

import os

#Path to the default database wher to store the information about the files.
#TODO: Take this from the configuration file.
dbPath = os.path.join(os.path.expanduser("~"),"flxfolder.info")

def getFilesInfo(dirStr, mask=None):
    """
    Get all files and information used to compare the files

    Will use os.walk to iterate all the files, ignoring the directories.
    :param dirStr:
        Starting directory to search for files.
    :return:
        array containing the path, file name, size, modification time and creation time as returned by os.stat()
    TODO:
        Implement the filter by the given mask, investigate:
            http://bytes.com/topic/python/answers/585607-more-efficient-fnmatch-fnmatch-multiple-patterns
            fnmatch module.
    """
    result = []
    for root, dirs, files in os.walk(dirStr):
        # ignoring directories as specified...
        for f in files:
            stats = os.stat(os.path.join(root,f))
            result.append([root, f, stats.st_size, stats.st_mtime, stats.st_ctime])
    return result

#TODO: Implement function to save the file information into a database.
#TODO: Implement function to calculate the hashes of the files for the given database (detect when files have changed).