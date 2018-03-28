'''
setup feature info table in mysql
'''
import os
from peewee import MySQLDatabase, Model, DoubleField, CharField
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

class FeatureInfo(BaseModel):
    table_name = CharField()
    feature_name = CharField()
    min = DoubleField(null=True)
    max = DoubleField(null=True)
    mean = DoubleField(null=True)
    std = DoubleField(null=True)
    class Meta:
        table_name = 'feature_info'

db.create_tables([FeatureInfo])
