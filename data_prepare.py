import subprocess
import os
import random

data_train = '.\\data\Training'
data_train_out = data_train #'.\\data\Aug'



# obliczanie ilości obrazów do wylosowania i ilości rozszerzenia danego obrazu
def count_class_ratio(class_counter, max_counter):
    ratio = class_counter / max_counter * 100
    # zrwarana tablca informacji o liczbie losowanych obrazów i liczbie rozszerzenia danego obrazu
    aug_info = [1, 1]
    temp_aug = 0
    temp_img_cnt = 0
    temp = max_counter - class_counter

    # zaszumienie danych trninigowych przez dodatkowe rozszerzenie danych (15%) - dla klas o ratio >90
    if ratio > 90 and class_counter <1000:
        temp = int(0.15 * class_counter)
        # ilość losowanych obrazów z rozszerzeniem 5
        temp_img_cnt = int(temp / 5)
        temp_aug = 5;
    elif ratio > 70:
        temp_img_cnt = int(temp / 10)
        temp_aug = 10
    elif ratio > 50:
        temp_img_cnt = int(temp / 15)
        temp_aug = 15
    elif ratio > 30:
        temp_img_cnt = int(temp / 20)
        temp_aug = 20
    else:
        temp_img_cnt = int(temp / 25) + 1
        temp_aug = 25


    aug_info[0] = temp_img_cnt
    aug_info[1] = temp_aug

    return aug_info

#losowanie obrazu do rozszerzenia i rozszerzenie obrazów
def prepare_data_aug( aug_info, cls, dir_in, dir_out):
    class_path = os.path.join(dir_in,cls)
    list_img = list(os.listdir(class_path))

    print(os.path.join(dir_out,cls),": random img cnt: ", aug_info[0]," aug: ", aug_info[1])
    for i in range(aug_info[0]):
        random_img = random.choice(list_img)
        #zabezpieczenie przed wylosowaniem już rozszerzonego obrazu
        while str(random_img).count("image"):
            print("Nowe losowanie",random_img)
            random_img = random.choice(list_img)
        imp_path = os.path.join(class_path,random_img)
        #print(random_img)
        subprocess.check_output(['py', 'src\data_augmation.py', '-i', imp_path, '-o', os.path.join(dir_out,cls), '-t ' + str(aug_info[1])])  # Just run the program




list_dir = list(os.listdir(path=data_train))
if os.path.exists(data_train_out) == False:
    os.mkdir(data_train_out)

max_classes_counter = 0;
classes = [[0 for col in range(2)] for row in range(len(list_dir))]
tab = [["" for col in range(2)] for row in range(10)]
#print (os.path.join(data_train,list_dir[1]))
i=0;

## sprawdzanie ilości danych treningowych dla równych klas
for subfiles in list_dir:
    #print(subfiles)
    list_subfile =list(os.listdir(path=os.path.join(data_train,subfiles)))
    #dodawanie do tablicy klasy i liczby danych treningowych
    classes[i][0] = subfiles
    classes[i][1] = len(list_subfile)
    i=i+1;
    #sprawdzanie maksymalnej liczby danych treningowych
    if len(list_subfile) > max_classes_counter:
        max_classes_counter =len(list_subfile)

print("Najwiksza liczba obrazów: ",max_classes_counter)
#print(classes)

#rozszerzenie danych dla przybliżonej loczby danych dla kazdej klasy
for subfiles,counter_classes in classes:
    if os.path.exists(os.path.join(data_train_out, subfiles))==False:
        os.mkdir(os.path.join(data_train_out,subfiles));

    aug_info = count_class_ratio(counter_classes, max_classes_counter)
    print("Ilość obrazów dla klasy przed rozszerzeniem: ",counter_classes)
    prepare_data_aug(aug_info,subfiles, data_train, data_train_out)
    print(aug_info)








