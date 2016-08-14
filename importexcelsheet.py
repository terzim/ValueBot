'''
Loads an excel sheet into memory
'''

from openpyxl import load_workbook, Workbook

source = 'example.xlsx'
sheetname = 'LIVE'

wb = load_workbook(source,data_only=True)
sheet_ranges = wb[sheetname]

if __name__ == '__main__':
	test1 = sheet_ranges['D14'].value
	print(test1)
	test2 = sheet_ranges['D78'].value
	print(test2)
	