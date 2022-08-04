import pandas as pd

Target=[56000,70000,75000,60000]
Sales=[58000,68000,78000,61000]
ZoneSales=[Target,Sales]

zsaleDf=pd.DataFrame(ZoneSales,columns=['ZoneA','ZoneB','ZoneC','ZoneD'],index=['Target','Sales'])
print(zsaleDf)
