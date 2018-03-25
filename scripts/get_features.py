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
    for i in range(size, count-size-1):
        x_val = df.iloc[i:i+size][raw_features].transpose().values
        high = ''
        low = ''
        close = ''
        total_quote_volume = ''
        buy_quote_volume = ''
        buy_base_volume = ''
        num_trades = ''
        rsi = ''
        mfi = ''
        proc = ''
        lsma = ''
        ssma = ''
        y = ''

        for j in range(size):
            high += '%.5f' % x_val[0][j] + ' '
            low += '%.5f' % x_val[1][j] + ' '
            close += '%.5f' % x_val[2][j] + ' '
            total_quote_volume += '%.5f' % x_val[3][j] + ' '
            buy_quote_volume += '%.5f' % x_val[4][j] + ' '
            buy_base_volume += '%.5f' % x_val[5][j] + ' '
            num_trades += '%.5f' % x_val[6][j] + ' '

        x_val = df.iloc[i-size:i]['close'].transpose().values.tolist()
        for j in range(size):
            lsma += '%.5f' % (sum(x_val)/size) + ' '
            x_val.pop(0)
            x_val.append(df.iloc[i+j]['close'])

        x_val = df.iloc[i-(size/3):i]['close'].transpose().values.tolist()
        for j in range(size):
            ssma += '%.5f' % (sum(x_val)/(size/3)) + ' '
            proc += '%.5f' % (100 * ((x_val[(size/3)-1] - x_val[0]) / x_val[0])) + ' '
            x_val.pop(0)
            x_val.append(df.iloc[i+j]['close'])

        x_val = df.iloc[i-size:i]['close'].transpose().values.tolist()
        for j in range(size):
            gains_avg = 0
            losses_avg = 0
            start = 0
            end = 1
            rel_strength = 0
            while end < size:
                diff = x_val[end] - x_val[start]
                if diff > 0:
                    gains_avg += diff
                else:
                    losses_avg += abs(diff)
                start += 1
                end += 1
            if losses_avg == 0:
                rel_strength = 9
            else:
                rel_strength = gains_avg/losses_avg

            rsi += '%.5f' % (100-(100/(1+rel_strength))) + ' '
            x_val.pop(0)
            x_val.append(df.iloc[i+j]['close'])

        x_val = df.iloc[i-size:i][['taker_buy_quote_asset_volume', 'total_quote_asset_volume']].transpose().values.tolist()
        for j in range(size):
            bqv = sum(x_val[0])
            tqv = sum(x_val[1])
            if tqv == 0:
                mfr = 1
            elif tqv == bqv:
                mfr = 9
            else:
                mfr = bqv/(tqv-bqv)

            mfi += '%.5f' %  (100-(100/(1+mfr))) + ' '
            x_val[0].pop(0)
            x_val[1].pop(0)
            x_val[0].append(df.iloc[i+j]['taker_buy_quote_asset_volume'])
            x_val[1].append(df.iloc[i+j]['total_quote_asset_volume'])

        closing_price = sum(df.iloc[i+size-1][['close']].transpose().values)
        next_kline_avg = sum(df.iloc[i+size][['close', 'high', 'low']].transpose().values)/3
        if closing_price < next_kline_avg:
            y = 1
        else:
            y = 0

        TableName.create(
            rsi=rsi,
            mfi=mfi,
            proc=proc,
            total_quote_volume=total_quote_volume,
            buy_quote_volume=buy_quote_volume,
            buy_base_volume=buy_base_volume,
            high=high,
            low=low,
            close=close,
            lsma=lsma,
            ssma=ssma,
            num_trades=num_trades,
            y=y
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
