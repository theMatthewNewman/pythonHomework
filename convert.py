from tkinter.tix import COLUMN
import pandas as pd

file = input("input file name: ")

df = pd.read_table(file,sep=",",header=None)
df.columns =['cell','E','W','N','S']

for index,row in df.iterrows():
    if row['E']>=.25:
        df.at[index,'E'] = 0
    else:
        df.at[index,'E'] = 1
    if row['W']>=.25:
        df.at[index,'W'] = 0
    else:
        df.at[index,'W'] = 1
    if row['N']>=.25:
        df.at[index,'N'] = 0
    else:
        df.at[index,'N'] = 1
    if row['S']>=.25:
        df.at[index,'S'] = 0
    else:
        df.at[index,'S'] = 1
df[['E','W','N','S']] = df[['E','W','N','S']].astype(int)

out = input("Output file name: ")
df.sort_values(by="cell").to_csv(out,sep=",",index=None)
