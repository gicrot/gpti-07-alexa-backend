# Documentación de USO API

## Requisitos

Para poder ejecutar de manera correcta la API es necesario tener instalado *python*, al menos la versión 3.6.0

## Uso

La API recibe inputs en forma de *events*, los cuales deben ser enviados en formato *json*. con contenido de forma similar a la siguiente:

```event
{
    "comuna": <comuna pedida>,
    "bencina": <bencina pedida> 
}
```

Donde *comuna* es un string que representa la comuna de la cual se quiere obtener el precio de la bencina, y *bencina* es un string que representa el tipo de bencina que se quiere obtener el precio.

Para *comuna* se espera que el string sea el nombre de una comuna real existente en Chile. Por ejemplo, para la comuna de *San Joaquín*.

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