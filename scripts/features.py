'''
A class to customize feature data
'''
import pandas as pd
import numpy as np

class Features:
    # pylint: disable=too-many-instance-attributes
    def __init__(self, **kwargs):
        self.csv_file = 'kline_one.csv'
        self.training_ratio = 0.8
        self.simple_moving_average = False
        self.interval_size = 30
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.data_frame = pd.read_csv(self.csv_file)
        self.count = int(self.data_frame.describe()['open_time']['count'])
        self.training_count = int(self.count * self.training_ratio)
        self.long_sma = self.interval_size
        self.mid_sma = int(self.interval_size/2)
        self.short_sma = int(self.interval_size/4)

    def get_info(self):
        return {
            'csv_file': self.csv_file,
            'training_ratio': self.training_ratio,
            'count': self.count,
            'training_count': self.training_count,
            'simple_moving_average': self.simple_moving_average,
            'interval_size': self.interval_size
        }

    def validate_chronological(self):
        prev_open_time = 0
        for i, row in self.data_frame.iterrows():
            if row['open_time'] < prev_open_time:
                return False
            prev_open_time = row['open_time']
        return True


    def get_x_train(self, data_range=None):
        '''
        get the X-training set
        '''
        if data_range is None:
            data_range = self.training_count

        int_size = self.interval_size

        x_train = []
        for i in range(int_size, int_size+data_range):
            open_price = self.data_frame.iloc[i:i+int_size][['open']].transpose().iloc[0]
            x_val = open_price.values.tolist()
            x_train.append(x_val)

            if self.simple_moving_average:
                sma = []
                lsma = self.long_sma
                msma = self.mid_sma
                ssma = self.short_sma

                for j in range(i, i+int_size):
                    close = self.data_frame.iloc[j-int_size:j][['close']].transpose().iloc[0]
                    close = close.values

                    long_sma = sum(close) / lsma
                    mid_sma = sum(close[lsma - msma-1:-1]) / msma
                    short_sma = sum(close[lsma - ssma-1:-1]) / ssma
                    sma.extend([long_sma, mid_sma, short_sma])
                x_train[-1].extend(sma)

        return np.array(x_train)

    def get_y_train(self, dataRange=None):
        '''
        get the Y-training set
        '''
        if dataRange is None:
            dataRange = self.training_count

        y_train = []
        for i in range(0, 1000):
            y_val = self.data_frame.iloc[i+30][['open']]
            y_train.append(y_val.values)
        y_train = np.array(y_train)
        return y_train
