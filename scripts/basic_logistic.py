import tensorflow as tf
from create_klines_schema import *

query = KlineOne.select().limit(10)

for kline in query:
    for attr, value in vars(kline).items():
        print attr, value, '\n'
