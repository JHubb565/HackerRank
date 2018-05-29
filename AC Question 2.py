# trades = [[99.0,5.0,20.0]
#           ,[95.0,15.0,10.0]
#           ,[5.0,80.0,40.0]
#           ,[3.0,92.0,20.0]]
#
# labels = ['green','green','red','red']
#
# new_trades = [[90.0,10.0,15.0]
#               ,[10.0,98.0,50.0]]


import pandas as pd
import numpy as np

# make pandas dataframe with old trades
trades_df = pd.DataFrame(trades, columns=('Profit','Risk','Latency',),index=labels)
trades_df.reset_index(level=0,inplace=True)
print(trades_df)

good_trades = trades_df.where(trades_df['index'] =='green')
good_trade_average = good_trades.groupby('index').mean()
good_trade_array = np.array(good_trade_average)
print(good_trade_array)

bad_trades = trades_df.where(trades_df['index'] =='red')
bad_trade_average = bad_trades.groupby('index').mean()
bad_trade_array = np.array(bad_trade_average)
print(bad_trade_array)

# find mean distance between training data sets
dist_training_set = np.linalg.norm(abs(good_trade_array - bad_trade_array))
print(dist_training_set)

result_list=[]
for row in new_trades:
    new_trades_array = np.array(row)
    # do instance between good and bad
    dist = np.linalg.norm(abs(good_trade_array - new_trades_array))
    if dist < dist_training_set:
        result='green'
        result_list.append(result)
    elif dist >= dist_training_set:
        result = 'red'
        result_list.append(result)
print(result_list)






