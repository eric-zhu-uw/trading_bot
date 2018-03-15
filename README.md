# Trading Bot

### Getting historical data (get_klines.py)
Utilize ```SELECT COUNT(*) FROM table_name;``` and  ```SELECT MAX(open_time) FROM table_name;``` when the query fails to update start at the last entry point recorded.

Can refer to **error.log** and **success.log** for more detailed failure report.

|Kline Time | Total # of Entries For Training Set |
| :-------: | :---------------------------------: |
| 1m | 151200 |
| 3m | 50400 |
| 5m | 30240 |

## TODO
1. clean up code and pylint error messages
2. get tensor flow and try training some models
