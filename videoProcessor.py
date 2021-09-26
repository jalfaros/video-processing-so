from genericpath import isdir
import cv2
import math
import os
from os import mkdir



pathFile = '/home/nacho/Desktop/videos/bb.mp4'

def videoProcessor( pathFile ): 
    
    count = 0
    videoFile = pathFile
    cap = cv2.VideoCapture( videoFile )
    frameRate =  cap.get(5)

    while( cap.isOpened() ):

      frameId = cap.get(1)
      ret, frame = cap.read()

      if not ret:
        break


      if (frameId % math.floor(frameRate) == 0):

        video_file_name = pathFile.split("/")[-1][0:-4]
        
        if( os.path.isdir('./unstructuredVideos/' + video_file_name)):
          writeFile(video_file_name, count, frame)
          count+=1
        else:

          mkdir('./unstructuredVideos/' + video_file_name)
          writeFile(video_file_name, count, frame)      
          count += 1

    cap.release()



def writeFile( video_file_name,count, frame):
  filename = './unstructuredVideos/'+video_file_name+"/" + video_file_name +"%d.jpg" % count;
  print(filename)
  cv2.imwrite(filename, frame)


videoProcessor( pathFile )