'''
populate mysql database with all feature fields filled out
will trim all invalid entries
create multiple different datasets
'''
from create_features_schema import FeaturesInt10
import constants
import pandas as pd
import numpy as np

def get_features(TableName, df, size):
    '''
    get features and insert them into the TableName
    '''
    count = int(df.describe()['open_time']['count'])
    raw_features = [
        'high', 'low', 'close', 'total_quote_asset_volume',
        'taker_buy_quote_asset_volume', 'taker_buy_base_asset_volume',
        'num_of_trades'
    ]
    for i in range(size, size+1):
        x_val = df.iloc[i:i+size][raw_features].transpose().values
        high = ''
        low = ''
        close = ''
        total_quote_volume = ''
        buy_quote_volume = ''
        buy_base_volume = ''
        num_trades = ''

        for i in range(size):
            high += '%.5f' % x_val[0][i] + ' '
            low += '%.5f' % x_val[1][i] + ' '
            close += '%.5f' % x_val[2][i] + ' '
            total_quote_volume += '%.5f' % x_val[3][i] + ' '
            buy_quote_volume += '%.5f' % x_val[4][i] + ' '
            buy_base_volume += '%.5f' % x_val[5][i] + ' '
            num_trades += '%.5f' % x_val[6][i] + ' '

    TableName.create(
        rsi=0,
        mfi=0,
        proc=0,
        total_quote_volume=total_quote_volume,
        buy_quote_volume=buy_quote_volume,
        buy_base_volume=buy_base_volume,
        high=high,
        low=low,
        close=close,
        lsma=0,
        ssma=0,
        num_trades=num_trades,
    ).save()

def validate_chronological(self, df):
    prev_open_time = 0
    for i, row in df.iterrows():
        if row['open_time'] < prev_open_time:
            return False
        prev_open_time = row['open_time']
    return True


if __name__ == "__main__":
    DF = pd.read_csv('kline_one.csv')
    get_features(FeaturesInt10, DF, 10)
    print 'Finished script!'
