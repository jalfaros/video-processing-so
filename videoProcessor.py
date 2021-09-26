import cv2
import math
 # Si la carpeta no está creada, crearla. 

pathFile = '/home/nacho/Desktop/VideoProcessor/videos/kof.mp4'

def videoProcessor( pathFile ): 
    count = 0
    videoFile = pathFile
    cap = cv2.VideoCapture( videoFile )
    frameRate =  cap.get(5)


    x = 1
    while( cap.isOpened() ):
      frameId = cap.get(1)
      ret, frame = cap.read()
      if( ret != True ):
        break
      if (frameId % math.floor(frameRate) == 0):

          filename ="/home/nacho/Desktop/VideoProcessor/images/video%d.jpg" % count;count+=1
          print( filename )
          cv2.imwrite(filename, frame)

    cap.release()






videoProcessor( pathFile )