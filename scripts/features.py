'''
A class to customize feature data
'''
import pandas as pd
import numpy as np

class Features:
    def __init__(self, training_ratio=0.8):
        self.data_frame = pd.read_csv('kline_one.csv')
        self.training_ratio = training_ratio
        self.count = int(self.data_frame.describe()['open_time']['count'])
        self.training_count = int(self.count * training_ratio)

    def get_info(self):
        return {
            'training_ratio': self.training_ratio,
            'count': self.count,
            'training_count': self.training_count
        }

    def get_x_train(self, dataRange=0):
        '''
        get the X-training set
        '''
        x_train = []
        for i in range(0, 1000):
            x_val = self.data_frame.iloc[i:i+30][['open']].transpose().iloc[0]
            x_train.append(x_val.values)
        x_train = np.array(x_train)
        return x_train

    def get_y_train(self, dataRange=0):
        '''
        get the Y-training set
        '''
        y_train = []
        for i in range(0, 1000):
            y_val = self.data_frame.iloc[i+30][['open']]
            y_train.append(y_val.values)
        y_train = np.array(y_train)
        return y_train
