import numpy as np
import pandas as pd

employee ={
    "age":[25,np.nan,27,29,np.nan,32,35],
    "salary":[50000, 54000, np.nan, 58000, 60000, np.nan, 63000],
    'Category': ['A', 'B', 'B', 'A', np.nan, 'B', 'A']
}
df =pd.DataFrame(employee)
print(df)