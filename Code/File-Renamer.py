# Renames files to a more readable name format
# Will need more work once being used on full dataset
# For use in full dataset, decompress every file and add them to the same location
# Use this to rename all files automatically
# Then, store all storms of the same year in their own place

import os
from os import listdir
import sys


# Path used for listdir method. Directory used to join paths in for loop
path = "C:\\Users\\chens\\Documents\\TestFold"
directory = "C:/Users/chens/Documents/TestFold"

# For loop goes through folder to rename every file in it
for f in listdir(path):
    old_file = os.path.join(directory, f)
    tmp_name_holder = f.split('.')
    file_name = ".".join(tmp_name_holder[1:6])
    full_file_name = file_name + ".nc"
    new_file = os.path.join(directory, full_file_name)
    os.rename(old_file, new_file)
    print(full_file_name)

    # os.rename(full_name_path,file_name)




