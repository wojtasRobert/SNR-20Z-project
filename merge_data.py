import os
import shutil

dirs = ['.\\data\\Test', '.\\data\\Training']

new_dir = '.\\data\All'

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
for dir_single in dirs:
    for filename in os.listdir(dir_single):
        print(filename) ##maybe some loading
        full_file_name = os.path.join(dir_single, filename)
        new_dirfile = os.path.join(new_dir, filename)
        copytree(full_file_name, new_dirfile)
        
