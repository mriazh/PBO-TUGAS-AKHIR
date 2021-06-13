import connect


class modelUsersData(connect.dataManagement):
	def show(self,orderby="users.rekening"):
		self.orderby = orderby
		result = []
		query = "SELECT id, name, users.rekening, jenis, jumlah, harga, status FROM users"
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result

	def getByid(self, id=1):
		self.id = id
		result = []
		query = "SELECT users.id,name,rekening,jenis,jumlah,harga,status FROM users WHERE users.id = {}".format(self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		result = self.cur.fetchone()
		return result

	def insert(self,nama,rekening,jenis,jumlah):
		self.nama = nama
		self.rekening = rekening
		self.jenis = jenis
		self.jumlah = jumlah
		query = "INSERT INTO users (name,rekening,jenis,jumlah,status) VALUES ('{}','{}','{}','{}','{}')".format(self.nama,self.rekening,self.jenis,self.jumlah,"Belum disetujui")
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()

	def update(self,upah,id):
		self.upah = upah
		self.id = id
		
		query = "UPDATE users SET harga = '{}', status = '{}'  WHERE id = '{}'".format(self.upah,"Disetujui",self.id)
		self.cur = self.conn.cursor()
		self.cur.execute(query)
		self.conn.commit()