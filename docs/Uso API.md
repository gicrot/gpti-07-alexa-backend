# Documentación de USO API

## Requisitos

Para poder ejecutar de manera correcta la API es necesario tener instalado *python*, al menos la versión 3.6.0. Además, es necesario tener instaladas las siguientes librerías:
- *json*
- *os*
- *requests*

Las primeras dos son librerías estándar de python, por lo que no es necesario instalarlas. En el caso de *requests*, es necesario instalarla mediante el comando `pip install requests`.

## Uso

La API recibe inputs en forma de *queryStringParameters*, generado a partir del *query* que se le entregará a Alexa, los cuales deben ser enviados en formato *json*. con contenido de forma similar a la siguiente:

```event
{
 "queryStringParameters": {
            "comuna": <comuna pedida>,
            "comuna2": <comuna pedida>,
            "comuna3": <comuna pedida>,
            "bencina": <bencina pedida>
        }
}
```

Donde *comuna*, *comuna2* y *comuna3* son un string que representa la comuna de la cual se quiere obtener el precio de la bencina, siendo los dos últimos opcionales, y *bencina* es un string que representa el tipo de bencina que se quiere obtener el precio.

Para los tipo *comuna* se espera que el string sea el nombre de una comuna real existente en Chile. Por ejemplo, la comuna de *San Joaquín*.

Para *bencina* se espera que el string sea uno de los siguientes: *93*, *95*, *97*, *diesel* o *petroleo*. 

### Caso de éxito
En caso que ambos sean correctos, el output entregará los 3 mejores locales (más baratos), entregando para cada uno el distribuidor, ubicación y precio para la bencina pedida en la comuna pedida, además de un código de éxito *200* de esta forma:

```output
{
    "statusCode": 200,
    "body": [{
        "distribuidor": <distribuidor1>,
        "dirección": <dirección1>,
        "bencina": <bencina pedida1>,
        "precio": <precio1>
      },
      {
        "distribuidor": <distribuidor2>,
        "dirección": <dirección2>,
        "bencina": <bencina pedida2>,
        "precio": <precio2>
      },
      {
        "distribuidor": <distribuidor3>,
        "dirección": <dirección3>,
        "bencina": <bencina pedida3>,
        "precio": <precio3>
      }
    ]
}
```

### Caso error sin parámetros

En caso que no se envíen los parámetros al hacer la llamada, o que estén incompletos, se entregará el siguiente mensaje de error:
  ```output
  {
      "statusCode": 400,
      "body": {
          "error": "Not found query params"
      }
  }
  ```

### Caso error sin comunas

En caso que no se envíen las comunas al hacer la llamada, se entregará el siguiente mensaje de error:
  ```output
  {
      "statusCode": 400,
      "body": {
          "error": "Indica al menos una comuna"
      }
  }
  ```

### Caso error por comuna
En caso que la comuna entregada no exista, o se haya entregado el nómbre de una fórma no válida, se entregará el siguiente mensaje de error como respuesta:
  
  ```output
  {
      "statusCode": 400,
      "body": {
          "error": "Comuna <comuna entregada> no encontrada"
      }
  }
  ```

### Caso error por bencina
De manera similar, si el tipo de bencina entregado no se encuentra entre las opciones válidas (*93*, *95*, *97*, *diesel* o *petroleo*), se entregará el siguiente mensaje de error como respuesta:


```output
{
    "statusCode": 400,
    "body": {
        "error": "Tipo de bencina <bencina entregada> no encontrada"
    }
}
```
