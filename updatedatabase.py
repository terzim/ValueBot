'''
When the database is already created, updates it
'''

import pickle
from openpyxl import load_workbook, Workbook
import numpy as np
import pandas as pd

try:
	dbfile = open('companies-pickle', 'rb')
except:
	print('File does not exist')
	quit()
else:
	db = pickle.load(dbfile)
	dbfile.close()

	wb = load_workbook('example.xlsx',data_only=True)
	sheet_ranges = wb['LIVE']

	companies = []
	scores = []

	for i in range(6,80):
		companies.append(sheet_ranges['D'+str(i)].value) 
		scores.append(sheet_ranges['BL'+str(i)].value)

	db[pd.to_datetime('now')] = scores

	dbfile = open('companies-pickle', 'wb')
	pickle.dump(db, dbfile)
	dbfile.close()

if __name__ == '__main__':
	import subprocess
	subprocess.Popen("dumpdatabase.py", shell=True)