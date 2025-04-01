# AWS Finance Data Pipeline

Este proyecto implementa un **pipeline** de procesamiento de datos financieros en la nube utilizando los servicios de **AWS**. El pipeline descarga, procesa y guarda datos financieros históricos de diversas fuentes como **Yahoo Finance** y **Alpha Vantage**, calculando métricas clave como el retorno diario y la volatilidad. Los datos procesados se almacenan en un **bucket de Amazon S3**, lo que facilita el análisis posterior y la integración con otras aplicaciones.

El propósito de este proyecto es ofrecer una solución escalable, eficiente y automatizada para gestionar datos financieros utilizando la infraestructura de **AWS**.

## Descripción

Este pipeline permite gestionar datos financieros de forma automatizada y eficiente, cubriendo las siguientes etapas:

 ### 1. **Obtención de Datos Financieros**
   - Los datos históricos de activos financieros se descargan de dos fuentes principales:
     - **Yahoo Finance** a través de la librería `yfinance`. Esta API proporciona datos históricos de acciones, fondos y otros activos financieros en tiempo real.
     - **Alpha Vantage**, utilizando una API gratuita que ofrece datos detallados sobre mercados de acciones, forex y criptomonedas.

 ### 2. **Procesamiento de los Datos**
   - Una vez descargados los datos, se procesan para calcular **métricas financieras clave**:
     - **Retorno Diario**: Calcula el cambio porcentual diario del precio de la acción.
     - **Volatilidad**: Mide la variabilidad de los precios de la acción a lo largo del tiempo.
   - Estos cálculos se realizan sobre las columnas de precios de cierre o precios ajustados de las acciones.
  
 ### 3. **Almacenamiento en S3**
   - Los datos procesados (incluidos los retornos y la volatilidad calculados) se almacenan en un archivo CSV.
   - Este archivo CSV se sube de manera automatizada a un bucket de **Amazon S3**, proporcionando un lugar seguro, duradero y accesible desde cualquier lugar para su análisis posterior.

 ### 4. **Escalabilidad y Automatización**
   - Este pipeline está diseñado para escalar fácilmente con más tickers de acciones o períodos de tiempo más largos.
   - El uso de servicios como **Amazon S3** y la automatización del proceso lo hacen adecuado para análisis en tiempo real, informes periódicos o integraciones con otros sistemas.
     
### Requisitos

Para ejecutar este proyecto, debes tener configurado lo siguiente:

- **Python 3.x**: El proyecto está desarrollado en Python 3.x, por lo que necesitas tener esta versión instalada en tu entorno.
- **Paquetes de Python**: El proyecto utiliza varias bibliotecas, que puedes instalar utilizando `pip`:
  - `yfinance`: Para descargar datos históricos de Yahoo Finance.
  - `pandas`: Para la manipulación de datos y el análisis financiero.
  - `boto3`: Para interactuar con los servicios de AWS (S3).
  - `requests`: Para realizar peticiones HTTP a la API de Alpha Vantage.

####  Instala las Dependencias
Instala las dependencias necesarias:
- pip install -r requirements.txt
