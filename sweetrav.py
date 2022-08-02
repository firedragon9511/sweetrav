import argparse
from argparse import RawTextHelpFormatter
from ast import arg
import fileinput
import sys
import os

banner = '''

          __    __    _______                  _                   
         / /   / /   / / ____|                | |                  
        / /   / /   / / (_____      _____  ___| |_ _ __ __ ___   __
       / /   / /   / / \___ \ \ /\ / / _ \/ _ \ __| '__/ _` \ \ / /
  _ _ / / _ / / _ / /  ____) \ V  V /  __/  __/ |_| | | (_| |\ V / 
 (_|_)_(_|_)_(_|_)_/  |_____/ \_/\_/ \___|\___|\__|_|  \__,_| \_/  
                                                                                                                                                                                                                                                                  
                                              
../../../../../../by_firedragon9511
                                              
'''
parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)

parser.add_argument('-p','--path', dest='path', action='store', type=str, help='Specify current folder.', required=False)
parser.add_argument('-d','--depth', dest='depth', action='store', type=int, help='Generate using depth.', required=False)
parser.add_argument('-s','--separator', dest='separator', action='store', type=str, help='Custom separator.', required=False, default='/')
parser.add_argument('-r','--range', dest='range', action='store', type=str, help='Generate a list, ex.: 1-10.', required=False, default='/')
parser.add_argument('-a','--append', dest='append', action='store', type=str, help='Append to final.', required=False, default='')
parser.add_argument('-f','--fuzz', dest='fuzz', action='store', type=str, help='Fuzz script, ex.: -f "./script.sh FUZZ".', required=False)

parser.add_argument('-i', dest='stdin', help='Use stdin pipe.', action='store_true')


args = parser.parse_args()

def fuzz(payload):
    cmd = str(args.fuzz).replace('FUZZ', payload)
    if args.fuzz is not None:
        os.system(cmd)
        pass

def gen_traversal(count, separator = '/'):
    result = ""
    for i in range(0,count):
        result = result + '../'

    
    result = result.replace('/', separator)
    #fuzz(result)
    return result


def back_root(path, separator = '/'):
    if '\\' in path:
        path.replace('\\', '')

    if path[-1] == '/':
        path = path[:-1]

    result = gen_traversal(path.count('/'),  separator=separator)
    #fuzz(result)
    return result

def from_list(lst, separator = '/', append = ''):
    for l in lst:
        res = back_root(l.rstrip(), separator) + append
        fuzz(res)
        print(res)

def range_list(rng, separator = '/', append = ''):
    mi = 0
    mx = 0

    if '-' in rng:
        rng = rng.split('-')
        mi = int(rng[0])
        mx = int(rng[1])
    else:
        mx = int(rng)

    for i in range(mi, mx + 1):
        res = gen_traversal(i, separator) + append
        fuzz(res)
        print(res)


stdin_input = []


if args.stdin:
    for line in sys.stdin:
        stdin_input.append(line)
        pass

if len(stdin_input) >= 1:
    from_list(stdin_input, args.separator, args.append)
    exit()

if args.path is None and args.depth is not None:
    print(gen_traversal(args.depth, args.separator) + args.append)
    exit()

if args.path is None and args.range is not None:
    range_list(args.range, args.separator, args.append )
    exit()

print(back_root(args.path,  args.separator) + args.append)
