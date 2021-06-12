import connect

class adminAccount(connect.dataManagement):
	def setDataAccount(self, password, username):
		self.query = 'INSERT INTO admin (password, username) VALUES (\'%s\', \'%s\')' 
		self.query = self.query % (password, username)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg

	def getDataAccount(self, username, password):
		self.query = 'SELECT id FROM admin WHERE username=\'%s\' AND password=\'%s\' ' 
		self.query = self.query % (username, password)
		if self.isDebug:
			print('self.query : ', self.query )
		id,errMsg = self.executeQuery(self.query, retVal=True)
		return id,errMsg

	def updateAccount(self, username, password):
		self.query = 'UPDATE admin SET username=\'%s\', password=\'%s\' WHERE id = %i;' 
		self.query = self.query % ( username, password, id)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg

	def deleteAccount(self, id):
		self.query = 'DELETE FROM admin WHERE id = %i' 
		self.query = self.query % (id)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg
