
# (C)2021, Vertock Softwares
class gravity:
  def fall_stats(x,y,xDown,yDown,magMax=20):
    if y > yDown: 

     Ymagnitude = float(y-yDown ) 
    else:      
      Ymagnitude = float(yDown -y) 
    if x > xDown: 

     Xmagnitude = float(x-xDown ) 
    else:      
      Xmagnitude = float(xDown -x)

    return {
      'GoodFall':  Ymagnitude >=  magMax ,
      'Y Magnitude': Ymagnitude,
      'X Magnitude': Xmagnitude
      }
  
 # Version 1.0.0 
