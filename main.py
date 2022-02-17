import numpy as np
import pandas as pd
import glob

files = glob.glob("*.csv")
df = []

for f in files:
    csv = pd.read_csv(f)
    df.append(csv)

df = pd.concat(df)

df['date'] = pd.to_datetime(df['date'])

total_sales = pd.pivot_table(df, index='item', values='qty', aggfunc=np.sum)
sales_by_country = pd.pivot_table(df, index=['item', 'country'], values='qty', aggfunc=np.sum)

print(sales_by_country)
