# ipsep

[![License: MIT](https://img.shields.io/github/license/aerodiduch/ipsep)](LICENSE) ![Python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white)

[English](README.md)

Una herramienta chica de línea de comandos que separa una lista de direcciones IP en privadas y públicas. Le pasás un archivo con una IP por línea y te muestra los dos grupos, o los guarda en un archivo.

## Uso

Python 3, sin paquetes extra.

```sh
git clone https://github.com/aerodiduch/ipsep
cd ipsep
python ipsep.py -f mis_ips.txt                  # muestra el resultado
python ipsep.py -f mis_ips.txt -o resultado.txt # lo guarda en un archivo
```

Con este `mis_ips.txt`:

```
10.0.0.5
192.168.1.1
8.8.8.8
```

sale:

```
*****PRIVATE IPS*****
10.0.0.5
192.168.1.1
-----PUBLIC IPS-----
8.8.8.8
```

## Limitaciones

- Decide por el primer número: todo lo que empieza con `10`, `172` o `192` cuenta como privado. Los rangos privados de verdad son más chicos (`172.16.0.0` a `172.31.255.255` y `192.168.0.0` a `192.168.255.255`), así que una dirección como `172.123.123.12` o `192.0.2.10` queda en el grupo de las privadas.
- Las IP públicas salen sin un orden fijo.

## Licencia

MIT, ver [LICENSE](LICENSE).
