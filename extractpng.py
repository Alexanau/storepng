#!/usr/bin/python
import Image
import sys
import math
import getopt as g

optlist, args = g.getopt(sys.argv[1:],'o:')
output = ''
for o,a in optlist:
  if o == '-o':
    output = a

filename = ''
if len(args)>0:
  filename = args[0]
else:
  print "No file given"
  exit(1);

im = Image.open(filename)
X,Y = im.size
fh = sys.stdout
if len(output)>0:
  fh=open(output,'w')

for y in range(Y):
  for x in range(X):
    r,g,b = im.getpixel((x,y))
    fh.write(chr(r))
    fh.write(chr(g))
    fh.write(chr(b))

fh.close()
