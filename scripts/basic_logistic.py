'''
model training
'''
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np

# create and saving weights
from keras.callbacks import ModelCheckpoint

df = pd.read_csv('kline_one.csv')
print df[1:10]
exit()

# data.split(',') # 3,4,5,6,7 -> [3,4,5,6,7]

model = Sequential()

# adding input layer and current layer
model.add(Dense(40, input_shape=(50,)))
model.add(Dense(1, activation='sigmoid'))

# defining the model
model.compile(loss='binary_crossentropy', optimizer='adam')

filepath = 'somename.hdf5'

#save to file
checkpoint = ModelCheckpoint(filepath, monitor='losee', verbose=1, save_best_only=True, mode='mine')

# save best thetas for next epoch
callbacks = [checkpoint]

# training of the model
model.fit(X_train, Y_train, epoch=100, batch_size=64, callbacks=callbacks_list)

#finished training and don't want to retrain
# save the weights are already saved into the <somename.hdf5> so you don't wanna retrain
model.load_weights('somename.hdf5')

## input vector sequence in same format and get result
# model.predict()
