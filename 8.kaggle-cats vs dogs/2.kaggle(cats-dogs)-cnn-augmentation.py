#dropout and data-augmentation to reduce overfitting

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten, Dense, Dropout
from keras import backend as K
#import collections
import os
import pandas as pd
import shutil
from keras.models import load_model



import sys
sys.path.append('C:\\Users\\prana\\Documents\\GitHub\\deep-learning\\2018-feb\\utils')

import utils
from keras.callbacks import ModelCheckpoint, EarlyStopping

train_dir, validation_dir, test_dir, nb_train_samples, nb_validation_samples,nb_test_samples = \
                    utils.preapare_small_dataset_for_flow(
                            train_dir_original='C:\\Users\\prana\\Downloads\\Deep_Learning_Data\\train\\train', 
                            test_dir_original='C:\\Users\\prana\\Downloads\\Deep_Learning_Data\\test1\\test1',
                            target_base_dir='C:\\Users\\prana\\Downloads\\Deep_Learning_Data\\data')

img_width, img_height = 150, 150
epochs = 100
batch_size = 20

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
    
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu',input_shape=input_shape))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))
print(model.summary())

model.compile(loss='binary_crossentropy', 
              optimizer='adam',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

early_stopping = EarlyStopping(monitor='val_loss', patience=3, verbose=1, mode='auto')   
save_weights = ModelCheckpoint('model.h5', monitor='val_loss', save_best_only=True)

history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples//batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples//batch_size,
    callbacks=[save_weights, early_stopping])

historydf = pd.DataFrame(history.history, index=history.epoch)

utils.plot_loss_accuracy(history)

test_datagen = ImageDataGenerator(rescale=1. / 255)
test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)
#print(test_generator.filenames)
probabilities = model.predict_generator(test_generator, nb_test_samples//batch_size)

mapper = {}
i = 0
for file in test_generator.filenames:
    id = int(file.split('\\')[1].split('.')[0])
    mapper[id] = probabilities[i][1]
    i += 1
#od = collections.OrderedDict(sorted(mapper.items()))    
tmp = pd.DataFrame({'id':list(mapper.keys()),'label':list(mapper.values())})    
tmp.to_csv('submission.csv', columns=['id','label'], index=False)



target_base_dir='C:\\Users\\prana\\Downloads\\Deep_Learning_Data\\data'
results_dir = os.path.join(target_base_dir, 'results')
os.mkdir(results_dir)

results_cat_dir = os.path.join(results_dir, 'cats')
os.mkdir(results_cat_dir)

results_dog_dir = os.path.join(results_dir, 'dogs')
os.mkdir(results_dog_dir)