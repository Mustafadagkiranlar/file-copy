import shutil
import os
import sys

file_loc = str(input('Enter the file location: '))
copy_to = str(input('Where to copy the file: ')) 

shutil.copy(file_loc, copy_to)
