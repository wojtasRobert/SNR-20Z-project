import os
import shutil
import random

sample_ratio = 0.85

# dirs for LessClass case
dir_validation = '.\\data\\LessClasses\\Validation'
dir_training = '.\\data\\LessClasses\\Training'

# dirs for full-class case
# dir_validation = '.\\data\\Validation'
# dir_training = '.\\data\\Training'

for d in os.listdir(dir_training):
    print('Extracting validation data from... ', d)    
    
    train_dirfile = os.path.join(dir_training, d)   
    val_dirfile = os.path.join(dir_validation, d)
    if not os.path.exists(val_dirfile):
        os.makedirs(val_dirfile) 
    
    train_idx = set(random.sample(list(range(len(os.listdir(train_dirfile)))),
                              int(sample_ratio*len(os.listdir(train_dirfile)))))
    val_files = [n for i,n in enumerate(os.listdir(train_dirfile)) if i not in train_idx]
    
    for file in val_files:
        file_path = os.path.join(train_dirfile, file)
        shutil.move(file_path, val_dirfile)
    

