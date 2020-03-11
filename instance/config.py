# flask config

import os

#grab the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving the actual key outside of the source code under version control

class Config(object):
    SECRET_KEY = '\xd3\xde\x052\x08F_\x18E\xf6\x10,6\xe2\x08\x1df\xf7\xe9I\xfdz\xc7\xe1'
    DEBUG = True