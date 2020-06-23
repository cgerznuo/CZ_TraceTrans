#  coding: utf-8
#  Edit Date : 2016 08 17

try:	import PySide.QtGui as QtGui
except :	import PySide2.QtWidgets as QtGui
try:	import PySide.QtCore as QtCore
except :	import PySide2.QtCore as QtCore
try:	import PySide.QtWebKit as QwebK
except :	import PySide2.QtWebKit as QwebK

import Library_TraceTrans.CZUI_MainWindow_V07 as CZMainwin
import Library_TraceTrans.CZcss_V06 as CZcss
import Library_TraceTrans.CZUI_Custom_UI_V12 as CZui
import Library_TraceTrans.CZ_Msg_PM_V02 as CZmsg
import CZ_TraceTrans_Cmd as CZcmd

reload( CZMainwin )
reload( CZui )
reload( CZcss )
reload( CZmsg )
reload( CZcmd )

class CZ_TraceTrans_UI( QtGui.QWidget ):

	def __init__ ( self ):
		self.CSS = CZcss.CZ_Style()
		super( CZ_TraceTrans_UI, self ).__init__()
		self.Debug = False
		self.initUI()

	def GetObj( self ):
		Obj = CZcmd.GetObj()
		self.Source.LineEdit[0].setText( Obj )
		pass

	def Spread( self ):
		Obj = self.Source.LineEdit[0].text()
		CZcmd.Spread( Source = Obj )

	def initUI ( self ):
		self.Contents = QtGui.QVBoxLayout( self )
		self.Contents.setContentsMargins( 1, 1, 1, 1 )
		self.Contents.setSpacing( 1 )

		self.TraceTransBox = CZui.CZ_BOX( Mode = 'V' )
		self.TraceTransBox.Set_Vis_Toggle()
		self.TraceTransBox.Label.setText( ' Trace Trans ' )
		self.Contents.addWidget( self.TraceTransBox )

		self.Source = CZui.CZ_LineEdit_Button()
		self.Source.createUI( BTNLabel = [ 'Get' ], LineEdit = [ 'Source' ], Count = 1 , Mode = 'V' )
		self.Contents.addLayout( self.Source.In_Layout )

		self.Button = QtGui.QPushButton()
		self.Button.setText( ' Spread ' )
		self.Contents.addWidget( self.Button )
		self.Button.setMinimumHeight( 40 )
		self.Button.setStyleSheet( self.CSS.BTN_Plate_PastelOrange )


		self.Source.Button[0].clicked.connect( self.GetObj )

		self.Button.clicked.connect( self.Spread )


if __name__ == '__main__':
		import sys
		app = QtGui.QApplication( sys.argv )
		CZ_Run_TraceTrans = CZ_TraceTrans_UI()
		CZ_Run_TraceTrans.show()
		sys.exit( app.exec_() )
