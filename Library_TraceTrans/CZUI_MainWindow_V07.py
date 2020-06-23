#  -*- coding: utf-8 -*-

try:	import PySide.QtGui as QtGui
except :	import PySide2.QtWidgets as QtGui
try:	import PySide.QtCore as QtCore
except :	import PySide2.QtCore as QtCore
try:	from shiboken import wrapInstance
except:	from shiboken2 import wrapInstance

import pymel.all as pm
import CZUI_Custom_UI_V12 as CZui
import CZcss_V06 as CZcss

reload( CZcss )
reload( CZui )

def mayaMainWindowChecker ():
	import sys
	return type( sys.stdout ) != file

def getMayaWindow ():
	if mayaMainWindowChecker():
		import maya.OpenMayaUI as OMUI
		try:
			mainWindow = OMUI.MQtUtil.mainWindow()
			return wrapInstance( long( mainWindow ), QtGui.QMainWindow )
		except:			pass
	else:		return None

def CZ_rePosition ():
	if getMayaWindow() == None :		print ' this is not mayawindow ... '
	else :
		import maya.cmds as cmds
		start_Position = [45, 165]
		WindowSize = cmds.window( 'MayaWindow', q = 1, wh = 1 )
		WindowList = []
		ListDumpWidget = cmds.lsUI( dw = 1 )
		for Widget in ListDumpWidget:
			if 'CZ_' in Widget:
				if '_Win' in Widget:
					if cmds.window( Widget, q = 1, ex = 1 ):
						if cmds.window( Widget, q = 1, vis = 1 ):
							if not Widget in WindowList:		WindowList.append( Widget )
		existList = []
		for CZwindow in WindowList:
			windowHeight = cmds.window( CZwindow, q = 1, h = 1 )
			existList.append( [windowHeight, CZwindow] )
		existList.sort()
		existList.reverse()
		positionX = start_Position[0]
		positionY = start_Position[1]
		SizeY = 0
		for Height, CZwindow in existList:
			if cmds.window( CZwindow, q = 1, vis = 1 ):
				if Height > SizeY:			SizeY = Height + 40
				offset = cmds.window( CZwindow, q = 1, w = 1 )
				if positionX + offset + 20 > WindowSize[0]:
					positionX = start_Position[0]
					positionY = positionY + SizeY
				Ver = cmds.about( v = 1, q = 1 )
				if '2016' in Ver :
					DockName = CZwindow.replace( '_Win', '_Dock' )
					if cmds.dockControl( DockName , q = 1, ex = 1 ) :
						if cmds.dockControl( DockName , q = 1, fl = 1 ) :
							cmds.window( DockName , e = 1, tlc = ( positionY, positionX ) )
							positionX = positionX + offset + 20
					else :
						cmds.window( CZwindow , e = 1, tlc = ( positionY, positionX ) )
						positionX = positionX + offset + 20
				else :
					cmds.window( CZwindow , e = 1, tlc = ( positionY, positionX ) )
					positionX = positionX + offset + 20

def CZ_DeleteUI ( Window_Name = None ):
	if getMayaWindow() == None :		print ' this is not maya window ... '
	else :
		import maya.cmds as cmds
		WindowList = []
		ListDumpWidget = cmds.lsUI( dw = 1 )
		for Widget in ListDumpWidget:
			if 'CZ_' in Widget:
				if cmds.window( Widget, q = 1, ex = 1 ):
					if not Widget in WindowList:		WindowList.append( Widget )
		for CZwindow in WindowList:
			if Window_Name in CZwindow :			cmds.deleteUI( CZwindow )

class CZ_Creater( QtGui.QWidget ):
	def __init__ ( self ):
		super( CZ_Creater, self ).__init__()
		Css = CZcss.CZ_Style()
		self.setStyleSheet( Css.Style )

		self.CenterLayout = QtGui.QVBoxLayout( self )
		self.Creater = CZui.ClickLabel()
		self.Creater.setText( ' CZ Tools ' )
		self.Creater.setFrameShape( QtGui.QFrame.Box )
		self.Creater.setLineWidth( 3 )
		self.Creater.setStyleSheet( Css.Creater )

		self.CenterLayout.addWidget( self.Creater )

		self.ToolNameLay = QtGui.QHBoxLayout()
		self.CenterLayout.addLayout( self.ToolNameLay )

		self.ToolName = CZui.ClickLabel()
		self.ToolName.setText( ' Tool Name ' )
		self.ToolName.setFrameShape( QtGui.QFrame.Box )
		self.ToolName.setLineWidth( 1 )
		self.ToolName.setStyleSheet( Css.AppName )
		self.ToolNameLay.addWidget( self.ToolName )

		self.AppHelp = CZui.ClickLabel()
		self.AppHelp.setText( ' Help ' )
		self.AppHelp.setFrameShape( QtGui.QFrame.Box )
		self.AppHelp.setLineWidth( 1 )
		self.AppHelp.setMinimumWidth( 55 )
		self.AppHelp.setMaximumWidth( 55 )
		self.AppHelp.setStyleSheet( Css.AppName )
		self.ToolNameLay.addWidget( self.AppHelp )
		self.AppHelp.hide()

		self.CenterLayout.setContentsMargins( 3, 3, 3, 3 )

class UI_MainWindow( QtGui.QMainWindow ):
	def __init__ ( self ):
		self.MainWindow = getMayaWindow()
		super( UI_MainWindow, self ).__init__( self.MainWindow )

	def createMainWindow ( self, W_Name = 'Window', W_Title = 'UI_Title', W_Width = 200, W_Height = 100 , Mode = 'Main' ):

		self.CSS = CZcss.CZ_Style()
		self.DockName = W_Name.replace( '_Win', '_Dock' )
		self.setStyleSheet( self.CSS.Style )
		self.WindowName = W_Name
		self.WindowTitle = W_Title

		if pm.window( self.WindowName , q = 1 , ex = 1 ) :
			pm.deleteUI( self.WindowName )
			pm.refresh()

		self.Centralwidget = QtGui.QWidget( self )
		self.Centralwidget.setContentsMargins( 1, 1, 1, 1 )
		self.Main_Lay = QtGui.QVBoxLayout( self.Centralwidget )
		self.Main_Lay.setContentsMargins( 1, 1, 1, 1 )
		self.Main_Lay.setSpacing( 1 )
		self.setCentralWidget( self.Centralwidget )

		if Mode == 'Main' :
			self.Creater = CZ_Creater()
			self.Creater.ToolName.ClickConnect( Commamd = CZ_rePosition )
			self.Main_Lay.addWidget( self.Creater )

		self.setBaseSize( QtCore.QSize( W_Width, W_Height ) )
		self.setObjectName( self.WindowName )
		self.setWindowTitle( self.WindowTitle )
		self.setGeometry( 45, 160, 200, 100 )

	def DeleteDock( self ):
		WindowCheck = mayaMainWindowChecker()
		if WindowCheck == True :
			if pm.dockControl( self.DockName, ex = 1 ) :
				pm.deleteUI( self.DockName )
				pm.refresh()

	def SetDock( self , SetSide = 'right' , Content = None ):
		WindowCheck = mayaMainWindowChecker()
		if WindowCheck == True :
			pm.dockControl( self.DockName, area = SetSide , r = 1, content = Content , allowedArea = ['left', 'right'] , w = 100 )
			pm.refresh()

	def ToggleDock( self , Content = None ):
		WindowCheck = mayaMainWindowChecker()
		if WindowCheck == True :
			if pm.dockControl( self.DockName, ex = 1 ) :
				Floating = pm.dockControl( self.DockName, q = 1, fl = 1 )
				if Floating == 0 :
					pm.dockControl( self.DockName , e = 1 , fl = 1 )
					pm.window( self.DockName , e = 1 , w = 10, h = 10 )
					pm.dockControl( self.DockName , e = 1 , fl = 0 )
					pm.dockControl( self.DockName , e = 1 , fl = 1 )
					CZ_rePosition()
				else :
					pm.dockControl( self.DockName , e = 1 , fl = 0 )
					pm.dockControl( self.DockName, e = 1, r = 1 )
				pm.refresh()
			else :
				self.SetDock( SetSide = 'right', Content = Content )
				pm.dockControl( self.DockName, e = 1, r = 1 )
				pm.refresh()

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication( sys.argv )
	TestWindow = UI_MainWindow()
	TestWindow.createMainWindow( W_Name = 'Test Window', W_Title = 'Test_W', W_Width = 200, W_Height = 100 )
	TestWindow.show()
	sys.exit( app.exec_() )
