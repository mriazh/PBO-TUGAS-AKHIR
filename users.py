import connect


class modelUsersData(connect.dataManagement):
	def show(self,orderby="users.rekening"):
		self.orderby = orderby
		result = []
		query = "SELECT name, users.rekening, jenis, jumlah, harga, status FROM users"
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result
