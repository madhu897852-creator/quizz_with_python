import pandas as pd
a=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
iloc=a.iloc[4]
print('Iloc',iloc)
print('Loc',a.loc['e'])
print('Slicing',a[1:4])
print('Slicing with loc',a['b':'e'])
print('Filtering',a[a<5])
