import wx
import sqlite3
import gui
import admin
import users


class App(wx.App):
	appFrame=None

	def OnInit(self):
		self.appFrame = start(None)
		self.appFrame.Show()
		return True


class start(gui.frameBegin):
	def __init__(self,parent):
		gui.frameBegin.__init__(self,parent)

	def eventAdminPage(self,event):
		self.adminPage = subLoginAdmin(None)
		self.Destroy()
		self.adminPage.Show()

	def eventUserPage(self,event):
		self.userPage = subHomeUser(None)
		self.Destroy()
		self.userPage.Show()


class subLoginAdmin(gui.frameLoginAdmin):
	def __init__(self,parent):
		gui.frameLoginAdmin.__init__(self,parent)

	def eventBack(self,event):
		self.back = start(None)
		self.Destroy()
		self.back.Show()

	def eventLoginAdmin(self,event):
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		conn = sqlite3.connect("myDb.sqlite3")
		cur = conn.cursor()
		cur.execute("SELECT username FROM admin WHERE username='%s' AND password = '%s';" % (inputtedUsername, inputtedPassword))
		if not cur.fetchone():
			wx.MessageBox('Data login salah', 'Terjadi kesalahan')
		else:
			self.loginAdmin = subHomeAdmin(None)
			self.Destroy()
			self.loginAdmin.Show()


class subHomeAdmin(gui.frameHomeAdmin):
	def __init__(self,parent):
		gui.frameHomeAdmin.__init__(self,parent)

	def eventHome(self,event):
		event.Skip()

	def eventAdminAccountPage(self,event):
		self.adminAccountPage = subAdminAccount(None)
		self.Destroy()
		self.adminAccountPage.Show()

	def eventDataPage(self,event):
		self.dataPage = subFrameData(None,None)
		self.Destroy()
		self.dataPage.Show()

	def eventLogout(self,event):
		dlg = wx.MessageBox("Anda yakin ingin logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
		if dlg == 2:
			self.login = subLoginAdmin(None)
			self.Destroy()
			self.login.Show()


class subAdminAccount(gui.frameAdminAccount):
	def __init__(self,parent):
		gui.frameAdminAccount.__init__(self,parent)
		self.id=id
		self.InitData()		

	def InitData(self,orderby="admin.id"):
		listAdmin = admin.modelAdminData()
		dataListAdmin = listAdmin.show(orderby)
		self.adminAccountTable.DeleteRows(0, self.adminAccountTable.GetNumberRows())

		self.adminAccountTable.AppendRows(len(dataListAdmin))

		for row in range(len(dataListAdmin)):
			for col in range(self.adminAccountTable.GetNumberCols()):
				val = dataListAdmin[row][col]
				self.adminAccountTable.SetCellValue(row,col,str(val))	

	def eventHome(self,event):
		self.home = subHomeAdmin(None)
		self.Destroy()
		self.home.Show()

	def eventAdminAccountPage(self,event):
		self.adminAccountPage = subAdminAccount(None)
		self.Destroy()
		self.adminAccountPage.Show()

	def eventDataPage(self,event):
		self.dataPage = subFrameData(None,None)
		self.Destroy()
		self.dataPage.Show()

	def eventLogout(self,event):
		dlg = wx.MessageBox("Anda yakin ingin logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
		if dlg == 2:
			self.login = subLoginAdmin(None)
			self.Destroy()
			self.login.Show()

	def eventAddAdminDialog(self,event):
		self.dialog = subAddAdmin(None)
		self.dialog.ShowModal()

	def eventSelectCell(self, event):
		col = event.GetCol()
		self.row = event.GetRow()	

	def eventEditAdminDialog(self,event):
		self.dialog = subEditAdmin(None,self.adminAccountTable.GetCellValue(self.row,0))
		self.dialog.ShowModal()

	def eventDeleteAdminDialog(self,event):
		deleteAdminData = admin.modelAdminData()
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		dialog = wx.MessageBox("Anda yakin ingin menghapus " + str(self.adminAccountTable.GetValue(self.row,1)) + " ?", wx.YES_NO | wx.ICON_INFORMATION)
		if dialog == 2:
			deleteAdminData.delete(str(self.adminAccountTable.GetCellValue(self.row,0)))
			wx.MessageBox("Data berhasil dihapus", "Delete", wx.OK | wx.ICON_INFORMATION)


class subAddAdmin(gui.dialogAddAdmin):
	def __init__(self,parent):
		gui.dialogAddAdmin.__init__(self,parent)
		
	def eventAddAdmin(self,event):
		insertAdminData = admin.modelAdminData()
		inputtedUsername = self.txtUsername.GetValue()
		inputtedPassword = self.txtPassword.GetValue()
		if inputtedUsername=="" or inputtedPassword=="":
			wx.MessageBox("Terdapat kolom kosong", "ERROR", wx.OK | wx.ICON_ERROR)
		else:
			insertAdminData.insert(str(inputtedUsername),str(inputtedPassword))
			wx.MessageBox("Akun admin telah ditambah", "Insert", wx.OK | wx.ICON_INFORMATION)
			self.Destroy()

	def eventCancelAdmin(self,event):
		self.Destroy()


class subEditAdmin(gui.dialogEditAdmin):
	def __init__(self,parent,id):
		gui.dialogEditAdmin.__init__(self,parent)
		listadmin = admin.modelAdminData()
		self.oldid = id
		adminid = listadmin.getByid(self.oldid)
		self.txtUsername.SetValue(str(adminid[0]))
		self.txtPassword.SetValue(str(adminid[1]))

	def eventEditAdmin(self,event):
		updateAdmin = admin.modelAdminData()
		self.txtUsername.GetValue()
		self.txtPassword.GetValue()
		updateAdmin.update(str(self.txtUsername.GetValue()),str(self.txtPassword.GetValue()),str(self.oldid))
		wx.MessageBox("Data berhasil diubah", "Update", wx.OK | wx.ICON_INFORMATION)
		self.Destroy()

	def eventCancelAdmin(self,event):
		self.Destroy()


class subFrameData(gui.frameData):
	def __init__(self,parent,id):
		gui.frameData.__init__(self,parent)
		self.id = id
		self.InitData()

	def InitData(self,orderby="users.rekening"):
		listUser = users.modelUsersData()
		dataListUser = listUser.show(orderby)
		self.dataUserAdmin.DeleteRows(0, self.dataUserAdmin.GetNumberRows())
		self.dataUserAdmin.AppendRows(len(dataListUser))

		for row in range(len(dataListUser)):
			for col in range(self.dataUserAdmin.GetNumberCols()):
				val = dataListUser[row][col]
				self.dataUserAdmin.SetCellValue(row,col,str(val))

	def eventHome(self,event):
		self.home = subHomeAdmin(None)
		self.Destroy()
		self.home.Show()

	def eventAdminAccountPage(self,event):
		self.adminAccountPage = subAdminAccount(None)
		self.Destroy()
		self.adminAccountPage.Show()

	def eventDataPage(self,event):
		self.dataPage = subFrameData(None)
		self.Destroy()
		self.dataPage.Show()

	def eventLogout(self,event):
		dlg = wx.MessageBox("Anda yakin ingin logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
		if dlg == 2:
			self.login = subLoginAdmin(None)
			self.Destroy()
			self.login.Show()


class subHomeUser(gui.frameHomeUser):
	def __init__(self,parent):
		gui.frameHomeUser.__init__(self,parent)
		self.id=id
		self.InitData()

	def InitData(self,orderby="users.rekening"):
		listUser = users.modelUsersData()
		dataListUser = listUser.show(orderby)
		self.dataUserUser.DeleteRows(0, self.dataUserUser.GetNumberRows())
		self.dataUserUser.AppendRows(len(dataListUser))

		for row in range(len(dataListUser)):
			for col in range(self.dataUserUser.GetNumberCols()):
				val = dataListUser[row][col]
				self.dataUserUser.SetCellValue(row,col,str(val))

	def eventBack(self,event):
		self.back = start(None)
		self.Destroy()
		self.back.Show()

	def eventFillForm(self,event):
		self.fillForm = subFormUser(None)
		self.Destroy()
		self.fillForm.Show()

class subFormUser(gui.dialogFormUser):
	def __init__(self,parent):
		gui.dialogFormUser.__init__(self,parent)

	def eventSaveForm( self, event ):
		event.Skip()

	def eventCancelForm( self, event ):
		event.Skip()