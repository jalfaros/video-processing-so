Instituto Tecnológico de Costa Rica <br>
Campus Tecnológico Local San Carlos <br>
Principios de Sistemas Operativos - II Semestre 2021 <br>

Proyecto creado por:
- Jose Ignacio Alfaro Solano <a href="https://github.com/jalfaros">GitHub<a/>
- Warner Fidel Hurtado Laguna <a href="https://github.com/warnerHurtado">GitHub<a/>
  

# Análisis de videos mediante la utilización del software llamado **YoloV5**

Primeramente, para realizar el análisis de los distintos videos se utilizó el software llamado <strong>Yolo</strong> en su última versión <strong>5</strong> <br /> el cual
se utiliza para la identificación de atributos en videos y/o imágenes.

## Entrenamiento realizado

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
Esta función descrita anteriormente se encuentra con el nombre <a href="https://github.com/jalfaros/video-processing-so/blob/4acdb71d03bb89fd4c81c238a43e2960c0065c8b/videoProcessor.py#L9" target="_blank">VideoProcessor</a>


## Resultados obtenidos

<p float="center" style="text-align:center;">
  <img src="https://i.imgur.com/7SZ4EbR.jpg" width="400" />
  <img src="https://i.imgur.com/AgukeWf.jpg" width="400" />
</p>




## Tutorial

Clonar el proyecto
```git
git clone https://github.com/jalfaros/video-processing-so.git
```

Una vez clonado el proyecto se debe ingresar a la carpeta

```cmd
cd video-processing-so
```

Una vez dentro de la carpeta donde se clonó el proyecto se procede a instalar las dependencias mediante el siguiente código:

```cmd
pip install -r requirements.txt
```

Cuando la instalación de las diferentes dependencias finalice correctamente es importante ubicar la ruta de los videos a procesar dentro de la lista que se encuentra en 
el archivo con la extensión **.py** llamado **videoProcessor** cuya lista recibe el nombre de **videoPaths**
A continuación, se presenta un ejemplo de cómo debe de ser ingresadas las rutas dentro de la lista:

```python
videoPaths = ["C:\\Users\\Huawei D14\\Desktop\\videos_yolo\\kof.mp4",
              "C:\\Users\\Huawei D14\\Desktop\\videos_yolo\\RHCP.mp4"]
```

Dependiendo del rendimiento de la máquina y las especificaciones de las mismas no se recomienda procesar más de tres videos a la vez.

Finalmente, dentro del mismo archivo llamado **videoProcessor.py** se encuentra el siguiente fragmento de código:

```python
if __name__ == '__main__':
    multiprocessing()
    #threads()
```

Se encuentran dos funciones, genéricamente la función llamada **mutiprocessing()** se encuentra descomentada y la otra función llamada **threads()** está comentada; estas
dos funciones se ponen a disposición de los usuarios para que se utilicen dos tipos de abarcamiento de los algoritmos, la primera utilizando el multiprocesamiento y la segunda
mediante el uso de hilos.


