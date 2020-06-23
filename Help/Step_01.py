#  -*- coding: utf-8 -*-
File = __file__.replace( '.pyc', '.HelpInfo' )
File = File.replace( '.py', '.HelpInfo' )

Title = '[ Step 01 ]'
ImageName = __file__.split( '\\Help\\' )[-1]
ImageName = ImageName.replace( '.py', '.png' )
ImageSize = [400, 250]

Info = u' <br>'
Info = Info + u' <font size="5" color="#0033aa"> 어셋위치 셋팅하기  </font> <br>'
Info = Info + u' <br><br> 1 : Project ( 프로젝트와 시즌이 하나로 되어 있습니다.)'
Info = Info + u' <br><br> 2 : Episode '
Info = Info + u' <br><br> 3 : Type ( 캐릭터, 배경, 프랍 )'
Info = Info + u' <br><br> 4 : Asset ( 어셋의 이름입니다. )'

Data = [ Title, ImageName, str( ImageSize[0] ), str( ImageSize[1] ), Info ]

import json
with open( File, 'w' ) as f :
	json.dump( Data, f )

print File
