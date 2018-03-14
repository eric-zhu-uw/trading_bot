'''
get_klines
'''

import time
from boto3 import resource
from binance.client import Client
import constants    #figure out how to clean up

def get_klines():
    '''
    get_klines
    '''
    client = Client('', '')
    dynamodb_resource = resource('dynamodb')
    table = dynamodb_resource.Table('OneMinute')
    start_time = constants.START_DATE
    print client.ping()

    while start_time < constants.END_DATE:
        klines = client.get_klines(
            symbol=constants.ETH_USDT,
            interval=Client.KLINE_INTERVAL_1MINUTE,
            limit=500,
            startTime=start_time
        )

        for kline in klines:

            row = {}
            row[constants.OPEN_TIME] = kline[0]
            row[constants.OPEN] = kline[1]
            row[constants.HIGH] = kline[2]
            row[constants.LOW] = kline[3]
            row[constants.CLOSE] = kline[4]
            row[constants.VOLUME] = kline[5]
            row[constants.CLOSE_TIME] = kline[6]
            row[constants.NUM_TRADES] = kline[7]
            row[constants.TAKER_BUY_BASE_ASSET_VOLUME] = kline[8]
            row[constants.TAKER_BUY_QUOTE_ASSET_VOLUME] = kline[9]

            table.put_item(Item=row)

        print klines[-1]
        start_time = klines[-1][0] + constants.SECOND
        time.sleep(30)


if __name__ == "__main__":
    get_klines()
    print 'SUCCESS!'
