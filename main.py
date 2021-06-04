import wx
from controller import App

if __name__=='__main__':
    App=App(redirect=False)
    App.MainLoop()
    #app = wx.App(False)
    #frame = frameHome(None)
    #frame.Show(True)
    #app.MainLoop()