import boto3

# Schema of One Minute
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

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='OneMinute',
    KeySchema=[
        {
            'AttributeName': 'open_time',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'open_time',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 500,
        'WriteCapacityUnits': 500
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='OneMinute')
print(table.item_count)
