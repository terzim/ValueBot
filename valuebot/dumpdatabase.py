'''
Loads the companies database stored in local
'''
import pickle

databasename = 'companies-pickle'

dbfile = open(databasename, 'rb') # use binary mode files in 3.X

db = pickle.load(dbfile)

if __name__ == '__main__':
	print(db)
