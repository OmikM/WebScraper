import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from check import check


# url but for this version it works only for my
# path to file must be changed if python script will not be in the same folder as txt files 
# then it can look like it C:\\Users\\User\\Folder\\file

df = pd.read_csv('data.csv')

print(df)
    # time program will wait in secounds before refreshing web 
while True:
    i = 0
    for row in df.values:
        nrow = check(*list(row))
        
        if list(row)!=nrow:
            df.loc[i] = nrow
        i+=1
        df.to_csv('data.csv', index=False)
        time.sleep(10000)