'''
model training
'''
# pylint: disable=E0401
# pylint: disable=W0403
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy as np
from constants import FEATURES_INT10, INTERVAL10, Features, TRAINING_RATIO, FEATURES_INT10_MAR1_MAR30
from create_feature_info_schema import FeatureInfo

def train_model(table_name, model_name, interval_size, train=True, test=True):
    df = pd.read_csv(table_name + '.csv')
    training_count = int(int(df.describe()['id']['count']) * TRAINING_RATIO)
    testing_count = int(df.describe()['id']['count'])
    feature_info = {}

    for key in Features:
        query = FeatureInfo.select().where(
            (FeatureInfo.table_name == table_name) &
            (FeatureInfo.feature_name == Features[key]))

        for result in query:
            feature_info[Features[key]] = result

    feature_names = list(df)
    feature_names.remove('id')
    feature_names.remove('y')

    # randomize training rows
    df = df.sample(frac=1).reset_index(drop=True)

    # =========================================================
    if train:
        print '/=== TRAINING ===/'
        x_train = []
        y_train = []

        for i in range(training_count):
            x_val = df.iloc[i].drop(['id', 'y']).values.tolist()
            y_val = df.iloc[i]['y']

            # MOVE ALL OF THIS TO A SEPARATE HELPER FN

            x_columns = []
            for j, feature in enumerate(x_val):
                feature_interval = feature.split(' ')
                if len(feature_interval) != interval_size:
                    feature_interval.pop()
                feature_interval = map(lambda x: (float(x)-feature_info[feature_names[j]].min)/(feature_info[feature_names[j]].max-feature_info[feature_names[j]].min), feature_interval)
                x_columns.append(feature_interval)

            # turn to 2d array to be transposed
            x_columns = np.array(x_columns)

            # (interval size x number of features) = (m x n)
            x_columns = np.transpose(x_columns)

            x_train.append(x_columns)
            y_train.append(y_val)

        model = load_model(model_name + ".h5")
        filepath = model_name + '.hdf5'

        #save to file
        checkpoint = ModelCheckpoint(
            filepath,
            monitor='loss',
            verbose=1,
            save_best_only=True,
            mode='mine',
        )

        x_train = np.reshape(x_train, (training_count, 10, 12))
        y_train = np.array(y_train)

        # training of the model
        model.fit(x_train, y_train, epochs=150, batch_size=32, callbacks=[checkpoint])

        # free up memory
        x_train = []
        y_train = []

    # ===========================================================================

    if test:
        print '/=== TESTING ===/'
        x_test = []
        y_test = []

        for i in range(0, testing_count):
            x_val = df.iloc[i].drop(['id', 'y']).values.tolist()
            y_val = df.iloc[i]['y']

            # MOVE ALL OF THIS TO A SEPARATE HELPER FN

            x_columns = []
            for j, feature in enumerate(x_val):
                feature_interval = feature.split(' ')
                if len(feature_interval) != interval_size:
                    feature_interval.pop()
                feature_interval = map(lambda x: (float(x)-feature_info[feature_names[j]].min)/(feature_info[feature_names[j]].max-feature_info[feature_names[j]].min), feature_interval)
                x_columns.append(feature_interval)

            # turn to 2d array to be transposed
            x_columns = np.array(x_columns)

            # (interval size x number of features) = (m x n)
            x_columns = np.transpose(x_columns)

            x_test.append(x_columns)
            y_test.append(y_val)

        x_test = np.reshape(x_test, (testing_count, 10, 12))
        y_test = np.array(y_test)

        filepath = model_name + '.hdf5'
        model = load_model(model_name + '.h5')
        model.load_weights(filepath, by_name=False)

        # testing the model
        score = model.evaluate(x_test, y_test, verbose=1)
        print score
        print 'LOSS: ' + str(score[0])
        print 'ACCURACY: ' + str(score[1])

if __name__ == "__main__":
    train_model(FEATURES_INT10_MAR1_MAR30, 'model_1', INTERVAL10, train=False)
    print 'Finished script!'
