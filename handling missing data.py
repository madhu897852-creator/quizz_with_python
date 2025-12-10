import pandas as pd
import numpy as np
a=pd.Series([1,2,np.nan,4,None,6])
isnull=a.isnull()
print('Is Null',isnull)
notnull=a.notnull()
print('Not NUll',notnull)
filled=a.fillna(3)
print('Filled',filled)
dropped=a.dropna()
print('Dropped NA',dropped)