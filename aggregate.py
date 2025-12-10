import pandas as pd
a=pd.Series([1,2,3,4,5])
print('Sum',a.sum())
print('Cumulative Sum',a.cumsum())
print('Aggregate',a.aggregate(['min','max','std','mean']))