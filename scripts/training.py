'''
model training
'''
from keras.models import Sequential, load_model
from keras.layers import Dense
import pandas as pd
import numpy as np

# create and saving weights
from keras.callbacks import ModelCheckpoint

df = pd.read_csv('kline_one.csv')

count = int(df.describe()['open_time']['count'])
training_count = int(count * 0.8)
print 'The number of rows is: ', count
print 'The training count indices are: [0,' + str(training_count-1) + ']'
print 'The testing count indicies are: [' + str(training_count) + ',' + str(count-1) + ']'

X_train = []
Y_train = []

for i in range(0, 1000):
    X_val = df.iloc[i:i+30][['open']].transpose().iloc[0]
    # print X_val.values
    X_train.append(X_val.values)

    Y_val = df.iloc[i+30][['open']]
    # print Y_val.values
    Y_train.append(Y_val.values)

X_train = np.array(X_train)
Y_train = np.array(Y_train)

# print X_train
# print Y_train

# model = Sequential()
model = load_model('model.h5')

# adding input layer and current layer
# defining the model

filepath = 'somename.hdf5'

#save to file
checkpoint = ModelCheckpoint(
    filepath,
    monitor='loss',
    verbose=1,
    save_best_only=True,
    mode='mine',
)

# save best thetas for next epoch
callbacks = [checkpoint]

# training of the model
model.fit(X_train, Y_train, epochs=100, batch_size=64, callbacks=callbacks)

#finished training and don't want to retrain
# save the weights are already saved into the <somename.hdf5> so you don't wanna retrain
# model.load_weights('somename.hdf5')
# model.evaluate()
## input vector sequence in same format and get result
# model.predict()
