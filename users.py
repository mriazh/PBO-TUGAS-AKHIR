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

	def insert(self,nama,rekening,jenis,jumlah):
		self.nama = nama
		self.rekening = rekening
		self.jenis = jenis
		self.jumlah = jumlah
		query = "INSERT INTO users (name,rekening,jenis,jumlah) VALUES ('{}','{}','{}','{}')".format(self.nama,self.rekening,self.jenis,self.jumlah)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()