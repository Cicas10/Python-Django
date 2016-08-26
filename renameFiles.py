import glob
import os

my_path = "/home/cicas/Pictures"
possible_files = os.path.join(my_path, "*.gif")
for file_name in glob.glob(possible_files):
    print('Converting "{}" to JPG...'.format(file_name))
    full_file_name = os.path.join(my_path, file_name)
    new_file_name = full_file_name[0:len(full_file_name) - 4] + ".jpg"
    os.rename(full_file_name, new_file_name)
