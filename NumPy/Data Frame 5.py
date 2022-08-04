import pandas as pd     # creating dataframe object from 2D dictionary.
import numpy as np

staff=pd.Series([20,36,44])
salaries=pd.Series([279000,396800,563000])
avg=salaries/staff
org={'people':staff,'Amount':salaries,'Average':avg}
dtf5=pd.DataFrame(org)
print(dtf5)
