# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class frameBegin
###########################################################################

class frameBegin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART", pos = wx.DefaultPosition, size = wx.Size( 500,220 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Broadway" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang di HSART", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Aquino Demo" ) )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonAdminPage = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.Size( 110,30 ), 0 )
		self.buttonAdminPage.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer1.Add( self.buttonAdminPage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.buttonUserPage = wx.Button( self, wx.ID_ANY, u"User", wx.DefaultPosition, wx.Size( 110,30 ), 0 )
		self.buttonUserPage.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer1.Add( self.buttonUserPage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonAdminPage.Bind( wx.EVT_BUTTON, self.eventAdminPage )
		self.buttonUserPage.Bind( wx.EVT_BUTTON, self.eventUserPage )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventAdminPage( self, event ):
		event.Skip()

	def eventUserPage( self, event ):
		event.Skip()


###########################################################################
## Class frameLoginAdmin
###########################################################################

class frameLoginAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Admin Login", pos = wx.DefaultPosition, size = wx.Size( 400,230 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Broadway" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.backMenu = wx.Menu()
		self.backMenuChoose = wx.MenuItem( self.backMenu, wx.ID_ANY, u"Back", wx.EmptyString, wx.ITEM_NORMAL )
		self.backMenu.Append( self.backMenuChoose )

		self.m_menubar2.Append( self.backMenu, u"Back" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Admin Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Aquino Demo" ) )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txtUsername.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		self.txtPassword.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.buttonLogin = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		self.buttonLogin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer1.Add( self.buttonLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.eventBack, id = self.backMenuChoose.GetId() )
		self.txtPassword.Bind( wx.EVT_TEXT_ENTER, self.eventLoginAdmin )
		self.buttonLogin.Bind( wx.EVT_BUTTON, self.eventLoginAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventBack( self, event ):
		event.Skip()

	def eventLoginAdmin( self, event ):
		event.Skip()



###########################################################################
## Class frameHomeAdmin
###########################################################################

class frameHomeAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Home", pos = wx.DefaultPosition, size = wx.Size( 400,230 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.homeMenu = wx.Menu()
		self.homeMenuChoose = wx.MenuItem( self.homeMenu, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.homeMenu.Append( self.homeMenuChoose )

		self.m_menubar1.Append( self.homeMenu, u"Home" )

		self.m_menu4 = wx.Menu()
		self.adminAccountChoose = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Admin Account", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.adminAccountChoose )

		self.dataChoose = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Data", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.dataChoose )

		self.m_menubar1.Append( self.m_menu4, u"Lainnya" )

		self.logoutMenu = wx.Menu()
		self.logoutMenuChoose = wx.MenuItem( self.logoutMenu, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.logoutMenu.Append( self.logoutMenuChoose )

		self.m_menubar1.Append( self.logoutMenu, u"Logout" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Aquino Demo" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizer7.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.eventHome, id = self.homeMenuChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventAdminAccountPage, id = self.adminAccountChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventDataPage, id = self.dataChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventLogout, id = self.logoutMenuChoose.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventHome( self, event ):
		event.Skip()

	def eventAdminAccountPage( self, event ):
		event.Skip()

	def eventDataPage( self, event ):
		event.Skip()

	def eventLogout( self, event ):
		event.Skip()


###########################################################################
## Class frameAdminAccount
###########################################################################

class frameAdminAccount ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Admin Account", pos = wx.DefaultPosition, size = wx.Size( 400,230 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.homeMenu = wx.Menu()
		self.homeMenuChoose = wx.MenuItem( self.homeMenu, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.homeMenu.Append( self.homeMenuChoose )

		self.m_menubar1.Append( self.homeMenu, u"Home" )

		self.m_menu4 = wx.Menu()
		self.adminAccountChoose = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Admin Account", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.adminAccountChoose )

		self.dataChoose = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Data", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.dataChoose )

		self.m_menubar1.Append( self.m_menu4, u"Lainnya" )

		self.logoutMenu = wx.Menu()
		self.logoutMenuChoose = wx.MenuItem( self.logoutMenu, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.logoutMenu.Append( self.logoutMenuChoose )

		self.m_menubar1.Append( self.logoutMenu, u"Logout" )

		self.SetMenuBar( self.m_menubar1 )

		eventHome = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.addAdminButton = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.addAdminButton, 0, wx.ALL, 5 )

		self.editAdminButton = wx.Button( self, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.editAdminButton, 0, wx.ALL, 5 )

		self.deleteAdminButton = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.deleteAdminButton, 0, wx.ALL, 5 )


		eventHome.Add( bSizer13, 1, wx.EXPAND, 5 )

		self.adminAccountTable = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.adminAccountTable.CreateGrid( 3, 3 )
		self.adminAccountTable.EnableEditing( True )
		self.adminAccountTable.EnableGridLines( True )
		self.adminAccountTable.EnableDragGridSize( False )
		self.adminAccountTable.SetMargins( 0, 0 )

		# Columns
		self.adminAccountTable.AutoSizeColumns()
		self.adminAccountTable.EnableDragColMove( False )
		self.adminAccountTable.EnableDragColSize( True )
		self.adminAccountTable.SetColLabelSize( 30 )
		self.adminAccountTable.SetColLabelValue( 0, u"ID" )
		self.adminAccountTable.SetColLabelValue( 1, u"Username" )
		self.adminAccountTable.SetColLabelValue( 2, u"Password" )
		self.adminAccountTable.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.adminAccountTable.EnableDragRowSize( True )
		self.adminAccountTable.SetRowLabelSize( 80 )
		self.adminAccountTable.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.adminAccountTable.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		eventHome.Add( self.adminAccountTable, 0, wx.ALL, 5 )


		eventHome.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		eventHome.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( eventHome )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.eventHome, id = self.homeMenuChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventAdminAccountPage, id = self.adminAccountChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventDataPage, id = self.dataChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventLogout, id = self.logoutMenuChoose.GetId() )
		self.addAdminButton.Bind( wx.EVT_BUTTON, self.eventAddAdminDialog )
		self.editAdminButton.Bind( wx.EVT_BUTTON, self.eventEditAdminDialog )
		self.deleteAdminButton.Bind( wx.EVT_BUTTON, self.eventDeleteAdminDialog )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventHome( self, event ):
		event.Skip()

	def eventAdminAccountPage( self, event ):
		event.Skip()

	def eventDataPage( self, event ):
		event.Skip()

	def eventLogout( self, event ):
		event.Skip()

	def eventAddAdminDialog( self, event ):
		event.Skip()

	def eventEditAdminDialog( self, event ):
		event.Skip()

	def eventDeleteAdminDialog( self, event ):
		event.Skip()


###########################################################################
## Class dialogAddAdmin
###########################################################################

class dialogAddAdmin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Add Account", pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Tambah Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Aquino Demo" ) )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonAdd = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonAdd.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonAdd, 0, wx.ALL, 5 )

		self.buttonCancelAdmin = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonCancelAdmin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonCancelAdmin, 0, wx.ALL, 5 )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.txtPassword.Bind( wx.EVT_TEXT_ENTER, self.eventAddAdmin )
		self.buttonAdd.Bind( wx.EVT_BUTTON, self.eventAddAdmin )
		self.buttonCancelAdmin.Bind( wx.EVT_BUTTON, self.eventCancelAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventAddAdmin( self, event ):
		event.Skip()


	def eventCancelAdmin( self, event ):
		event.Skip()


###########################################################################
## Class dialogEditAdmin
###########################################################################

class dialogEditAdmin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Edit Account", pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Ubah Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Aquino Demo" ) )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonEdit = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonEdit.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonEdit, 0, wx.ALL, 5 )

		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonCancel.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonCancel, 0, wx.ALL, 5 )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.txtPassword.Bind( wx.EVT_TEXT_ENTER, self.eventEditAdmin )
		self.buttonEdit.Bind( wx.EVT_BUTTON, self.eventEditAdmin )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.eventCancelAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventEditAdmin( self, event ):
		event.Skip()


	def eventCancelAdmin( self, event ):
		event.Skip()


###########################################################################
## Class frameData
###########################################################################

class frameData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Data", pos = wx.DefaultPosition, size = wx.Size( 650,330 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.homeMenu = wx.Menu()
		self.homeMenuChoose = wx.MenuItem( self.homeMenu, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.homeMenu.Append( self.homeMenuChoose )

		self.m_menubar1.Append( self.homeMenu, u"Home" )

		self.m_menu4 = wx.Menu()
		self.adminAccountChoose = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Admin Account", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.adminAccountChoose )

		self.dataChoose = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Data", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.dataChoose )

		self.m_menubar1.Append( self.m_menu4, u"Lainnya" )

		self.logoutMenu = wx.Menu()
		self.logoutMenuChoose = wx.MenuItem( self.logoutMenu, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.logoutMenu.Append( self.logoutMenuChoose )

		self.m_menubar1.Append( self.logoutMenu, u"Logout" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.validasi = wx.Button( self, wx.ID_ANY, u"Validasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.validasi, 0, wx.ALL, 5 )


		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )

		self.dataUserAdmin = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataUserAdmin.CreateGrid( 10, 6 )
		self.dataUserAdmin.EnableEditing( True )
		self.dataUserAdmin.EnableGridLines( True )
		self.dataUserAdmin.EnableDragGridSize( False )
		self.dataUserAdmin.SetMargins( 0, 0 )

		# Columns
		self.dataUserAdmin.AutoSizeColumns()
		self.dataUserAdmin.EnableDragColMove( False )
		self.dataUserAdmin.EnableDragColSize( True )
		self.dataUserAdmin.SetColLabelSize( 30 )
		self.dataUserAdmin.SetColLabelValue( 0, u"Nama" )
		self.dataUserAdmin.SetColLabelValue( 1, u"No Rekening" )
		self.dataUserAdmin.SetColLabelValue( 2, u"Jenis" )
		self.dataUserAdmin.SetColLabelValue( 3, u"Jumlah (Kg)" )
		self.dataUserAdmin.SetColLabelValue( 4, u"Harga" )
		self.dataUserAdmin.SetColLabelValue( 5, u"Status" )
		self.dataUserAdmin.SetColLabelValue( 6, u"Jenis" )
		self.dataUserAdmin.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataUserAdmin.EnableDragRowSize( True )
		self.dataUserAdmin.SetRowLabelSize( 80 )
		self.dataUserAdmin.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataUserAdmin.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer12.Add( self.dataUserAdmin, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.eventHome, id = self.homeMenuChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventAdminAccountPage, id = self.adminAccountChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventDataPage, id = self.dataChoose.GetId() )
		self.Bind( wx.EVT_MENU, self.eventLogout, id = self.logoutMenuChoose.GetId() )
		self.validasi.Bind( wx.EVT_BUTTON, self.validate )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventHome( self, event ):
		event.Skip()

	def eventAdminAccountPage( self, event ):
		event.Skip()

	def eventDataPage( self, event ):
		event.Skip()

	def eventLogout( self, event ):
		event.Skip()

	def validate( self, event ):
		event.Skip()


###########################################################################
## Class dialogAddAdmin1
###########################################################################

class dialogAddAdmin1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Add Account", pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Validasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Aquino Demo" ) )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"upah", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonAdd = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonAdd.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonAdd, 0, wx.ALL, 5 )

		self.buttonCancelAdmin = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonCancelAdmin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonCancelAdmin, 0, wx.ALL, 5 )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonAdd.Bind( wx.EVT_BUTTON, self.eventAddAdmin )
		self.buttonCancelAdmin.Bind( wx.EVT_BUTTON, self.eventCancelAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventAddAdmin( self, event ):
		event.Skip()

	def eventCancelAdmin( self, event ):
		event.Skip()


###########################################################################
## Class frameHomeUser
###########################################################################

class frameHomeUser ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Home", pos = wx.DefaultPosition, size = wx.Size( 650,330 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar3 = wx.MenuBar( 0 )
		self.backMenu = wx.Menu()
		self.backMenuChoose = wx.MenuItem( self.backMenu, wx.ID_ANY, u"Back", wx.EmptyString, wx.ITEM_NORMAL )
		self.backMenu.Append( self.backMenuChoose )

		self.m_menubar3.Append( self.backMenu, u"Back" )

		self.SetMenuBar( self.m_menubar3 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.fillForm = wx.Button( self, wx.ID_ANY, u"Isi Form", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.fillForm, 0, wx.ALL, 5 )


		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )

		self.dataUserUser = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataUserUser.CreateGrid( 10, 6 )
		self.dataUserUser.EnableEditing( True )
		self.dataUserUser.EnableGridLines( True )
		self.dataUserUser.EnableDragGridSize( False )
		self.dataUserUser.SetMargins( 0, 0 )

		# Columns
		self.dataUserUser.EnableDragColMove( False )
		self.dataUserUser.EnableDragColSize( True )
		self.dataUserUser.SetColLabelSize( 30 )
		self.dataUserUser.SetColLabelValue( 0, u"Nama" )
		self.dataUserUser.SetColLabelValue( 1, u"No Rekening" )
		self.dataUserUser.SetColLabelValue( 2, u"Jenis" )
		self.dataUserUser.SetColLabelValue( 3, u"Jumlah (Kg)" )
		self.dataUserUser.SetColLabelValue( 4, u"Harga" )
		self.dataUserUser.SetColLabelValue( 5, u"Status" )
		self.dataUserUser.SetColLabelValue( 6, u"Jenis" )
		self.dataUserUser.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataUserUser.EnableDragRowSize( True )
		self.dataUserUser.SetRowLabelSize( 100 )
		self.dataUserUser.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataUserUser.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer12.Add( self.dataUserUser, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.eventBack, id = self.backMenuChoose.GetId() )
		self.fillForm.Bind( wx.EVT_BUTTON, self.eventFillForm )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventBack( self, event ):
		event.Skip()

	def eventFillForm( self, event ):
		event.Skip()


###########################################################################
## Class dialogFormUser
###########################################################################

class dialogFormUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"HSART - Form", pos = wx.DefaultPosition, size = wx.Size( 391,271 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Formulir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Aquino Demo" ) )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txtName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		fgSizer1.Add( self.txtName, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"No Rekening", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtRekening = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txtRekening.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		fgSizer1.Add( self.txtRekening, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Jenis Sampah", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.txtJenis = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txtJenis.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		fgSizer1.Add( self.txtJenis, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.txtJumlah = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		self.txtJumlah.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		fgSizer1.Add( self.txtJumlah, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonSave.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonSave, 0, wx.ALL, 5 )

		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonCancel.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer20.Add( self.buttonCancel, 0, wx.ALL, 5 )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.txtJumlah.Bind( wx.EVT_TEXT_ENTER, self.eventSaveForm )
		self.buttonSave.Bind( wx.EVT_BUTTON, self.eventSaveForm )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.eventCancelForm )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventSaveForm( self, event ):
		event.Skip()


	def eventCancelForm( self, event ):
		event.Skip()


