
# ipsep

A CLI tool made with Python to bulk differentiate private from public ips.

# Usage

`python ipsep.py -h`

```
usage: ipsep [-h] -f FILE [-o OUT]

A simple tool to differentiate private ips from public ips.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing IPs to parse. Input must be a file containing only one IP per line.
  -o OUT, --out OUT     Name of the output file. If this is not defined, result will be printed to stdout

made by aerodiduch. https://github.com/aerodiduch
```

Input file must have one ip per line, for example:

`my_ip_file.txt`
```
22.93.11.31
180.212.134.0
182.185.9.194
133.160.248.129
54.56.183.241
70.218.26.140
250.220.30.159
209.59.84.106
255.14.218.192
249.88.35.23
157.179.252.49
205.180.13.138
172.123.123.12
192.168.1.1
```

## Usage example

Using aforementioned file `my_ip_file.txt`

`python ipsep.py -f my_ip_file.txt -o filteredips.txt`

`filteredips.txt`
```
*****PRIVATE IPS*****
172.123.123.12
192.168.1.1
-----PUBLIC IPS-----
180.212.134.0
54.56.183.241
157.179.252.49
133.160.248.129
22.93.11.31
205.180.13.138
209.59.84.106
249.88.35.23
250.220.30.159
182.185.9.194
255.14.218.192
70.218.26.140
```

If you didn't specify an output file, the result of the script will be printed to ``stoud``


## Authors

- [@aerodiduch](https://www.github.com/aerodiduch)

