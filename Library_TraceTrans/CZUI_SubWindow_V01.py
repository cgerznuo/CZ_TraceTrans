#  -*- coding: utf-8 -*-

try:	import PySide.QtGui as QtGui
except :	import PySide2.QtWidgets as QtGui
try:	import PySide.QtCore as QtCore
except :	import PySide2.QtCore as QtCore
import CZcss_V06 as CZcss
import CZUI_MainWindow_V07 as CZwin


class UI_SubWindow( QtGui.QMainWindow ):
	def __init__( self ):
		self.MainWindow = CZwin.getMayaWindow()
		super( UI_SubWindow, self ).__init__( self.MainWindow )

	def createWindow( self, W_Name = 'Window', W_Title = 'UI_Title', W_Width = 200, W_Height = 100 ):
		self.CSS = CZcss.CZ_Style()
		self.setStyleSheet( self.CSS.Style )
		self.WindowName = W_Name
		self.WindowTitle = W_Title
		self.Centralwidget = QtGui.QWidget( self )
		self.Centralwidget.setContentsMargins( 1, 1, 1, 1 )
		self.Main_Lay = QtGui.QVBoxLayout( self.Centralwidget )
		self.Main_Lay.setContentsMargins( 1, 1, 1, 1 )
		self.Main_Lay.setSpacing( 1 )
		self.setCentralWidget( self.Centralwidget )
		self.ToolName = QtGui.QLabel()
		self.ToolName.setText( ' Tool Name ' )
		self.ToolName.setFrameShape( QtGui.QFrame.Box )
		self.ToolName.setLineWidth( 1 )
		self.ToolName.setStyleSheet( self.CSS.AppName )
		self.ToolName.setMaximumHeight( 30 )
		self.Main_Lay.addWidget( self.ToolName )
		self.Main_Lay.setContentsMargins( 3, 3, 3, 3 )

		self.setBaseSize( QtCore.QSize( W_Width, W_Height ) )
		self.setObjectName( self.WindowName )
		self.setWindowTitle( self.WindowTitle )
		self.setGeometry( 45, 160, 200, 100 )

if __name__ == '__main__':
	TestWindow = UI_SubWindow()
	TestWindow.createWindow( W_Name = 'TestWindow', W_Title = 'Test_W' )
	TestWindow.show()






