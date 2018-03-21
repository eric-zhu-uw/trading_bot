# Trading Bot

## Table of Contents
1. [Model](#model)
2. [How To Use Files](#how-to-use-files)

## Model
### Input Data
### Optimizer
Try a variety and decide which one to settle on based off accuracy (minimizes loss the most)
Should have a graph to show each example
### Loss Function

## How To Use Files
### Setup (env.py)
Move **temp_env.py** into **scripts/env.py**.

Then fill out the information correctly for all the environment variables.

This is because **env.py** is in **.gitignore** to protect your credentials for Binance, AWS, MySQL etc.

<br/>

### Getting historical data (get_klines.py)
Utilize ```SELECT COUNT(*) FROM table_name;``` and  ```SELECT MAX(open_time) FROM table_name;``` when the query fails to update start at the last entry point recorded.

Can refer to **error.log** and **success.log** for more detailed failure report.

|Kline Time | Total # of Entries For Training Set |
| :-------: | :---------------------------------: |
| 1m | 151200 |
| 3m | 50400 |
| 5m | 30240 |

## TODO
1. start trying different models and recording the results
2. fix model printing information
3. fix up features to get more information
