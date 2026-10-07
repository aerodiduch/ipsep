# ipsep

[![License: MIT](https://img.shields.io/github/license/aerodiduch/ipsep)](LICENSE) ![Python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white)

[Español](README.es.md)

A small command-line tool that splits a list of IP addresses into private and public. Give it a file with one IP per line and it prints the two groups, or saves them to a file.

## Usage

Python 3, no extra packages.

```sh
git clone https://github.com/aerodiduch/ipsep
cd ipsep
python ipsep.py -f my_ips.txt                 # prints the result
python ipsep.py -f my_ips.txt -o result.txt   # saves it to a file
```

With this `my_ips.txt`:

```
10.0.0.5
192.168.1.1
8.8.8.8
```

you get:

```
*****PRIVATE IPS*****
10.0.0.5
192.168.1.1
-----PUBLIC IPS-----
8.8.8.8
```

## Limitations

- It decides by the first number: anything starting with `10`, `172` or `192` counts as private. The real private ranges are narrower (`172.16.0.0` to `172.31.255.255` and `192.168.0.0` to `192.168.255.255`), so an address like `172.123.123.12` or `192.0.2.10` ends up in the private group.
- Public IPs come out in no particular order.

## License

MIT, see [LICENSE](LICENSE).
