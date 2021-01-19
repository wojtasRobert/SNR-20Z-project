# script for

import os
import shutil

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

chosen_classes = ['Lemon',
                  'Raspberry',
                  'Mandarine',
                  'Pear 2',
                  'Apple Red 1',
                  'Strawberry',
                  'Pomegranate',
                  'Pepino',
                  'Kaki',
                  'Apricot',
                  'Ginger Root',
                  'Huckleberry']

# some dirs
dir_test = '.\\data\\Test'
dir_training = '.\\data\\Training'
new_dir = '.\\data\\LessClasses'
new_dir_training = '.\\data\\LessClasses\\Training'
new_dir_test = '.\\data\\LessClasses\\Test'

# Training
for cl_dir in chosen_classes:
    full_file_name = os.path.join(dir_training, cl_dir)
    print('Copying Training: ', full_file_name)
    new_dirfile = os.path.join(new_dir_training, cl_dir)
    copytree(full_file_name, new_dirfile)

# Test
for cl_dir in chosen_classes:
    full_file_name = os.path.join(dir_test, cl_dir)
    print('Copying Test: ', full_file_name)
    new_dirfile = os.path.join(new_dir_test, cl_dir)
    copytree(full_file_name, new_dirfile)
