'''
setting environment variables up
'''
import os

def set_db_env():
    '''
    setting environment variables up
    '''
    os.environ['DB_USER'] = 'root'
    os.environ['DB_PASSWORD'] = '...'
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_PORT'] = '3306'
    print 'Environment has been configured'
