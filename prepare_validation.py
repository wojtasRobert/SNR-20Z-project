import numpy as np
import os
import shutil

validation_path = "data\\Validation"
test_path = "data\\Test"
if not os.path.exists(validation_path):
    os.mkdir(validation_path)

# Do something with the files
for filename in os.listdir(test_path):
        print() ##maybe some loading
        full_file_name = os.path.join(test_path, filename)
        full_new_filename = os.path.join(validation_path, filename)
        files = os.listdir(full_file_name)
        # Select 0.5 of the files randomly  
        random_files = np.random.choice(files, int(len(files)*.5))
        # Get the remaining files
        other_files = [x for x in files if x not in random_files]
        os.mkdir(full_new_filename)
        for x in random_files:
            print(x)
            # shutil.move(os.path.join(full_file_name,x),os.path.join(full_new_filename,x)) 