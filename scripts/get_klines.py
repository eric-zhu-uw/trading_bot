'''
populate mysql database with kline data from Binance
'''
import datetime
from binance.client import Client
from create_klines_schema import Kline1, Kline3, Kline5, Kline15, Kline30, Kline1_Mar1_Mar30
from constants import (
    ETH_USDT,
    MARCH_1_2018_12AM,
    MARCH_30_2018_12AM,
    MINUTE,
    KLINE_INTERVAL_MAR1_MAR30
)

def get_klines(symbol, kline_interval, start_time, end_time):
    '''
    get_klines
    '''
    client = Client('', '')
    if client.ping() == {}:
        print 'Binance Connection Successful!'

    # default parameters
    limit = 500
    interval = client.KLINE_INTERVAL_1MINUTE
    KlineModel = Kline1


    # update parameters depending on interval
    if kline_interval == 3:
        KlineModel = Kline3
        interval = client.KLINE_INTERVAL_3MINUTE
    elif kline_interval == 5:
        KlineModel = Kline5
        interval = client.KLINE_INTERVAL_5MINUTE
    elif kline_interval == 15:
        KlineModel = Kline15
        interval = client.KLINE_INTERVAL_15MINUTE
    elif kline_interval == 30:
        KlineModel = Kline30
        interval = client.KLINE_INTERVAL_30MINUTE
    elif kline_interval == KLINE_INTERVAL_MAR1_MAR30:
        KlineModel = Kline1_Mar1_Mar30
        interval = client.KLINE_INTERVAL_1MINUTE
        kline_interval = 1

    time_between_start_time = kline_interval * limit * MINUTE

    while start_time < end_time:
        try:
            klines = client.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=start_time
            )
        except Exception as e:
            with open('error.log', 'a') as f:
                f.write('========================================\n')
                f.write(str(e) + '\n')
                f.write('Failed At Timestamp: ' + str(start_time) + ' on api request\n')
                f.write('Failing Time: ' + str(datetime.datetime.now()) + '\n')
                f.close()
                exit()

        for k in klines:
            try:
                KlineModel.create(
                    open_time=k[0],
                    open=float(k[1]),
                    high=float(k[2]),
                    low=float(k[3]),
                    close=float(k[4]),
                    volume=float(k[5]),
                    close_time=k[6],
                    total_quote_asset_volume=float(k[7]),
                    num_of_trades=k[8],
                    taker_buy_base_asset_volume=float(k[9]),
                    taker_buy_quote_asset_volume=float(k[10])
                ).save()
            except Exception as e:
                with open('error.log', 'a') as f:
                    print e
                    f.write('========================================\n')
                    f.write(str(e) + '\n')
                    f.write('Failed At Timestamp: ' + str(k[0]) + ' on insert\n')
                    f.write('Failing Time: ' + str(datetime.datetime.now()) + '\n')
                    f.close()
                    exit()

        with open('success.log', 'a') as f:
            f.write('========================================\n')
            f.write('Finished : [' + str(start_time) + ', ' +
                    str(start_time + time_between_start_time) + ']\n')
            f.write('Passed Time: ' + str(datetime.datetime.now()) + '\n')
            f.close()

        start_time = start_time + time_between_start_time

if __name__ == "__main__":
    get_klines(ETH_USDT, KLINE_INTERVAL_MAR1_MAR30, MARCH_1_2018_12AM, MARCH_30_2018_12AM)
    print 'Finished script!'
