'''
defining the machine learning model
'''
from keras.models import Sequential, load_model
from keras.layers import Dense

model = Sequential()
model.add(Dense(15, input_shape=(30,)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

print "===// View Model Definition //==="
for i, layer in enumerate(model.layers):
    print "--------"
    print "Layer " + str(i)
    print "--------"
    print layer.get_config()

model.save('model.h5')
