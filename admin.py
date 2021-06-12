import connect


class modelAdminAccount(connect.dataManagement):
	def show(self,orderby="admin.id"):
		self.orderby = orderby
		result = []
		query = "SELECT admin.id, username, password FROM admin"
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result
