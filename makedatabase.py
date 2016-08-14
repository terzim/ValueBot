'''
Imports the created data frame and loads it in a pickle local storage
'''

from createdataframe import df
import pickle

databasename = 'companies-pickle'

dbfile = open(databasename, 'wb') # use binary mode files in 3.X
pickle.dump(df, dbfile) # data is bytes, not str
dbfile.close()