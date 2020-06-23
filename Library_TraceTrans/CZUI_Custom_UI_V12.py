#  -*- coding: utf-8 -*-

try:	import PySide.QtGui as QtGui
except :	import PySide2.QtWidgets as QtGui
try:	import PySide.QtCore as QtCore
except :	import PySide2.QtCore as QtCore

import CZcss_V06 as CZcss
import random as random

reload( CZcss )

class CZ_LineEdit( QtGui.QWidget ):
	def __init__ ( self ):
		super( CZ_LineEdit, self ).__init__()
		self.CSS = CZcss.CZ_Style()
		self.setStyleSheet( self.CSS.Style )

		self.Layout = {}
		self.Line = {}
		self.HLay = {}

	def createUI ( self, LineEdit = None, Count = 1, Mode = 'V' , Label = False ):
		if Mode == 'G' :
			self.In_Layout = QtGui.QGridLayout()
			PosX = 0
			PosY = 0
			for Index in range( len( LineEdit ) ):
				if Label :
					self.Hlay[ Index ] = QtGui.QHBoxLayout()
					self.Line[ Index ] = QtGui.QLineEdit()
					self.Line[ Index ].setText( LineEdit[Index] )
					self.HLay[Index].addWidget( self.Line[ Index ] )
					self.In_Layout.addLayout( self.HLay[Index], PosY , PosX )
				else :
					self.Line[ Index ] = QtGui.QLineEdit()
					self.Line[ Index ].setText( LineEdit[Index] )
					self.In_Layout.addWidget( self.Line[ Index ], PosY , PosX )

				if PosX == ( Count - 1 ) :
					PosX = 0
					PosY += 1
				else :
					PosX += 1
		else :
			if Mode == 'V' :	self.In_Layout = QtGui.QVBoxLayout()
			else :				self.In_Layout = QtGui.QHBoxLayout()
			if type( LineEdit ) == str or type( LineEdit ) == unicode :
				if Label :
					self.Hlay[ 0 ] = QtGui.QHBoxLayout()
					self.Line[ 0 ] = QtGui.QLineEdit()
					self.Line[ 0 ].setText( LineEdit )
					self.HLay[ 0 ].addWidget( self.Line[ 0 ] )
					self.In_Layout.addLayout( self.HLay[ 0 ] )
				else :
					self.Line[ 0 ] = QtGui.QLineEdit()
					self.Line[ 0 ].setText( LineEdit )
					self.In_Layout.addWidget( self.Line[ 0 ] )
			else :
				if Label :
					for Index in range( Count ):
						self.Line[ Index ] = QtGui.QLineEdit()
						self.Line[ Index ].setText( LineEdit[Index] )
						self.In_Layout.addWidget( self.Line[ Index ] )
				else :
					for Index in range( Count ):
						self.Line[ Index ] = QtGui.QLineEdit()
						self.Line[ Index ].setText( LineEdit[Index] )
						self.In_Layout.addWidget( self.Line[ Index ] )

class CZ_LineEdit_Button( QtGui.QWidget ):
	def __init__ ( self ):
		super( CZ_LineEdit_Button, self ).__init__()
		self.CSS = CZcss.CZ_Style()
		self.setStyleSheet( self.CSS.Style )
		self.LineEdit = {}
		self.Button = {}

	def createUI ( self, BTNLabel = None, LineEdit = None, Count = 1 , Mode = 'V' ):
		if Mode == 'V' :
			self.In_Layout = QtGui.QVBoxLayout()
		else :
			self.In_Layout = QtGui.QHBoxLayout()

		for Index in range( len( BTNLabel ) ):
			if Mode == 'HU' :
				self.LE_Layout = QtGui.QVBoxLayout()
			else :
				self.LE_Layout = QtGui.QHBoxLayout()
			self.In_Layout.addLayout( self.LE_Layout )

			self.LineEdit[Index] = QtGui.QLineEdit()
			self.LineEdit[Index].setText( LineEdit[Index] )
			self.LE_Layout.addWidget( self.LineEdit[Index] )
			self.Button[Index] = QtGui.QPushButton()
			self.Button[Index].setText( BTNLabel[Index] )
			self.LE_Layout.addWidget( self.Button[Index] )

class CZ_ChoiceButton( QtGui.QWidget ):
	def __init__ ( self ):
		self.Count = 2
		super( CZ_ChoiceButton, self ).__init__()
		self.CSS = CZcss.CZ_Style()
		self.setStyleSheet( self.CSS.Style )

		self.BTNColorList = [self.CSS.BTN_Plate_PastelGreen]
		self.BTNColorList.append( self.CSS.BTN_Plate_PastelYellow )
		self.BTNColorList.append( self.CSS.BTN_Plate_SkyBlue )
		self.BTNColorList.append( self.CSS.BTN_Plate_PastelOrange )
		self.BTNColorList.append( self.CSS.BTN_Plate_Orange )

		self.Layout = {}
		self.Button = {}
		self.SelectedIndex = 0

	def createUI ( self, BTNLabel = None, Count = 2, Mode = 'H' ):
		if Mode == 'G' :
			self.In_Layout = QtGui.QGridLayout()
			PosX = 0
			PosY = 0
			for Index in range( len( BTNLabel ) ):
				self.Button[ Index ] = QtGui.QPushButton()
				self.Button[ Index ].setText( BTNLabel[Index] )
				self.In_Layout.addWidget( self.Button[ Index ], PosY , PosX )

				if PosX == ( Count - 1 ) :
					PosX = 0
					PosY += 1
				else :
					PosX += 1
		else :
			if Mode == 'V' :
				self.In_Layout = QtGui.QVBoxLayout()
			else :
				self.In_Layout = QtGui.QHBoxLayout()

			if type( BTNLabel ) == str or type( BTNLabel ) == unicode :
				self.Button[ 0 ] = QtGui.QPushButton()
				self.Button[ 0 ].setText( BTNLabel )
				self.In_Layout.addWidget( self.Button[ 0 ] )

			else :
				for Index in range( Count ):
					self.Button[ Index ] = QtGui.QPushButton()
					self.Button[ Index ].setText( BTNLabel[Index] )
					self.In_Layout.addWidget( self.Button[ Index ] )

	def ResetColors( self ):
		for Index in range( len( self.Button ) ) :
			self.Button[Index].setStyleSheet( self.CSS.BTN_default )
		self.SelectedIndex = 0

	def ChoiceColor( self, TargetIndex = 0 , CSS_Color = None ):
		for Index in range( len( self.Button ) ):
			self.Button[Index].setStyleSheet( self.CSS.BTN_default )
		if CSS_Color == None :
			ColorIndex = random.randrange( 0, 5 )
			ColorSet = self.BTNColorList[ColorIndex]
		if CSS_Color == 'Yellow' :
			ColorSet = self.CSS.BTN_Plate_PastelYellow
		if CSS_Color == 'Brown' :
			ColorSet = self.CSS.BTN_Plate_PastelBrown
		if CSS_Color == 'Red' :
			ColorSet = self.CSS.BTN_Plate_PastelRed
		if CSS_Color == 'Blue' :
			ColorSet = self.CSS.BTN_Plate_PastelBlue
		if CSS_Color == 'Sky' :
			ColorSet = self.CSS.BTN_Plate_SkyBlue
		if CSS_Color == 'Orange' :
			ColorSet = self.CSS.BTN_Plate_PastelOrange
		self.Button[TargetIndex].setStyleSheet( ColorSet )
		self.SelectedIndex = TargetIndex

	def ChangeColor( self, TargetIndex = 0, CSS_Color = None ):
		if CSS_Color == 'Yellow' :
			self.Button[TargetIndex].setStyleSheet( self.CSS.BTN_Plate_PastelYellow )
		if CSS_Color == 'Brown' :
			self.Button[TargetIndex].setStyleSheet( self.CSS.BTN_Plate_PastelBrown )
		if CSS_Color == 'Red' :
			self.Button[TargetIndex].setStyleSheet( self.CSS.BTN_Plate_PastelRed )
		if CSS_Color == 'Blue' :
			self.Button[TargetIndex].setStyleSheet( self.CSS.BTN_Plate_PastelBlue )
		if CSS_Color == 'Sky' :
			self.Button[TargetIndex].setStyleSheet( self.CSS.BTN_Plate_SkyBlue )
		if CSS_Color == 'Orange' :
			self.Button[TargetIndex].setStyleSheet( self.CSS.BTN_Plate_PastelOrange )

class CZ_BOX( QtGui.QWidget ):
	def __init__ ( self, parent = None , Mode = 'V' ):
		super( CZ_BOX, self ).__init__( parent )
		CSS = CZcss.CZ_Style()
		self.setStyleSheet( CSS.Style )
		self.setWindowTitle( 'Custom Widget' )
		self.In_Layout = QtGui.QVBoxLayout( self )
		self.In_Layout.setContentsMargins( 1, 1, 1, 1 )
		self.In_Layout.setSpacing( 1 )
		self.In_Layout.addStretch()

		self.Box = QtGui.QFrame()
		self.Box.setFrameShape( QtGui.QFrame.Box )
		self.Box.setFrameShadow( QtGui.QFrame.Plain )
		self.Box.setContentsMargins( 1, 1, 1, 1 )
		self.In_Layout.addWidget( self.Box )

		self.V_Layout_In = QtGui.QVBoxLayout( self.Box )
		self.V_Layout_In.setContentsMargins( 1, 1, 1, 1 )
		self.V_Layout_In.setSpacing( 1 )

		self.Label = ClickLabel()
		self.Label.setText( ' Label ' )
		self.Label.setStyleSheet( CSS.Label_SubTitle )
		self.V_Layout_In.addWidget( self.Label )

		self.Vis_Contents = QtGui.QWidget()
		self.V_Layout_In.addWidget( self.Vis_Contents )
		if Mode == 'V' :	self.V_Layout_Contents = QtGui.QVBoxLayout( self.Vis_Contents )
		else :				self.V_Layout_Contents = QtGui.QHBoxLayout( self.Vis_Contents )
		self.V_Layout_Contents.setContentsMargins( 1, 1, 1, 1 )
		self.V_Layout_Contents.setSpacing( 2 )

	def Set_Vis_Toggle( self ):
		self.Label.ClickConnect( Commamd = self.Toggle_Vis )

	def Toggle_Vis( self ):
		Vis_Status = self.Vis_Contents.isVisible()
		self.Vis_Contents.setVisible( not Vis_Status )

class CZ_CheckBox( QtGui.QWidget ):
	def __init__ ( self, parent = None ):
		super( CZ_CheckBox, self ).__init__( parent )
		self.setWindowTitle( 'Custom Widget' )
		self.ChoiceMode = False

	def createUI( self , ChoiceMode = False , Mode = 'V', Label = [] ):
		self.CheckBox = {}
		if Mode == 'V':
			self.In_Layout = QtGui.QVBoxLayout( self )
		else :
			self.In_Layout = QtGui.QHBoxLayout( self )
		self.In_Layout.setContentsMargins( 2, 2, 2, 2 )
		self.In_Layout.setSpacing( 1 )
		self.In_Layout.addStretch()

		for Index in range( len( Label ) ) :
			self.CheckBox[Index] = QtGui.QCheckBox( Label[Index] )
			self.CheckBox[Index].stateChanged.connect( self.PrintClicked )
			self.In_Layout.addWidget( self.CheckBox[Index] )

	def PrintClicked( self ):
		print ' CB Clicked   '

class CZ_Lister( QtGui.QWidget ):
	def __init__ ( self, parent = None ):
		super( CZ_Lister, self ).__init__( parent )
		self.setWindowTitle( 'Custom Widget' )
		self.CSS = CZcss.CZ_Style()
		self.setStyleSheet( self.CSS.Style )

		self.In_Layout = QtGui.QVBoxLayout()
		self.Lister = QtGui.QListWidget()
		self.In_Layout.addWidget( self.Lister )

	def GetList( self ):
		List = []

		print List
		return List

	def SetList( self , List = [] ):
		self.Lister.clear()
		for Item in List :
			if type( Item ) == str or type( Item ) == unicode :
				self.Lister.addItem( Item )
			else :
				self.Lister.addItem( Item.name() )

class CZ_ComboBox( QtGui.QWidget ):
	def __init__ ( self ):
		super( CZ_ComboBox, self ).__init__()
		self.In_Lay = QtGui.QVBoxLayout( self )
		self.In_Lay.setContentsMargins( 0, 0, 0, 0 )
		self.Css = CZcss.CZ_Style()
		self.setStyleSheet( self.Css.Style )
		self.ComboBox = QtGui.QComboBox()
		self.ComboBox.setMinimumHeight( 22 )
		self.In_Lay.addWidget( self.ComboBox )

	def Add_Item ( self, Label = '' ):
		self.ComboBox.addItem( Label )

	def Add_ItemList ( self, LabelList = [] ):
		for Item in LabelList :
			self.ComboBox.addItem( Item )

	def Get_Item ( self ):
		Label = self.ComboBox.currentText()
		return Label

class ClickLabel( QtGui.QLabel ):
	def __init( self ):
		super( ClickLabel, self ).__init__()

	def mouseReleaseEvent( self, ev ):
		self.emit( QtCore.SIGNAL( 'clicked()' ) )

	def ClickConnect( self, Commamd ):
		self.connect( self, QtCore.SIGNAL( 'clicked()' ), Commamd )

def AddSeprater( Parent = None ):
	Seprater = QtGui.QLabel()
	Seprater.setText( ' ' )
	Seprater.setMinimumHeight( 3 )
	Seprater.setMaximumHeight( 3 )
	Parent.addWidget( Seprater )

if __name__ == '__main__' :
	import sys
	app = QtGui.QApplication( sys.argv )
	Test = CZ_ComboBox()
	CSS = CZcss.CZ_Style()
	Test.setStyleSheet( CSS.Style )
	Test.Add_ItemList( LabelList = ['A', 'B', 'C'] )
	Test.show()
	for Index in range( Test.ComboBox.count() ):
		print Test.ComboBox.itemText( Index )

	sys.exit( app.exec_() )


