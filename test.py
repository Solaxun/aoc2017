import collections
import itertools
import sys

sys.setrecursionlimit(10000)

#os.chdir('../../aoc2017')
print(os.getcwd())
print(os.listdir())
data = open('day9.txt').read().strip()

def process_stream(s,val=1):
    if not s: return 0
    first, rest = s[0], s[1:]
    if first == '{':
        return val + process_stream(rest,val + 1)
    elif first == '}':
        return process_stream(rest, val - 1)
    else:
        return process_stream(rest,val)

print(process_stream(data))
