import numpy as np
import pandas as pd

employee ={
    "age":[25,np.nan,27,29,np.nan,32,35],
    "salary":[50000, 54000, np.nan, 58000, 60000, np.nan, 63000],
    'category': ['A', 'B', 'B', 'A', np.nan, 'B', 'A']
}
df =pd.DataFrame(employee)
print(df)


#Mean imputation

# df['age']=df['age'].fillna(df['age'].mean())
# print(df)
#Median imputation
# df['age']=df['age'].fillna(df['age'].median())
# print(df)
# Mode imputation
# df['category']=df['category'].fillna(df['category'].mode()[0])
# # The result of mode() could be a list (or Series) of one or more values.
# #  The [0] selects the first mode (i.e., the most frequent value) in case there are multiple modes.
# # For example, if the modes are ['A', 'B'], df['Category'].mode()[0] will select 'A', which is the first mode in the list
# print(df)
