'''
From the imported excel sheet loads the names and scores of companies in two lists. 
Then, it creates a dataframe (in pandas style)
'''

from importexcelsheet import sheet_ranges
import numpy as np
import pandas as pd

companies = []
scores = []

for i in range(6,80):
	companies.append(sheet_ranges['D'+str(i)].value) 
	scores.append(sheet_ranges['BL'+str(i)].value)

d = {'initialtime': pd.Series(scores, index=companies)}
df = pd.DataFrame(d)
#d = dict(zip(companies, scores))

#formato_panda = pd.Series(d)

if __name__ == '__main__':
	print(df)