import pandas as pd
import numpy as np
import torch

df1 = pd.DataFrame({'key': list('ababcdc'), 'data1': [5, 2, 3, 1, 2, 3, 4]})
print(df1)

res = df1.groupby('key')['data1'].min().values
print(res)
print(np.argsort(res))

print(np.argsort(np.array([3, 1, 2])))

res = torch.FloatTensor(2, 3)
print(res.zero_())
index = torch.LongTensor([1, 3]).view(-1, 1)
print(index)
res = res.scatter_(1, index, 1)
print(res)
