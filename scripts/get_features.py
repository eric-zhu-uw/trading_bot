'''
populate mysql database with all feature fields filled out
will trim all invalid entries
create multiple different datasets
'''
import datetime
from binance.client import Client
from create_klines_schema import *
import constants    #figure out how to clean up

def get_features(TableName):
    '''
    get_features
    '''
    TableName.create().save()

if __name__ == "__main__":
    get_features()
    print 'Finished script!'
