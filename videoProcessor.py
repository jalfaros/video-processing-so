import cv2
import math
import os
from os import mkdir
import time
import concurrent.futures


def videoProcessor(pathFile):

    print("Desestructurando video... \n")
    count = 0
    cap = cv2.VideoCapture(pathFile)
    frameRate = cap.get(5)
    video_file_name = pathFile.split("\\")[-1][0:-4]

    if (os.path.isdir('./unstructuredVideos/' + video_file_name)):
        os.system("py detect.py --weights best.pt --img 640 --conf 0.25 --source ./unstructuredVideos/" + video_file_name + "/")
    else:
        while(cap.isOpened()):

            frameId = cap.get(1)
            ret, frame = cap.read()

            if not ret:
                break

            if (frameId % math.floor(frameRate) == 0):

                if not os.path.isdir('./unstructuredVideos/' + video_file_name):
                    mkdir('./unstructuredVideos/' + video_file_name)

                filename = './unstructuredVideos/'+video_file_name + \
                    "/" + video_file_name + "%d.jpg" % count
                cv2.imwrite(filename, frame)
                count += 1

        cap.release()
        os.system("py detect.py --weights best.pt --img 640 --conf 0.25 --source ./unstructuredVideos/" + video_file_name + "/")


videoPaths = ["C:\\Users\\Huawei D14\\Desktop\\videos_yolo\\kof.mp4",
              "C:\\Users\\Huawei D14\\Desktop\\videos_yolo\\RHCP.mp4"]


def multiprocessing():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for videoNamePath in videoPaths:
            executor.submit(videoProcessor, videoNamePath)
    print(f'Duración con multiprocesamiento: {time.perf_counter() - start}')


def threads():
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for video in videoPaths:
            executor.submit(videoProcessor, video)
    print(f'Duración con hilos: {time.perf_counter() - start}')



if __name__ == '__main__':
    multiprocessing()
    #threads()
