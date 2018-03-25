'''
setup kline tables in mysql
'''
import os
from peewee import MySQLDatabase, Model, DoubleField, IntegerField, PrimaryKeyField, CharField
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

class FeaturesInt10(BaseModel):
    id = PrimaryKeyField(primary_key=True)
    rsi = CharField()
    mfi = CharField()
    proc = CharField()
    total_quote_volume = CharField()
    buy_quote_volume = CharField()
    buy_base_volume = CharField()
    high = CharField()
    low = CharField()
    close = CharField()
    lsma = CharField()
    ssma = CharField()
    num_trades = CharField()
    y = IntegerField()
    class Meta:
        table_name = 'features_int10'

db.create_tables([FeaturesInt10])
