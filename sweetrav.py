#!/usr/bin/python3

import argparse
from argparse import RawTextHelpFormatter
from ast import arg
import base64
import urllib.parse
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

parser.add_argument('-p','--path', dest='path', action='store', type=str, help='specify current folder.', required=False)
parser.add_argument('-d','--depth', dest='depth', action='store', type=int, help='generate using depth.', required=False)
parser.add_argument('-s','--separator', dest='separator', action='store', type=str, help='custom separator.', required=False, default='/')
parser.add_argument('-r','--range', dest='range', action='store', type=str, help='generate a list. Ex.: 1-10.', required=False, default='/')
parser.add_argument('-a','--append', dest='append', action='store', type=str, help='append to final.', required=False, default='')
parser.add_argument('-A','--Append', dest='Append', action='store', type=str, help='append to final using list. Ex.: -r 1-10 -A files.txt', required=False)
parser.add_argument('-f','--fuzz', dest='fuzz', action='store', type=str, help='fuzz script. Ex.: -f "./script.sh FUZZ".', required=False)
parser.add_argument('-e','--encoding', dest='encoding', action='store', type=str, help='Available encodings: urlencode, doubleencode, base64.', required=False)
parser.add_argument('-o','--output', dest='output', action='store', type=str, help='Save output to a file (append).', required=False)



parser.add_argument('-t','--trim', dest='clear', help='replace duplicated bars.', action='store_true')
parser.add_argument('-i', dest='stdin', help='use stdin pipe.', action='store_true')



args = parser.parse_args()



def prnt(payload, ignoreFuzz = False):
    global output_file

    if args.clear:
        payload = payload.replace('//','/').replace('\\\\', '\\')

    if args.encoding is not None:
        if args.encoding == 'base64':
            payload = base64.b64encode(payload.encode('ascii')).decode('ascii')
        if args.encoding == 'urlencode':
            payload = urllib.parse.quote(payload)
        if args.encoding == 'doubleencode':
            payload = urllib.parse.quote(urllib.parse.quote(payload))

    if args.output is not None:
        output_file.write(payload + '\n')

    if not ignoreFuzz:
        fuzz(payload)

    print(payload)
    

def fuzz(payload):
    cmd = str(args.fuzz).replace('FUZZ', payload)
    if args.fuzz is not None:
        os.system(cmd)
        pass

def gen_traversal(count, separator = '/', ignoreAppend = False):
    result =  "../" * int(count)

    if args.Append is not None and not ignoreAppend:
        data = read_file(args.Append)
        for d in data:       
            res = ("../" * count) + d
            prnt(res.replace('/', separator))
            #fuzz(res.replace('/', separator))
            #print(res.replace('/', separator))
        return ''
    else:
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
        prnt(res)
        #fuzz(res)
        #print(res)

def read_file(path):
    f = open(path, 'r')
    data = f.read().split('\n')
    f.close()
    return data

def range_list(rng, separator = '/', append = ''):
    mi = 0
    mx = 0

    if '-' in rng:
        rng = rng.split('-')
        mi = int(rng[0])
        mx = int(rng[1])
    else:
        mx = int(rng)

    if args.Append is not None:
        data = read_file(args.Append)
        for d in data:
            for i in range(mi, mx + 1):
                res = gen_traversal(i, separator, ignoreAppend=True) + d
                prnt(res)
                #fuzz(res)
                #print(res)
        return


    for i in range(mi, mx + 1):
        res = gen_traversal(i, separator) + append
        prnt(res)
        #fuzz(res)
        #print(res)

    return


stdin_input = []
output_file = None

if args.output is not None:
    output_file = open(args.output, 'a+')

if args.stdin:
    for line in sys.stdin:
        stdin_input.append(line)
        pass

if len(stdin_input) >= 1:
    from_list(stdin_input, args.separator, args.append)
    exit()

if args.path is None and args.depth is not None:
    prnt(gen_traversal(args.depth, args.separator) + args.append, ignoreFuzz=True)
    exit()

if args.path is None and args.range is not None:
    range_list(args.range, args.separator, args.append )
    exit()

prnt(back_root(args.path,  args.separator) + args.append, ignoreFuzz=True )

if output_file is not None:
    output_file.close()
