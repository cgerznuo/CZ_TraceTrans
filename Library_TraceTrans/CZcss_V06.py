#  -*- coding: utf-8 -*-

class CZ_Style():
	def __init__ ( self ):
		self.Style = ' QWidget { color: #b1b1b1; background-color: #323232; }'
		self.Style += 'QWidget:item:hover { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619); color: #000000; } '
		self.Style += 'QWidget:item:selected { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a); }'
		self.Style += 'QWidget:disabled { color: #404040; background-color: #323232; }'
		self.Style += 'QWidget:focus { /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/ }'

		self.Style += 'QTabWidget::pane { border: 1px solid #444; top: 1px; }'

		self.Style += 'QDockWidget::title { text-align: center; spacing: 3px; background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232); }'
		self.Style += 'QDockWidget::close-button, QDockWidget::float-button { text-align: center; spacing: 1px; background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232); }'
		self.Style += 'QDockWidget::close-button:hover, QDockWidget::float-button:hover { background: #242424; }'
		self.Style += 'QDockWidget::close-button:pressed, QDockWidget::float-button:pressed { padding: 1px -1px -1px 1px; }'

		self.Style += 'QMenu { border: 1px solid #000; }'
		self.Style += 'QMenu::item { padding: 2px 20px 2px 20px; }'
		self.Style += 'QMenu::item:selected { color: #000000; }'
		self.Style += 'QMenu::separator { height: 2px; color: white;  padding-left: 4px; margin-left: 10px; margin-right: 5px; background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434); }'

		self.Style += 'QMenuBar::item { background: transparent; }'
		self.Style += 'QMenuBar::item:selected { background: transparent; border: 1px solid #ffaa00; }'
		self.Style += 'QMenuBar::item:pressed { background: #444; border: 1px solid #000; margin-bottom:-1px; padding-bottom:1px; background-color: QLinearGradient( x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434 ); }'

		self.Style += 'QToolBar::handle { spacing: 3px; background: url(:/images/handle.png); }'

		self.Style += 'QProgressBar { border: 2px solid grey; border-radius: 3; text-align: center; }'
		self.Style += 'QProgressBar::chunk { background-color: #d7801a; width: 2.15px; margin: 0.5px; }'

		self.Style += 'QTabBar::tab:last { margin-right: 0; border-top-right-radius: 3px; }'
		self.Style += 'QTabBar::tab:first:!selected { margin-left: 0px; border-top-left-radius: 3px; }'
		self.Style += 'QTabBar::tab { color: #b1b1b1; border: 1px solid #444; border-bottom-style: none; background-color: #323232; padding-left: 10px; padding-right: 10px; padding-top: 3px; padding-bottom: 2px; margin-right: -1px; }'
		self.Style += 'QTabBar::tab:!selected { color: #b1b1b1; border-bottom-style: solid; margin-top: 3px; background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434); }'
		self.Style += 'QTabBar::tab:selected { border-top-left-radius: 3px; border-top-right-radius: 3px; margin-bottom: 0px; }'
		self.Style += 'QTabBar::tab:!selected:hover { border-top-left-radius: 3px; border-top-right-radius: 3px; background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00); }'

		self.Style += 'QScrollBar:horizontal { border: 1px solid #222222; background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848); height: 7px; margin: 0px 16px 0 16px; }'
		self.Style += 'QScrollBar::handle:horizontal { background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f); min-height: 20px; border-radius: 2; }'
		self.Style += 'QScrollBar::add-line:horizontal { border: 1px solid #1b1b19; border-radius: 2; width: 14px; subcontrol-position: right; subcontrol-origin: margin; background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a); }'
		self.Style += 'QScrollBar::sub-line:horizontal { border: 1px solid #1b1b19; border-radius: 2; width: 14px; subcontrol-position: left; subcontrol-origin: margin; background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a); }'
		self.Style += 'QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal { order: 1px solid black; width: 1px;  height: 1px; background: white; }'
		self.Style += 'QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {  background: none; }'
		self.Style += 'QScrollBar:vertical { background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848); width: 7px; margin: 16px 0 16px 0; border: 1px solid #222222; }'
		self.Style += 'QScrollBar::handle:vertical { background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);min-height: 20px;border-radius: 2px; }'
		self.Style += 'QScrollBar::add-line:vertical { border: 1px solid #1b1b19; border-radius: 2; height: 14px; subcontrol-position: bottom; subcontrol-origin: margin; background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a); }'
		self.Style += 'QScrollBar::sub-line:vertical { border: 1px solid #1b1b19; border-radius: 2; height: 14px; subcontrol-position: top; subcontrol-origin: margin; background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f); }'
		self.Style += 'QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { border: 1px solid black; width: 1px; height: 1px; background: white; }'
		self.Style += 'QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }'

		self.Style += 'QAbstractItemView { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d); }'

		self.Style += 'QLineEdit {	color : #e6e6fa ; background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #4d4d4d, stop: 1 #304080); border-width: 1px;  border-color: #1e1e1e; border-style: solid; border-radius: 3; padding: 1px; }'

		self.Style += 'QTextEdit { background-color: #242424; }'
		self.Style += 'QTextEdit:focus{ border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a); }'

		self.Style += 'QPlainTextEdit { background-color: #242424; }'

		self.Style += 'QListWidget { color : #e6e6fa ;border-width: 1px;border-color: #1e1e1e; border-style: solid; border-radius: 3;padding: 1px; background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #4d4d4d, stop: 1 #304080); }'

		self.Style += 'QPushButton { color: #b1b1b1; border-width: 1px; border-color: #1e1e1e; border-style: solid; border-radius: 3; padding: 3px; font-size: 12px; padding-left: 5px; padding-right: 5px; background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #505050, stop: 0.3 #404040, stop: 0.7 #404040, stop: 1 #303030 ) ; }'
		self.Style += 'QPushButton:pressed { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000000, stop: 0.4 #202020, stop: 0.6 #202020, stop: 1 #505050 ) ; }'

		self.Style += 'QRadioButton::indicator:checked{ color: #b1b1b1; background-color: #323232; border: 1px solid #b1b1b1; border-radius: 6px; }'
		self.Style += 'QRadioButton::indicator:unchecked{ color: #b1b1b1; background-color: #323232; border: 1px solid #b1b1b1; border-radius: 6px; }'
		self.Style += 'QRadioButton::indicator:checked { background-color: qradialgradient( cx: 0.5, cy: 0.5, fx: 0.5, fy: 0.5, radius: 1.0, stop: 0.25 #ffaa00, stop: 0.3 #323232); }'
		self.Style += 'QRadioButton::indicator { border-radius: 3; }'
		self.Style += 'QRadioButton::indicator:hover{  border: 1px solid #88aaff; }'
		self.Style += 'QRadioButton::indicator:disabled {  border: 1px solid #444; }'

		self.Style += 'QComboBox{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646); selection-background-color: #ffaa00; border-style: solid; border: 1px solid #1e1e1e; border-radius: 3; }'
		self.Style += 'QComboBox:on { padding-top: 3px;  padding-left: 4px; selection-background-color: #ffaa00; background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525); }'
		self.Style += 'QComboBox QAbstractItemView { border: 2px solid darkgray; selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a); }'
		self.Style += 'QComboBox::down-arrow { image: url(:/down_arrow.png); }'
		self.Style += 'QGroupBox:focus{ border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a); }'
		self.Style += 'QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 15px; border-left-width: 0px; border-left-color: darkgray; border-left-style: solid; border-top-right-radius: 3px; border-bottom-right-radius: 3px; }'

		self.Style += 'QComboBox:hover,QPushButton:hover,QLineEdit:hover,QListWidget:hover { border: 1px solid #88aaff; }'

		self.Style += 'QCheckBox { color: #ff9933; background-color: #323232; font-size: 12px; padding-left: 2px; padding-right: 2px; }'
		self.Style += 'QCheckBox::indicator:Checked { border: 1px solid #ff9933;background-color: #aa3300; }'
		self.Style += 'QCheckBox:disabled { color:#b1b1b1; }'

		self.Style += 'QMainWindow::separator { background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434); color: white;  padding-left: 4px; border: 1px solid #4c4c4c; spacing: 3px; }'
		self.Style += 'QMainWindow::separator:hover { background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f); color: white; padding-left: 4px;  border: 1px solid #6c6c6c; spacing: 3px;  }'

		self.Style += 'QHeaderView::section { background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565); color: white; padding-left: 4px; border: 1px solid #6c6c6c; }'

		self.Style += 'QToolTip { border: 1px solid black; background-color: #ffa02f; padding: 1px; border-radius: 3; opacity: 100; }'

		#  버튼컬러
		Font = 'font-family: Menlo;'
		BGC = 'background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,'
		Text_White = 'color: #b1b1b1 ;'
		Text_Black = 'color: #202020 ;'
		Text_Orange = 'color: #ff9933 ;'

		Blue = ['#5588ff', '#3366cc', '#1144aa']
		Orange = ['#ee9933', '#dd5533', '#991100']

		DarkGray = ['#606060', '#404040', '#202020']
		DarkSkyBlue = ['#77aaee', '#5599cc', '#3377aa']
		DarkRed = ['#aa3344', '#991122', '#770000']
		DarkBlue = ['#4477dd', '#2255aa', '#112288']

		PastelGreen = ['#ccffcc', '#aaffaa', '#88dd88']
		PastelBlue = ['#88aaff', '#6688ff', '#4466dd']
		PastelYellow = ['#ffff22', '#ffdd00', '#ddbb00']

		PastelRed = ['#ffcccc', '#ffaaaa', '#dd8888']
		PastelBrown = ['#ee9955', '#e18033', '#dd6000']
		PastelOrange = ['#ffbb55', '#ff9933', '#dd7711']
		PastelSkyBlue = ['#99ccff', '#77aadd', '#5588bb']

		AppBTN_Orange = ' QPushButton { font-size: 20px ; color: #ff9933; font-weight:1000 ; text-align:left; border-width: 1px; border-color: #ff9933; border-style: solid; border-radius: 6; background-color: #202050 ; padding-right: 12px; padding-top: 12px; }'
		AppBTN_Orange_Click = ' QPushButton:pressed { background-color: #505050 ;border-color: #ffffff; } '
		AppBTN_Orange_Hover = ' QPushButton:hover { border-color: #6688ff; } '
		self.BTN_AppBTN_Blue_2_Orange = AppBTN_Orange + AppBTN_Orange_Click + AppBTN_Orange_Hover
		self.BTN_default = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_White, BGC, DarkGray[0], DarkGray[1], DarkGray[1], DarkGray[2] )

		self.BTN_Plate_PastelGreen = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelGreen[0], PastelGreen[1], PastelGreen[1], PastelGreen[2] )
		self.BTN_Plate_PastelBlue = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelBlue[0], PastelBlue[1], PastelBlue[1], PastelBlue[2] )
		self.BTN_Plate_PastelYellow = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelYellow[0], PastelYellow[1], PastelYellow[1], PastelYellow[2] )
		self.BTN_Plate_PastelRed = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelRed[0], PastelRed[1], PastelRed[1], PastelRed[2] )
		self.BTN_Plate_PastelBrown = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelBrown[0], PastelBrown[1], PastelBrown[1], PastelBrown[2] )
		self.BTN_Plate_PastelOrange = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelOrange[0], PastelOrange[1], PastelOrange[1], PastelOrange[2] )

		self.BTN_Plate_SkyBlue = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelSkyBlue[0], PastelSkyBlue[1], PastelSkyBlue[1], PastelSkyBlue[2] )
		self.BTN_Plate_Orange = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, Orange[0], Orange[1], Orange[1], Orange[2] )
		self.BTN_Plate_DarkSkyBlue = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, DarkSkyBlue[0], DarkSkyBlue[1], DarkSkyBlue[1], DarkSkyBlue[2] )
		self.BTN_Plate_DarkRed = '%s %s stop: 0 %s, stop: 0.3 %s, stop: 0.7 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, DarkRed[0], DarkRed[1], DarkRed[1], DarkRed[2] )

		self.QBTN_DarkGray = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, DarkGray[1], DarkGray[2], DarkGray[2] )
		self.QBTN_PastelGreen = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelGreen[1], PastelGreen[2], PastelGreen[2] )
		self.QBTN_PastelBlue = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelBlue[1], PastelBlue[2], PastelBlue[2] )
		self.QBTN_PastelYellow = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelYellow[1], PastelYellow[2], PastelYellow[2] )
		self.QBTN_PastelRed = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelRed[1], PastelRed[2], PastelRed[2] )
		self.QBTN_PastelSkyBlue = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelSkyBlue[1], PastelSkyBlue[2], PastelSkyBlue[2] )
		self.QBTN_PastelOrange = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, PastelOrange[1], PastelOrange[2], PastelOrange[2] )
		self.QBTN_DarkSkyBlue = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, DarkSkyBlue[1], DarkSkyBlue[2], DarkSkyBlue[2] )
		self.QBTN_DarkRed = '%s %s stop: 0 #ffffff, stop: 0.8 %s, stop: 0.81 %s, stop: 1 %s ) ; ' % ( Text_Black, BGC, DarkRed[1], DarkRed[2], DarkRed[2] )

		self.Label_Gray = '%s %s %s stop: 0 %s, stop: 0.2 %s, stop: 0.85 %s, stop: 1 %s ) ;' % ( Text_White, Font, BGC, DarkGray[0], DarkGray[1], DarkGray[1], DarkGray[2] )
		self.Label_Green = '%s %s %s stop: 0 %s, stop: 0.2 %s, stop: 0.85 %s, stop: 1 %s ) ;' % ( Text_Black, Font, BGC, PastelGreen[0], PastelGreen[1], PastelGreen[1], PastelGreen[2] )
		self.Label_Yellow = '%s %s %s stop: 0 %s, stop: 0.2 %s, stop: 0.85 %s, stop: 1 %s ) ;' % ( Text_Black, Font, BGC, PastelYellow[0], PastelYellow[1], PastelYellow[1], PastelYellow[2] )
		self.Label_Blue = '%s %s %s stop: 0 %s, stop: 0.2 %s, stop: 0.85 %s, stop: 1 %s ) ;' % ( Text_Black, Font, BGC, PastelBlue[0], PastelBlue[1], PastelBlue[1], PastelBlue[2] )
		self.Label_Red = '%s %s %s stop: 0 %s, stop: 0.2 %s, stop: 0.85 %s, stop: 1 %s ) ;' % ( Text_Black, Font, BGC, PastelRed[0], PastelRed[1], PastelRed[1], PastelRed[2] )

		self.Label_Plate_Gray = '%s %s font-size: 15px; background-color: %s;' % ( Text_White, Font, DarkGray[1] )
		self.Label_Plate_Yellow = '%s %s font-size: 15px; background-color: %s;' % ( Text_Black, Font, PastelYellow[1] )
		self.Label_Plate_Blue = '%s %s font-size: 15px; background-color: %s;' % ( Text_Black, Font, PastelBlue[1] )
		self.Label_Plate_Red = '%s %s font-size: 15px; background-color: %s;' % ( Text_Black, Font, PastelRed[1] )
		self.Label_Plate_Green = '%s %s font-size: 15px; background-color: %s;' % ( Text_Black, Font, PastelGreen[1] )

		self.Label_SubTitle = '%s %s font-size: 15px; background-color: %s;' % ( Text_Orange, Font, DarkGray[2] )

		self.Creater = '%s font-family: Impact ; font-size: 30px ; background-color: %s;' % ( Text_Orange, DarkGray[2] )
		self.AppName = '%s font-family: Impact ; font-size: 20px ; background-color: %s;' % ( Text_Orange, Blue[2] )


if __name__ == '__main__' :
	import sys
	import PySide.QtGui as QtGui
	import PySide.QtCore as QtCore
	app = QtGui.QApplication( sys.argv )

	CSS = CZ_Style()
	Main = QtGui.QWidget()
	Main.setStyleSheet( CSS.Style )
	VLay = QtGui.QVBoxLayout( Main )
	HLay1 = QtGui.QHBoxLayout()
	VLay.addLayout( HLay1 )

	BtnList = []
	BtnList.append( ( CSS.BTN_default, 'default' ) )
	BtnList.append( ( CSS.BTN_AppBTN_Blue_2_Orange, 'BTN_AppBTN_Blue_2_Orange' ) )

	PlateList = []
	PlateList.append( ( CSS.BTN_Plate_PastelBlue, 'BTN_Plate_PastelBlue' ) )
	PlateList.append( ( CSS.BTN_Plate_PastelBrown, 'BTN_Plate_PastelBrown' ) )
	PlateList.append( ( CSS.BTN_Plate_PastelGreen, 'BTN_Plate_PastelGreen' ) )
	PlateList.append( ( CSS.BTN_Plate_PastelOrange, 'BTN_Plate_PastelOrange' ) )
	PlateList.append( ( CSS.BTN_Plate_PastelRed, 'BTN_Plate_PastelRed' ) )
	PlateList.append( ( CSS.BTN_Plate_PastelYellow, 'BTN_Plate_PastelYellow' ) )
	PlateList.append( ( CSS.BTN_Plate_Orange, 'BTN_Plate_Orange' ) )
	PlateList.append( ( CSS.BTN_Plate_SkyBlue, 'BTN_Plate_SkyBlue' ) )
	PlateList.append( ( CSS.BTN_Plate_DarkRed, 'BTN_Plate_DarkRed' ) )
	PlateList.append( ( CSS.BTN_Plate_DarkSkyBlue, 'BTN_Plate_DarkSkyBlue' ) )

	QBTNList = []
	QBTNList.append( ( CSS.QBTN_DarkGray, 'QBTN_DarkGray' ) )
	QBTNList.append( ( CSS.QBTN_DarkSkyBlue, 'QBTN_DarkSkyBlue' ) )
	QBTNList.append( ( CSS.QBTN_DarkRed, 'QBTN_DarkRed' ) )
	QBTNList.append( ( CSS.QBTN_PastelBlue, 'QBTN_PastelBlue' ) )
	QBTNList.append( ( CSS.QBTN_PastelGreen, 'QBTN_PastelGreen' ) )
	QBTNList.append( ( CSS.QBTN_PastelYellow, 'QBTN_PastelYellow' ) )
	QBTNList.append( ( CSS.QBTN_PastelRed, 'QBTN_PastelRed' ) )
	QBTNList.append( ( CSS.QBTN_PastelSkyBlue, 'QBTN_PastelSkyBlue' ) )
	QBTNList.append( ( CSS.QBTN_PastelOrange, 'QBTN_PastelOrange' ) )

	LabelList = []
	LabelList.append( ( CSS.Label_Blue, 'Label_Blue' ) )
	LabelList.append( ( CSS.Label_Gray, 'Label_Gray' ) )
	LabelList.append( ( CSS.Label_Green, 'Label_Green' ) )
	LabelList.append( ( CSS.Label_Red, 'Label_Red' ) )
	LabelList.append( ( CSS.Label_SubTitle, 'Label_SubTitle' ) )
	LabelList.append( ( CSS.Label_Yellow, 'Label_Yellow' ) )
	PlateLabelList = []

	PlateLabelList.append( ( CSS.Label_Plate_Blue, 'Label_Plate_Blue' ) )
	PlateLabelList.append( ( CSS.Label_Plate_Gray, 'Label_Plate_Gray' ) )
	PlateLabelList.append( ( CSS.Label_Plate_Green, 'Label_Plate_Green' ) )
	PlateLabelList.append( ( CSS.Label_Plate_Red, 'Label_Plate_Red' ) )
	PlateLabelList.append( ( CSS.Label_Plate_Yellow, 'Label_Plate_Yellow' ) )

	for List in [ ( BtnList, 'Btn' ), ( PlateList, 'Plate Btn' ), ( QBTNList, 'Quard Btn' ), ( LabelList, 'Label' ), ( PlateLabelList, ' Plate Label' ) ] :
		Part = QtGui.QLabel()
		VLay.addWidget( Part )
		Part.setText( ' ====== ' + List[1] + ' ====== ' )
		Part.setStyleSheet( CSS.Label_SubTitle )
		HLay = QtGui.QHBoxLayout()
		VLay.addLayout( HLay )
		Count = 0
		for BTN in List[0]:
			if Count > 2 :
				HLay = QtGui.QHBoxLayout()
				VLay.addLayout( HLay )
				Count = 0
			if 'Label' in List[1] :
				Widget = QtGui.QLabel()
			else :
				Widget = QtGui.QPushButton()
			HLay.addWidget( Widget )
			Widget.setStyleSheet( BTN[0] )
			Widget.setText( BTN[1] )
			Count = Count + 1

	Part = QtGui.QLabel()
	VLay.addWidget( Part )
	Part.setText( ' ====== CheckBox ====== ' )
	Part.setStyleSheet( CSS.Label_SubTitle )

	Lay = QtGui.QHBoxLayout()
	VLay.addLayout( Lay )
	Test = QtGui.QCheckBox( 'CheckBox On' )
	Lay.addWidget( Test )
	Test2 = QtGui.QCheckBox( 'CheckBox Off' )
	Lay.addWidget( Test2 )
	Test.setCheckState( QtCore.Qt.Checked )

	Main.show()
	sys.exit( app.exec_() )

