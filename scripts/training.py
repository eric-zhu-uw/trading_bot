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
    FEATURE = Features()
    MODEL = load_model('model.h5')
    FILEPATH = 'somename.hdf5'

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
