import keras,os
from keras.models import Sequential, Model
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten, GlobalAveragePooling2D, Dropout
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.callbacks import ModelCheckpoint, EarlyStopping


## data augumation for train data-check different possibilities 
trdata = ImageDataGenerator(preprocessing_function=preprocess_input,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
traindata = trdata.flow_from_directory(directory="../data/Training",target_size=(224,224)) ##set params
print(traindata)
CLASSES = len(traindata.class_indices) ##get number of classes
i = 0
for batch in trdata.flow(traindata, batch_size=100,
                          save_to_dir='augmented',
                          save_prefix='aug',
                          save_format='png'):    
    i += 1    
    if i > 20:        
        break
## get test data
tsdata = ImageDataGenerator()
testdata = tsdata.flow_from_directory(directory="../data/Test", target_size=(224,224))

# ##load pretrained model without last layer- classifing
base_model = VGG16(weights='imagenet', include_top=False)
print(base_model.summary())

##adding custom layer
x = base_model.output
x = GlobalAveragePooling2D(name='avg_pool')(x)
x = Dropout(0.4)(x)
predictions = Dense(CLASSES, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

##freeze all  base_model layers and train the last ones
for layer in base_model.layers:
    layer.trainable = False

##selecting the optimizer, the loss function, and the metrics- CHECK DIFFERENT PARAMS
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
EPOCHS = 5
BATCH_SIZE = 32
STEPS_PER_EPOCH = 320
VALIDATION_STEPS = 64
MODEL_FILE = 'models/vgg16-pretrained-rmsprop.model'

##to be checked
# checkpoint = ModelCheckpoint("vgg16_1.h5", monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
# early = EarlyStopping(monitor='val_acc', min_delta=0, patience=20, verbose=1, mode='auto')
#

model.save(MODEL_FILE)


