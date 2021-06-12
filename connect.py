import sqlite3
import sys

class dataManagement:
	def __init__(self):
		self.isDebug = False
		self.conn = sqlite3.connect('myDb.sqlite3')
		self.cursor = self.conn.cursor() # instantiate a cursor obj
	def executeQuery(self, query, retVal=False):
		errMessage = 'conn error'
		all_results = ''
		try:
			self.cursor.execute(query)
			self.con.commit()
		except:
			errMessage = str(sys.exc_info())
			if self.isDebug:
				print('errMessage: ', errMessage)

		if retVal:
			all_results = self.cursor.fetchall()
			return all_results, errMessage
		else:
			return errMessage
