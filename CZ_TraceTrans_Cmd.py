#  	coding: utf-8
#  	Created = 2018. 3. 19.
#  	author = Cgerzuno
import pymel.all as pm
import math as math

def GetObj():
	Select = 'None'
	List = pm.selected()
	if List :
		Select = List[0].name()
	return Select

def Make_TraceGrp( Source = None ):
	A_Grp = pm.group( em = 1, n = 'TraceTrans_A_Grp' )
	B_Grp = pm.group( em = 1, n = 'TraceTrans_B_Grp' )
	C_Grp = pm.group( em = 1, n = 'TraceTrans_C_Grp' )

	Source = pm.PyNode( Source )
	TransA = pm.xform( Source.vtx[0] , q = 1, t = 1, ws = 1 )
	TransB = pm.xform( Source.vtx[1] , q = 1, t = 1, ws = 1 )
	TransC = pm.xform( Source.vtx[2] , q = 1, t = 1, ws = 1 )

	A_Grp.t.set( TransA )
	B_Grp.t.set( TransB )
	C_Grp.t.set( TransC )

	TmpCon = pm.aimConstraint( B_Grp , A_Grp , wut = 'object' , wuo = C_Grp )
	TmpCon.rename( A_Grp.name() + '_Acon' )
	Dup = pm.duplicate( Source )[0]
	Dup.setParent( A_Grp )
	Shape = Dup.getShapes()
	if Shape :
		pm.delete( Shape )
	return [ A_Grp , B_Grp , C_Grp , Dup ]

def Cmd_GetDistance(PA=None , PB=None):
	XDis = (PB[0] - PA[0]) * (PB[0] - PA[0])
	YDis = (PB[1] - PA[1]) * (PB[1] - PA[1])
	ZDis = (PB[2] - PA[2]) * (PB[2] - PA[2])
	Distance = math.sqrt(XDis + YDis + ZDis)
	return Distance

def Spread( Source = None ):
	List = pm.selected()
	Return = Make_TraceGrp( Source = Source )
	SpreadGrp = pm.group( em = 1, n = Source + '_Spread_Grp' )
	print Return
	A_Grp = Return[0]
	B_Grp = Return[1]
	C_Grp = Return[2]
	DupGrp = Return[3]
	TA = pm.xform( A_Grp, q=1, t=1, ws=1 )
	TB = pm.xform( B_Grp, q=1, t=1, ws=1 )

	OrigScale = Cmd_GetDistance(PA=TA, PB=TB )

	if List :
		for Target in List :
			print Target
			TransA = pm.xform( Target.vtx[0] , q = 1, t = 1, ws = 1 )
			TransB = pm.xform( Target.vtx[1] , q = 1, t = 1, ws = 1 )
			TransC = pm.xform( Target.vtx[2] , q = 1, t = 1, ws = 1 )
			A_Grp.t.set( TransA )
			B_Grp.t.set( TransB )
			C_Grp.t.set( TransC )
			TargScale = Cmd_GetDistance(PA=TransA, PB=TransB )
			NS = TargScale / OrigScale
			A_Grp.s.set(NS,NS,NS)

			Loc = pm.spaceLocator()
			Loc.setParent( SpreadGrp )
			Trans = pm.xform( DupGrp , q = 1, t = 1, ws = 1 )
			Rot = pm.xform( DupGrp , q = 1, ro = 1, ws = 1 )
			Scale = pm.xform( DupGrp , q = 1, s = 1, ws = 1 )
			pm.xform( Loc , t = Trans , ro = Rot, s=Scale,ws = 1 )

	pm.delete( Return[0] )
	pm.delete( Return[1] )
	pm.delete( Return[2] )
