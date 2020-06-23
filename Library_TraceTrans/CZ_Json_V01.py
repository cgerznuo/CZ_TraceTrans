#  -*- coding: utf-8 -*-
import json
import os.path as Path

def GetJson( File = None , Debug = False ):
	if Path.isfile( File ) :
		with open( File , 'r' ) as f :
			Data = json.load( f )
	else :
		if Debug :		print ' File does not Exists ... '
		Data = [None]
	return Data

def SetJson( File = None , Data = ['Test'] , Debug = False ):
	with open( File, 'w' ) as f :
		json.dump( Data, f )

if __name__ == '__main__' :
	File = 'c:/Test.ShdInfo'
	Data = GetJson( File = File )
	Data.append( 'OpenOnce' )
	SetJson( File = File, Data = Data )
