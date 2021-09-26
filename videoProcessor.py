from genericpath import isdir
import cv2
import math
import os
from os import mkdir
 # Si la carpeta no está creada, crearla. 

pathFile = 'D:\TEC\SO\primerProyecto\VideoProcessor\\videos\disparos.mp4'

def videoProcessor( pathFile ): 
    count = 0
    videoFile = pathFile
    cap = cv2.VideoCapture( videoFile )
    frameRate =  cap.get(5)

    while( cap.isOpened() ):
      frameId = cap.get(1)
      ret, frame = cap.read()
      if( ret != True ):
        break
      if (frameId % math.floor(frameRate) == 0):

        pathToSave = pathFile.split("\\")[-1][0:-4]
        
        if( os.path.isdir('./unstructuredVideos/'+pathToSave)):

          filename = './unstructuredVideos/'+pathToSave+"/video%d.jpg" % count;count+=1
          print( filename )
          cv2.imwrite(filename, frame)

        else:
          mkdir('./unstructuredVideos/'+pathToSave)
          
          filename = './unstructuredVideos/'+pathToSave+"/video%d.jpg" % count;count+=1
          print( filename )
          cv2.imwrite(filename, frame)
          

    cap.release()

videoProcessor( pathFile )