# import collections
# import itertools
# import sys

# sys.setrecursionlimit(10000)

# #os.chdir('../../aoc2017')
# print(os.getcwd())
# print(os.listdir())
# data = open('day9.txt').read().strip()

# def process_stream(s,val=1):
#     if not s: return 0
#     first, rest = s[0], s[1:]
#     if first == '{':
#         return val + process_stream(rest,val + 1)
#     elif first == '}':
#         return process_stream(rest, val - 1)
#     else:
#         return process_stream(rest,val)

# print(process_stream(data))

import re

def process_pva(p,v,a):
    v = vector_process(v,a)
    p = vector_process(v,p)
    return (p,v,a)

def vector_abs_add(*v):
    return sum(abs(sum(transposed)) for transposed in zip(*v))

# print(tick(*tick(*tick((3,0,0),(2,0,0),(-1,0,0)))))
def parse_pva(pva):
    parsed = re.findall(r'<(.*?)>',pva)
#     [list(map(int,p.split(','))) for p in parsed]
    return [[int(n) for n in p.split(',')] for p in parsed]

pvas = list(map(parse_pva,data))
for tick in pvas:
    print(process_pva(*tick),len(tick))
