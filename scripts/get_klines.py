'''
get_klines
'''

import datetime
from binance.client import Client
from create_klines_schema import *
import constants    #figure out how to clean up

def get_klines(TableName, interval, start_time=constants.START_DATE):
    '''
    get_klines
    '''
    client = Client('', '')
    if client.ping() == {}:
        print 'Binance Connection Successful!'

    while start_time < constants.END_DATE:
        try:
            klines = client.get_klines(
                symbol=constants.ETH_USDT,
                interval=interval,
                limit=500,
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
                TableName.create(
                    open_time=k[0],
                    open=float(k[1]),
                    high=float(k[2]),
                    low=float(k[3]),
                    close=float(k[4]),
                    volume=float(k[5]),
                    close_time=k[6],
                    quote_asset_volume=float(k[7]),
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
                    str(start_time + (500 * constants.MINUTE)) + ']\n')
            f.write('Passed Time: ' + str(datetime.datetime.now()) + '\n')
            f.close()

        start_time = start_time + (2500 * constants.MINUTE)

if __name__ == "__main__":
    get_klines(KlineFive, Client.KLINE_INTERVAL_5MINUTE, 1515076800000 + (5 * constants.MINUTE))
    print 'Finished script!'
