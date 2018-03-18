'''
setup kline tables in mysql
'''
import os
from peewee import MySQLDatabase, Model, BigIntegerField, DoubleField, IntegerField
import env

env.set_db_env()
db = MySQLDatabase(
    'crypto',
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
    port=int(os.environ['DB_PORT'])
)

if db.connect():
    print 'Successful DB connection'
else:
    print 'Failed to connect'
    exit()

class BaseModel(Model):
    class Meta:
        database = db

# Schema for Kline API
#     1499040000000,       Open time
#     "0.01634790",        Open
#     "0.80000000",        High
#     "0.01575800",        Low
#     "0.01577100",        Close
#     "148976.11427815",   Volume
#     1499644799999,       Close time
#     "2434.19055334",     Quote asset volume
#     308,                 Number of trades
#     "1756.87402397",     Taker buy base asset volume
#     "28.46694368",       Taker buy quote asset volume
#     "17928899.62484339"  Can be ignored

# FOR CUR1/CUR2
# quote asset volume: volume of CUR2 bought & sold
# taker buy base asset volume: volume market takers bought of CUR1 (sold of CUR1)
# taker buy quote asset volume: volume market takers bought of CUR2

class Kline1(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    total_quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField() #how many
    taker_buy_quote_asset_volume = DoubleField()

    class Meta:
        table_name = 'kline_1'


class Kline3(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    total_quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField()

    class Meta:
        table_name = 'kline_3'

class Kline5(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    total_quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField()

    class Meta:
        table_name = 'kline_5'

class Kline15(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    total_quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField()

    class Meta:
        table_name = 'kline_15'

class Kline30(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    total_quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField()

    class Meta:
        table_name = 'kline_30'

db.create_tables([Kline1, Kline3, Kline5, Kline15, Kline30])
