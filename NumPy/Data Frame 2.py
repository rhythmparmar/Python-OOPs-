import pandas as pd

zoneA={'Target':56000,'Sales':58000}
zoneB={'Target':70000,'Sales':68000}
zoneC={'Target':75000,'Sales':78000}
zoneD={'Target':60000,'Sales':61000}

sales=[zoneA,zoneB,zoneC,zoneD]
saleDf=pd.DataFrame(sales,index=['zoneA','zoneB','zoneC','zoneD'])
print(saleDf)
