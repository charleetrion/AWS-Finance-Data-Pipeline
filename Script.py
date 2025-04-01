import yfinance as yf
import pandas as pd
import boto3
import os
import requests
from io import StringIO


# Configuracion de AWS S3
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET_NAME = "script-finance"

# Configuración de Alpha Vantage y Tiingo
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


def obtener_datos_yfinance(ticker="AAPL", periodo="1mo"):
    # Descargar los datos Historicos desde desde Yahoo Finance
    return yf.download(ticker, period=periodo)
    
def obtener_datos_alphavantage(ticker):
   # Obtiene datos históricos desde Alpha Vantage
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame.from_dict(data.get("Time Series (Daily)", {}), orient='index')

def procesar_datos(df):
    #Verificar si 'Adj Close' o 'Close' están en el DataFrame
    if ('Adj Close', 'AAPL') in df.columns:
        df["Retorno Diario"] = df[('Adj Close', 'AAPL')].pct_change()
    elif ('Close', 'AAPL') in df.columns:
        df["Retorno Diario"] = df[('Close', 'AAPL')].pct_change()
    else:
        print("No se encontró 'Adj Close' ni 'Close' en los datos")
        return None

    return {"media_retorno": df["Retorno Diario"].mean(), "volatilidad": df["Retorno Diario"].std(), "data": df}
 
def guardar_en_s3(df, resultado):
    # Guardar el DataFrame procesado como archivo CSV en S3
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

    file_name = f"datos_financieros_{resultado['data'].index[-1]}.csv"
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=file_name, Body=csv_buffer.getvalue())
    print(f"Datos subidos a S3: {file_name}")

def main():
    """Función principal para descargar, procesar y guardar los datos"""
    # Descargar los datos de las diferentes fuentes
    df_yf = obtener_datos_yfinance("AAPL", "3mo")
    df_av = obtener_datos_alphavantage("AAPL")

    # Concatenar los datos de Yahoo Finance y Alpha Vantage
    df_final = pd.concat([df_yf, df_av], axis=1)

    # Procesar los datos
    resultado = procesar_datos(df_final)
    if resultado:
        guardar_en_s3(df_final, resultado)


if __name__ == "__main__":
    main()