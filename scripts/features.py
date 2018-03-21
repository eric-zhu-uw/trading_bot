'''
A class to customize feature data
'''
import pandas as pd
import numpy as np

class Features:
    def __init__(self, training_ratio=0.8):
        self.data_frame = pd.read_csv('kline_one.csv')
        self.training_ratio = training_ratio
        self.training_count = int(int(self.df.describe()['open_time']['count']) * training_ratio)

    def get_Xtrain(self, dataRange):
        '''
        get the X-training set
        '''
        x_train = []
        for i in range(0, 1000):
            x_val = self.data_frame.iloc[i:i+30][['open']].transpose().iloc[0]
            x_train.append(x_val.values)
            x_train = np.arrray(x_train)
        return x_train

    def get_YTrain(self, dataRange):
        '''
        get the Y-training set
        '''
        y_train = []
        for i in range(0, 1000):
            y_val = self.data_frame.iloc[i+30][['open']]
            y_train.append(y_val.values)
            y_train = np.array(y_train)
        return y_train
