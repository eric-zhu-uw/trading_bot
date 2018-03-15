from peewee import *
import env
import os

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

class KlineOne(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField

    class Meta:
        table_name = 'kline_one'


class KlineThree(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField

    class Meta:
        table_name = 'kline_three'

class KlineFive(BaseModel):
    open_time = BigIntegerField(primary_key=True)
    open = DoubleField()
    high = DoubleField()
    low = DoubleField()
    close = DoubleField()
    volume = DoubleField()
    close_time = BigIntegerField()
    quote_asset_volume = DoubleField()
    num_of_trades = IntegerField()
    taker_buy_base_asset_volume = DoubleField()
    taker_buy_quote_asset_volume = DoubleField

    class Meta:
        table_name = 'kline_five'

db.create_tables([KlineOne, KlineThree, KlineFive])
