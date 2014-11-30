"""
Module to contain all the functions to handle the interaction with the database.
"""

__author__ = 'tmc'

import sqlite3
import flexfoldersync

def getConnection(dirStr = None):
    """
    Function to get a connection to the specified database.
    :param dirStr:
https://www.sqlite.org/datatype3.html
    :return:
      connection to the database
    """

    if dirStr == None:
        dirStr = flexfoldersync.dbPath
    #TODO: Check if the database structure is corret and initialize if empty.
    return sqlite3.connect(dirStr)

def init(conn):
    """
    Initialize the tables needed in the database.
    :param conn:
        Connection to the database to initialize.
    :return:
    """

    #TODO: Create indexes and hash to compare.
    filesInfoTableQry = "CREATE TABLE FilesInfo(pathK TEXT, file_name TEXT, size INT, mtime FLOAT, ctime FLOAT);"
    cur = conn.cursor()
    cur.execute(filesInfoTableQry)
    cur.close()