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
    MODEL = load_model('LSTM_MSE_ADAM_(30,4).h5')
    FILEPATH = 'LSTM_MSE_ADAM_(30,4).hdf5'

    # print feature information
    print FEATURE.get_info()

    #save to file
    CHECKPOINT = ModelCheckpoint(
        FILEPATH,
        monitor='loss',
        verbose=1,
        save_best_only=True,
        mode='mine',
    )
    X_TRAIN = FEATURE.get_x_train()
    Y_TRAIN = FEATURE.get_y_train()

    # training of the model
    MODEL.fit(X_TRAIN, Y_TRAIN, epochs=100, batch_size=64, callbacks=[CHECKPOINT])
    print 'Finished script!'
