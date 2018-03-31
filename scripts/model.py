'''
defining the machine learning model
'''
# pylint: disable=E0401
# pylint: disable=W0403
from keras.models import Sequential
from keras.layers import Dense, LSTM

MODEL = Sequential()
MODEL.add(LSTM(6, input_shape=(10, 12)))
MODEL.add(Dense(1, activation='sigmoid'))
MODEL.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print "/=== View Model Definition ===/"
for i, layer in enumerate(MODEL.layers):
    print "--------"
    print "Layer " + str(i)
    print "--------"
    print layer.get_config()

MODEL.save('model_1.h5')
print 'Finished script!'
