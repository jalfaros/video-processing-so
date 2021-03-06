Instituto Tecnológico de Costa Rica <br>
Campus Tecnológico Local San Carlos <br>
Principios de Sistemas Operativos - II Semestre 2021 <br>

Proyecto creado por:
- Jose Ignacio Alfaro Solano <a href="https://github.com/jalfaros">GitHub<a/>
- Warner Fidel Hurtado Laguna <a href="https://github.com/warnerHurtado">GitHub<a/>
  

# Análisis de videos mediante la utilización del software llamado **YoloV5**

Primeramente, para realizar el análisis de los distintos videos se utilizó el software llamado <strong>Yolo</strong> en su última versión <strong>5</strong> el cual
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

Como se muestra en las figuras presentes, se puede observar la identificación de los distintos objetos que fueron entrenados para que **Yolo** marcara en las imágenes de
los distintos videos que han sido suministrados previamente.

## Modificaciones para la mejora del proceso de identificación

Como se ha mencionado anteriormente, **Yolo** ya se encuentra de manera optimizada la parte de su procesamiento al momento de la identificación, sin embargo para la parte
de la desestructuración de los distintos videos, se han hecho ciertos cambios principalmente para utilizar los distintos procesos de concurrencia que existen en **Python**
para de esta manera reducir el tiempo del procesamiento de los videos.
  
La siguiente función es utilizada para la desestructuración del video en imágenes, esta función se encarga principalmente en crear una imágen por cada cuadro por segundo a su
vez generando una carpeta para alojarlas
```python
videoProcessor()
````
  
Los siguientes dos métodos hacen referencia a los distintos procesos de concurrencia utilizados para la mejora en el proceso de procesamiento de los videos e imágenes:

Esta función se encarga de utilizar hilos para generar una instancia por cada ruta de video que se encuentre dentro de la lista, maximizando así la capacidad de abarcar
más de un video a la vez.
  
```python
threads()
````

Por último, esta función es utilizada para aprovechar todos los núcleos disponibles del CPU, esto para aumentar la capacidad de procesamiento de los distintos videos.

```python
multiprocessing()
````
  
**Nota importante:** de las dos funciones anteriormente descritas, la que cuenta con mayor efectividad de tiempo en el procesamiento es la llamada: **multiprocessing()**

Esta en distintas pruebas han demostrado tener una capacidad de hasta 30 segundos más rápida en comparación si se utilizaran hilos de concurrencia.
  
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

<p style= "align:justify">Cuando la instalación de las diferentes dependencias finalice correctamente es importante ubicar la ruta de los videos a procesar dentro de la lista que se encuentra en 
el archivo con la extensión <strong>.py</strong> llamado <strong>videoProcessor</strong> cuya lista recibe el nombre de <strong>videoPaths</strong></p>
A continuación, se presenta un ejemplo de cómo debe de ser ingresadas las rutas dentro de la lista:

```python
videoPaths = ["C:\\Users\\Huawei D14\\Desktop\\videos_yolo\\kof.mp4",
              "C:\\Users\\Huawei D14\\Desktop\\videos_yolo\\RHCP.mp4"]
```

Dependiendo del rendimiento de la máquina y las especificaciones de las mismas no se recomienda procesar más de tres videos a la vez.

Finalmente, dentro del mismo archivo llamado <strong>videoProcessor.py</strong> se encuentra el siguiente fragmento de código:

```python
if __name__ == '__main__':
    multiprocessing()
    #threads()
```

Se encuentran dos funciones, genéricamente la función llamada **mutiprocessing()** se encuentra descomentada y la otra función llamada <strong>threads()</strong> está comentada; estas dos funciones se ponen a disposición de los usuarios para que se utilicen dos tipos de abarcamiento de los algoritmos, la primera utilizando el multiprocesamiento y la segunda mediante el uso de hilos.

  

