import multiprocessing as mp
import sys

print('Get data from stdin:')
s = input('Input smth:')
print('Upload data to stdout: ', s)
print('Upload data to stderr: ', s, file=sys.stderr)
