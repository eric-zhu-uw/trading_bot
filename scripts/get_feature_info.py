'''
populate mysql database with feature information such as:
 min/max/mean etc.
'''
from create_feature_info_schema import FeatureInfo
from constants import Features, FEATURES_INT10
import pandas as pd

def get_min_max(df, table_name, feature_name):
    print 'TABLE NAME: ' + str(table_name)
    print 'FEATURE NAME: ' + str(feature_name)

    count = int(df.describe()['id']['count'])
    min_val = float(df.iloc[0][feature_name].split(' ')[0])
    max_val = float(df.iloc[0][feature_name].split(' ')[0])

    for i in range(count):
        val = float(df.iloc[i][feature_name].split(' ')[0])
        min_val = min(min_val, val)
        max_val = max(max_val, val)

    print 'MIN: ' + str(min_val)
    print 'MAX: ' + str(max_val)

    try:
        FeatureInfo.get(
            (FeatureInfo.table_name == table_name) &
            (FeatureInfo.feature_name == feature_name))

        (FeatureInfo
         .update({FeatureInfo.min: min_val, FeatureInfo.max: max_val})
         .where((FeatureInfo.table_name == table_name) & (FeatureInfo.feature_name == feature_name))
         .execute())

    except FeatureInfo.DoesNotExist:
        FeatureInfo.create(
            table_name=table_name,
            feature_name=feature_name,
            min=min_val,
            max=max_val
        )

if __name__ == "__main__":
    DF = pd.read_csv(FEATURES_INT10 + '.csv')
    for key in Features:
        get_min_max(DF, FEATURES_INT10, Features[key])
    print 'Finished script!'
