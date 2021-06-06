import wx
from gui import *
import sqlite3
import sys

#koneksi ke db
class dataManager:
	def __init__(self):
		self.isDebug = False
		self.con = sqlite3.connect('myDb.sqlite3')
		self.cursor = self.con.cursor() # instantiate a cursor obj
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

#fungsi crud DB, nanti, fokus login
class account(dataManager):
	def setDataAccount(self, password, name, rekening):
		self.query = 'INSERT INTO users (password, name, rekening) VALUES (\'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (password, name, rekening)
		if self.isDebug:
			print('self.query : ', self.query )
		errMsg = self.executeQuery(self.query)
		return errMsg
		
	def getDataAccount(self, username, name, rekening):
		self.query = 'SELECT id FROM users where username=\'%s\' and name=\'%s\' and rekening=\'%s\' ' 
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

if __name__ == '__main__':
	acc = account()
	accList = acc.getDaftarMahasiswa()
	baris = 1
	for acc_row in accList:
		print(baris,'. ', acc_row)
		baris += 1

class App(wx.App):
    appFrame=None

    def OnInit(self):
        self.appFrame = loginController(frameLogin(None))
        self.appFrame.Show()
        return True

#login Frame controller
class loginController(frameLogin):

    def eventButtonLogin(self,event):
        inputtedUsername=self.txtUsername.GetValue()
        inputtedPassword=self.txtPassword.GetValue()
        con = sqlite3.connect("myDb.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT username from users WHERE username='%s' AND password = '%s';" % (inputtedUsername, inputtedPassword))
        if not cur.fetchone():
            wx.MessageBox('Data login salah', 'Terjadi kesalahan')
        else:
            #wx.MessageBox('Anda berhasil login', 'sukses')
        	self.appFrame=homeController(frameHomeAdmin(None))
        	self.appFrame.Show()
        	self.Destroy()

class homeController(frameHomeAdmin):

	def buttonUserList(self, event):
		self.appFrame=dataUserController(frameDataUser(None))
		self.appFrame.Show()
		self.Destroy()

class dataUserController(frameDataUser):

	def buttonAddUser(self, event):
		event.Skip()