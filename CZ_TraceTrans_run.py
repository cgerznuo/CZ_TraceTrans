#  coding: utf-8

def CZ_TraceTrans_run():
	import sys
	FilePath = __file__
	NewPath = FilePath.rpartition( "\\" )[0]
	if not NewPath in sys.path:
		sys.path.append( NewPath )
	import CZ_TraceTrans_Win as CZttrans_Win
	reload( CZttrans_Win )
	CZttrans_Win.makeUI()
if __name__ == 'CZ_TraceTrans_run' :
	CZ_TraceTrans_run()

elif __name__ == '__main__' :
	import CZ_TraceTrans_Win as CZttrans_Win
	reload( CZttrans_Win )
	CZttrans_Win.makeUI()
