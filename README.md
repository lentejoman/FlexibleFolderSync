Script to compare and syncronize to collections of files being flexible enought to allow for different folder structure.

ROADMAP:
--------

* First develop command line tool, and maybe some day user interface.

TODO:

1. Tool to create an sqlite database with the different files:
  Information: path, date created, date modified, sha1.
  1.1 Use as the starting point a previously created database, update only modified Files.

FEATURES:
---------

- Remember deleted files.
- Detect moved files.
- Compare different file types differently (instead of solelly relying on the sha1 hash).