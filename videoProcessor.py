from genericpath import isdir
import cv2
import math
import os
from os import mkdir
import time
import concurrent.futures


def videoProcessor( pathFile ): 

    count = 0
    cap = cv2.VideoCapture( pathFile )
    frameRate =  cap.get( 5 )
    video_file_name = pathFile.split("\\")[-1][0:-4]

    while( cap.isOpened() ):

      frameId = cap.get( 1 )
      ret, frame = cap.read()

      if not ret:
        break

      if (frameId % math.floor( frameRate ) == 0):

    
        if not  os.path.isdir('./unstructuredVideos/' + video_file_name):
          mkdir('./unstructuredVideos/' + video_file_name)
          
        filename = './unstructuredVideos/'+video_file_name+"/" + video_file_name +"%d.jpg" % count;
        cv2.imwrite( filename, frame )
        count += 1

    cap.release()
    os.system("python detect.py --weights best.pt --img 640 --conf 0.25 --source ./unstructuredVideos/" + video_file_name + "/")
 



# threads = list();
# pathList = ['/home/nacho/Desktop/videos/kof.mp4', '/home/nacho/Desktop/videos/bb.mp4']


# def exampleFunction():
#   for i in range(len(pathList)):
#     thread = threading.Thread(target=videoProcessor, args=( pathList[i], ))
#     threads.append(thread)
#     thread.start()




#exampleFunction()
#D:\TEC\SO\primerProyecto\VideoProcessor\videos\\
videoPaths = ['D:\TEC\SO\primerProyecto\VideoProcessor\\videos\\disparos.mp4']

def multiProcessing():
  start = time.perf_counter()
  with concurrent.futures.ProcessPoolExecutor() as executor:
    for videoNamePath in videoPaths:
      executor.submit( videoProcessor, videoNamePath )
  print(f'Duration: {time.perf_counter() - start}')




if __name__ == '__main__':
  #videoProcessor('D:\TEC\SO\primerProyecto\VideoProcessor\\videos\\disparos.mp4')
  multiProcessing()