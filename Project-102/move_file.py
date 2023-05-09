import os
import shutil

from_dir = 'C:/Users/atomi/Downloads'
to_dir = 'V:/WhitehatJR/Project-102-moved files'

print_dir = os.listdir(from_dir)

path2 = to_dir + '/' + 'Project-102-files'  # Define path2 outside the loop

for file in print_dir:
    name, extension = os.path.splitext(file)
    if extension == ' ':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file
        path3 = path2 + '/' + file  # Update path2 inside this block
        if os.path.exists(path2):
            print("Moving " + file + '...')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file + '...')
            shutil.move(path1, path3)