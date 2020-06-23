#  coding: utf-8
try:	import PySide.QtGui as QtGui
except :	import PySide2.QtWidgets as QtGui
try:	import PySide.QtCore as QtCore
except :	import PySide2.QtCore as QtCore
try:	import PySide.QtWebKit as QwebK
except :	import PySide2.QtWebKit as QwebK
import functools as FT

import Library_TraceTrans.CZUI_MainWindow_V07 as CZMainwin
import Library_TraceTrans.CZUI_SubWindow_V01 as CZsubW
import Library_TraceTrans.CZUI_Custom_UI_V12 as CZui
import Library_TraceTrans.CZ_Msg_PM_V02 as CZmsg
import Library_TraceTrans.CZ_Json_V01 as Json
import CZ_TraceTrans_UI as UI

reload( CZMainwin )
reload( CZmsg )
reload( CZui )
reload( Json )
reload( UI )

class HelpPage():
	def __init__( self ):
		self.Debug = True
		self.Page = ''
		self.Head = ' <html> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head> '
		self.BodyStart = ' <body bgcolor=white> <table border="0" cellpadding="10"> <tr> <td> <h2> '
		self.PageTitle = '[ Step 01 ]'
		self.BodyHead = ' </h2> </td> </tr> </table> <ul> <image Src = "'
		self.ImagePath = ''
		self.ImageFile = 'Step_01.png'
		self.ImageW = 400
		self.ImageH = 200
		self.BodyMid = '" width = 400 , height= 200 > </image> <br> '
		self.HelpMain = ' <br> line A <br> line B <br> line C <br> line D <br>  '
		self.BodyEnd = ' </ul> </body> </html> '

	def GetHelpInfo( self , File = None ):
		Data = Json.GetJson( File = File , Debug = self.Debug )
		self.PageTitle = Data[0]
		self.ImageFile = Data[1]
		self.ImageW = Data[2]
		self.ImageH = Data[3]
		self.BodyMid = '" width = %s height= %s > </image> <br> ' % ( self.ImageW, self.ImageH )
		self.HelpMain = Data[4]

	def PageInfo ( self , File = 'NoPage' ):
		if File == 'NoPage' :
			self.PageTitle = '[ Step 01 ]'
			self.ImageW = '400'
			self.ImageH = '200'
			self.BodyMid = '" width = %s height= %s > </image> <br> ' % ( self.ImageW, self.ImageH )
			self.ImageFile = 'Step_01.png'
			self.HelpMain = ' <br> line A <br> line B <br> line C <br> line D <br>  '
		else :
			self.GetHelpInfo( File = self.ImagePath + File )

		self.Page = self.Head + self.BodyStart + self.PageTitle + self.BodyHead
		self.Page = self.Page + self.ImagePath + self.ImageFile
		self.Page = self.Page + self.BodyMid + self.HelpMain + self.BodyEnd

	def GetPageList( self ):
		if __name__ == '__main__' :
			Path = 'C:\\OneDrive\\CZPython\\CZ_App\\Help\\'
		else :
			FileName = 'CZ_' + __file__.rsplit( 'CZ_' )[-1]
			Path = __file__.split( FileName )[0] + 'Help\\'

		import os
		PageList = os.listdir( Path )
		StepPage = []
		for File in PageList :
			if '.HelpInfo' in File :
				StepPage.append( File )
				self.ImagePath = Path
		return [ Path , StepPage ]

class CZ_TraceTrans_Win( CZMainwin.UI_MainWindow ):
	def __init__ ( self ):
		self.W_Name = 'CZ_TraceTrans_Win'
		self.DockName = self.W_Name.replace( '_Win', '_Dock' )
		self.Title = self.W_Name.replace( 'CZ_', '' )
		self.Title = self.Title.replace( '_Win', '' )
		super( CZ_TraceTrans_Win, self ).__init__()
		self.StepList = []
		self.StepIndex = 0
		self.initUI()
		self.setStyleSheet( self.CSS.Style )

	def ViewPage( self , Mode = 'Main' ):
		if Mode == 'Back' :
			print ' Back Page '
			self.StepIndex = self.StepIndex - 1
			if self.StepIndex < 0 :
				self.StepIndex = 0
			self.HelpInfo.PageInfo( File = self.StepList[self.StepIndex] )
			self.HelpView.setHtml( self.HelpInfo.Page )

		elif Mode == 'Next' :
			print ' Next Page '
			self.StepIndex = self.StepIndex + 1
			if self.StepIndex > len( self.StepList ) - 1 :
				self.StepIndex = len( self.StepList ) - 1
			self.HelpInfo.PageInfo( File = self.StepList[self.StepIndex] )
			self.HelpView.setHtml( self.HelpInfo.Page )

		if Mode == 'Main' :
			self.HelpInfo = HelpPage()
			self.StepList = self.HelpInfo.GetPageList()[1]
			print self.StepList
			self.HelpInfo.PageInfo( File = self.StepList[self.StepIndex] )
			self.HelpView.setHtml( self.HelpInfo.Page )

	def HelpPage( self ):
		Help_Wname = self.W_Name.replace( '_Win', '_Help' )
		HelpWindow = CZsubW.UI_SubWindow()
		HelpWindow.createWindow( W_Name = Help_Wname, W_Title = ' Help Page ' )
		HelpWindow.ToolName.setText( Help_Wname )
		self.HelpView = QwebK.QWebView()
		HelpWindow.Main_Lay.addWidget( self.HelpView )

		HelpBtn = CZui.CZ_ChoiceButton()
		HelpBtn.createUI( BTNLabel = [' Back Page ', ' Next Page ' ], Count = 2, Mode = 'H' )
		HelpBtn.Button[0].clicked.connect( FT.partial( self.ViewPage , 'Back' ) )
		HelpBtn.Button[1].clicked.connect( FT.partial( self.ViewPage , 'Next' ) )

		HelpWindow.Main_Lay.addLayout( HelpBtn.In_Layout )
		HelpWindow.resize( 500, 800 )

		HelpWindow.show()

		self.ViewPage()

		CZMainwin.CZ_rePosition()

	def initUI ( self, Dock = None ):
		AppName = self.W_Name.replace( '_Win', '' ).replace( 'CZ_', '' )
		self.DeleteDock()
		self.createMainWindow( W_Name = self.W_Name, W_Title = self.Title, W_Width = 50, W_Height = 50 )
		self.Creater.Creater.ClickConnect( Commamd = CZMainwin.CZ_rePosition )

		self.Creater.ToolName.setText( ' ' + AppName + ' ' )
		self.Creater.ToolName.ClickConnect( Commamd = FT.partial( self.ToggleDock, self.DockName ) )

		self.UI = UI.CZ_TraceTrans_UI()
		self.Main_Lay.addWidget( self.UI )
		self.Main_Lay.addStretch( 1 )
		self.Creater.AppHelp.show()
		self.Creater.AppHelp.ClickConnect( self.HelpPage )


def makeUI ():
	global CZ_Run_TraceTrans
	try:
		CZ_Run_TraceTrans.close()
		CZ_Run_TraceTrans.deleteLater()
		CZMainwin.CZ_DeleteUI()
	except:
		pass

	if CZMainwin.mayaMainWindowChecker():
		CZ_Run_TraceTrans = CZ_TraceTrans_Win()
		CZ_Run_TraceTrans.show()

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication( sys.argv )
	CZ_Run_TraceTrans = CZ_TraceTrans_Win()
	CZ_Run_TraceTrans.show()
	sys.exit( app.exec_() )
