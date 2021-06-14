import pandas as pd


kart = pd.read_excel(r'C:\Users\Jaison\Desktop\kart 2021\bd pandas.xlsm')
kart = kart.to_html()
print(kart)

