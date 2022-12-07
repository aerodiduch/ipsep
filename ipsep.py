import argparse
import re

re_pattern = r'^(10|192|172).\d+.\d+.\d+'

parser = argparse.ArgumentParser(
    prog='ipdiff',
    description='A simple tool to differentiate private ips from public ips.',
    epilog='made by aerodiduch. https://github.com/aerodiduch'
)

parser.add_argument(
    '-f', '--file',help='File containing IPs to parse. Input must be a file containing only one IP per line.', required=True
)

parser.add_argument(
    '-o', '--out', help='Name of the output file. If this is not defined, result will be printed to stdout',
)

args = parser.parse_args()


def read_file_data(file: str) -> list:
    '''Reads data from the specific file

    Args:
        file (str): Filename to read from

    Returns:
        list: A list containing the ips on the file.
    '''
    ip_list = []
    with open(file, 'r') as fh:
        for line in fh:
            ip_list.append(line.replace('\n', ''))
    return ip_list

def identify_private(ips: list) -> list:
    '''Receives a list of ips and identifies which are private.

    Args:
        ips (list): List of ips

    Returns:
        list: A list containing only private ips.
    '''
    
    filtered_ips = list(filter(lambda v: re.match(re_pattern, v), ips))
    return filtered_ips

def prepare_data(raw_ips: list, filtered_ips: list) -> str:
    '''Preparing the data for its export/printing.

    Args:
        raw_ips (list): A list containing all of the ips
        filtered_ips (list): A list containing only the private ips

    Returns:
        str: Text body ready to be printed/exported to a file
    '''
    
    public_ips = list(set(raw_ips).difference(filtered_ips))
    body = ''
    body += "*"*5 + 'PRIVATE IPS' + '*' *5 + '\n'
    body += "\n".join([i for i in filtered_ips])
    body += '\n' + "-"*5 + 'PUBLIC IPS' + '-' *5 + '\n'
    body += "\n".join([i for i in public_ips])
    return body

def dump_data(data: str, output_file: str):
    '''Dumps data to a file/stdout  

    Args:
        data (str): Data to be exported/printed 
        output_file (str): Optional. Path of the file to be writed.
    '''
    
    if output_file is None:
        print(data)
    else:
        with open(output_file, 'w') as fh:
            fh.write(data)
        print(f'Succesfully exported data to "{output_file}".')



if __name__ == '__main__':
    if args.file:
        ips = read_file_data(args.file)
        filtered_ips = identify_private(ips)
        final_data = prepare_data(ips, filtered_ips)
        dump_data(final_data, args.out)