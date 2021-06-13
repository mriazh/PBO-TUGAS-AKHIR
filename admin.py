import connect


class modelAdminData(connect.dataManagement):
	def show(self,orderby="admin.id"):
		self.orderby = orderby
		result = []
		query = "SELECT admin.id,username,password FROM admin"
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result

	def insert(self,username,password):
		self.username = username
		self.password = password
		query = "INSERT INTO admin (username,password) VALUES ('{}','{}')".format(self.username,self.password)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def getByid(self, id=1):
		self.id = id
		result = []
		query = "SELECT admin.id,username,password FROM admin WHERE admin.id = {}".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchone()
		return result

	def update(self,id,username,password,oldid):
		self.oldid = oldid
		self.id = id
		self.username = username
		self.password = password
		query = "UPDATE admin SET id = '{}', username = '{}', password = '{}' WHERE id = '{}'".format(self.id, self.username, self.password, self.oldid)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def delete(self,id):
		self.id = id
		query = "DELETE FROM admin WHERE id = '{}'".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()