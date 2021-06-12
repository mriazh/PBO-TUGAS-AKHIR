import connect

class usersData(connect.dataManagement):
	def setDataAccount(self, name, rekening):
		self.query = 'INSERT INTO users (name, rekening) VALUES (\'%s\', \'%s\')' 
		self.query = self.query % (name, rekening)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg

	def getDataAccount(self, username, name, rekening):
		self.query = 'SELECT id FROM users where name=\'%s\' and rekening=\'%s\' ' 
		self.query = self.query % (username, name, rekening)
		if self.isDebug:
			print('self.query : ', self.query )
		id,errMsg = self.executeQuery(self.query, retVal=True)
		return id,errMsg

	def updateAccount(self, id, name, rekening):
		self.query = 'UPDATE users SET name=\'%s\', rekening=\'%s\' where id = %i;' 
		self.query = self.query % ( name, rekening, id)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg

	def deleteAccount(self, id):
		self.query = 'DELETE FROM users where id = %i' 
		self.query = self.query % (id)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg
