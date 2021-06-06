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
## Class frameLogin
###########################################################################

class frameLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Broadway" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Aquino Demo" ) )

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
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.buttonLogin = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonLogin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer1.Add( self.buttonLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Belum memiliki akun?", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer8.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.buttonRegisterPage = wx.Button( self, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonRegisterPage.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		fgSizer8.Add( self.buttonRegisterPage, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( fgSizer8, 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonLogin.Bind( wx.EVT_BUTTON, self.eventButtonLogin )
		self.buttonRegisterPage.Bind( wx.EVT_BUTTON, self.eventButtonRegisterPage )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventButtonLogin( self, event ):
		event.Skip()

	def eventButtonRegisterPage( self, event ):
		event.Skip()


###########################################################################
## Class frameRegistration
###########################################################################

class frameRegistration ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Registrasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Aquino Demo" ) )

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
		fgSizer1.Add( self.txtName, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"No Rekening", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtRekening = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtRekening, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century" ) )

		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.buttonRegister = wx.Button( self, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonRegister.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century" ) )

		bSizer1.Add( self.buttonRegister, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonRegister.Bind( wx.EVT_BUTTON, self.buttonEventRegister )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonEventRegister( self, event ):
		event.Skip()


###########################################################################
## Class frameHomeAdmin
###########################################################################

class frameHomeAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menubar1.Append( self.m_menu3, u"Home" )

		self.m_menu2 = wx.Menu()
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Profile Saya", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Nasabah", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menu2.AppendSubMenu( self.m_menu1, u"Profile" )

		self.m_menubar1.Append( self.m_menu2, u"Profile" )

		self.m_menu4 = wx.Menu()
		self.m_menu21 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"View Info Sampah", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Tambah Info Sampah", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem4 )

		self.m_menu4.AppendSubMenu( self.m_menu21, u"Info Sampah" )

		self.m_menubar1.Append( self.m_menu4, u"Info Sampah" )

		self.m_menu5 = wx.Menu()
		self.m_menu31 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu31, wx.ID_ANY, u"Data Sampah", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu31.Append( self.m_menuItem5 )

		self.m_menu5.AppendSubMenu( self.m_menu31, u"Setoran Sampah" )

		self.m_menubar1.Append( self.m_menu5, u"Setoran Sampah" )

		self.m_menu6 = wx.Menu()
		self.menuListUser = wx.Menu()
		self.m_menu6.AppendSubMenu( self.menuListUser, u"Semua User" )

		self.m_menubar1.Append( self.m_menu6, u"List User" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"HSART", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Aquino Demo" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizer7.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"C:\\Users\\Yola\\Downloads\\icon-bank-sampah-removebg-preview (1).bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_bitmap3, 0, wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.adad = wx.Button( self.m_panel4, wx.ID_ANY, u"placeholder userlist", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.adad, 0, wx.ALL, 5 )


		self.m_panel4.SetSizer( fgSizer6 )
		self.m_panel4.Layout()
		fgSizer6.Fit( self.m_panel4 )
		bSizer7.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.adad.Bind( wx.EVT_BUTTON, self.buttonUserList )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonUserList( self, event ):
		event.Skip()


###########################################################################
## Class panelDataUser
###########################################################################

class panelDataUser ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class frameDataUser
###########################################################################

class frameDataUser ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"total user", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer6.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.txtTotalUser = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtTotalUser.Wrap( -1 )

		fgSizer6.Add( self.txtTotalUser, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizer6, 1, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tambahuser = wx.Button( self, wx.ID_ANY, u"Tambah User", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.tambahuser, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizer7, 1, wx.EXPAND, 5 )

		self.tableUser = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tableUser.CreateGrid( 1, 1 )
		self.tableUser.EnableEditing( True )
		self.tableUser.EnableGridLines( True )
		self.tableUser.EnableDragGridSize( False )
		self.tableUser.SetMargins( 0, 0 )

		# Columns
		self.tableUser.EnableDragColMove( False )
		self.tableUser.EnableDragColSize( True )
		self.tableUser.SetColLabelSize( 30 )
		self.tableUser.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tableUser.EnableDragRowSize( True )
		self.tableUser.SetRowLabelSize( 80 )
		self.tableUser.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tableUser.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.tableUser, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tambahuser.Bind( wx.EVT_BUTTON, self.buttonAddUser )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonAddUser( self, event ):
		event.Skip()


