import re
import sys

# prog = re.compile('([A-Z]\d+)+')
prog = re.compile('flo2d_10_+')

while True:
  line = sys.stdin.readline()
  if not line: break

  if prog.match(line):
    print ('matched')
  else:
    print ('not matched')

# fbakjbg
# not matched
# svsjvsnkv153
# not matched
# SESGSG12
# not matched
# S2
# matched
# D22
# matched
# R222
# matched
# D2DDNYDMYYYYYM
# matched