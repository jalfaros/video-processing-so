## Analización de videos mediante la utilización de YoloV5


Primeramente, para realizar el análisis de los distintos videos se utilizó el software llamado <strong>Yolo</strong> en su última versión <strong>5</strong> <br />

## Entrenamiento

El software anteriormente utilizado brinda un modelo previamente entrenado desde su descarga, sin embargo, para la utilización de este proyecto en específico tenía
la necesidad de identificar objetos en específico. Estos objetos que se plantearon en la ubicación son los siguientes: <br />

- Personas
- Armas
- Cuchillos
- Bebidas (principalmente alcohólicas)

Para el entrenamiento del modelo que permitiera a <strong>Yolo</strong> se procedió a generar un dataset con 5000 imágenes por categoría teniendo como peso total de imágenes
poco más de 5Gb. La realización del entrenamiento tomó en total 12 horas para generar el archivo con los modelos que **Yolo** necesita para su identificación en las imágenes. 

## Puntos a considerar durante el proceso de desarrollo

En el proceso de desarrollo se pretendía mediante los beneficios de los hilos y/o la concurrencia potenciar el poder de análisis de la tecnología de **Yolo** para que así;
la reducción del tiempo en el procesamiento de las imágenes se redujera, sin embargo, **Yolo** en su interior ya trabajaba métodos de concurrencia que optimizaba al máximo
su poder de procesamiento de video e imágenes.

## Aplicación de la solución

Para la realización de este proyecto y mediante las distintas pruebas realizadas durante el proceso de implementación se llegó a la conclusión de que la parte del procesamiento
e identificación de **Yolo** mediante video generaba un alto consumo en las máquinas en donde fue probado. A su vez, el tiempo de identificación mediante el procesamiento del 
video era totalmente exagerado, arrojando consigo hasta 40 minutos en procesar un video de una media de 5 minutos a una calidad de 1080p. 

Dado el poco aprovechamiento en el procesamiento de video, se procedió a crear un algoritmo que se encarga en desestructurar el video en una imágen a partir de cada cuadro
por segundo del video, por lo que así el manejo hacia la identificación de las clases en **Yolo** reducía considerablemente el tiempo en el que se procesaba.
Esta función descrita anteriormente se encuentra con el nombre <a href="https://github.com/jalfaros/video-processing-so/blob/4acdb71d03bb89fd4c81c238a43e2960c0065c8b/videoProcessor.py#L9">VideoProcessor</a>
