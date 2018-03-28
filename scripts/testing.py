
#finished training and don't want to retrain
# save the weights are already saved into the <somename.hdf5> so you don't wanna retrain
# model.load_weights('somename.hdf5')
## input vector sequence in same format and get result
# model.predict()

'''
model training
'''
from keras.models import Sequential, load_model
from keras.layers import Dense
import pandas as pd
import numpy as np
from features import Features

# create and saving weights
from keras.callbacks import ModelCheckpoint

if __name__ == "__main__":
    FEATURE = Features(simple_moving_average=True)
    FILEPATH = 'somename.hdf5'
    MODEL = load_model('model.h5')
    MODEL.load_weights(FILEPATH, by_name=False)

    # print feature information
    print FEATURE.get_info()

    X_TEST = FEATURE.get_x_test(data_range=1000)
    Y_TEST = FEATURE.get_y_test(data_range=1000)

    # testing the model
    score = MODEL.evaluate(X_TEST, Y_TEST, verbose=1)
    print score
    print 'Finished script!'
