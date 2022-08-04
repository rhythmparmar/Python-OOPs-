import pandas  as pd
Sales={'yr1':{'Qtr1':34500,'Qtr2':56000,'Qtr3':47000,'Qtr4':49000},
       'yr2':{'Qtr1':44900,'Qtr2':46100,'Qtr3':57000,'Qtr4':59000}}

dfsales=pd.DataFrame(Sales)
print(dfsales)
