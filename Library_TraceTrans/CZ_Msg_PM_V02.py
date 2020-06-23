#  -*- coding: utf-8 -*-

def CZ_Msg ( Message = None, Object = None ):
	import pymel.all as pm
	try :
		if Message == None :
			Msg = '  Notice .... '
			pm.inViewMessage( bkc = 000000, msg = '<p>' + Msg + '</p>', fade = 1, fts = 12, pos = 'midCenterTop' )
			Message = '      ======[ CZ Script ] : Danger Notice ===== '
		else :
			if Object == None :
				pm.inViewMessage( bkc = 000000, msg = '<p>' + Message + '</p>', fade = 1, fts = 12, pos = 'midCenterTop' )
			else :
				pm.headsUpMessage( Message, o = Object, t = 3 )
				Message = '      ======[ CZ Script ] : ' + Message + ' >>>> ' + Object + ' ===== '
	except :
		pass
	print( Message )
