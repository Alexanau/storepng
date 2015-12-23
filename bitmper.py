#!/usr/bin/python
import Image
import sys
import math
def minsq(x):
  return int(math.sqrt(x)+1)

def align(x):
  return (x+(8-x%8))

def bits(ch):
  for b in reversed(xrange(8)):
    yield (ch >>b) & 1

X = 16
Y = 16
data = []
size = 0;
for line in sys.stdin:
  for ch in line:
    for b in bits(ord(ch)):
      data.append(b)
      size += 1


X = align(minsq(size))
Y = minsq(size)
print "C", size/8
print ' ',X*Y/8,"<--avalable"
print "X",X
print "Y",Y

im = Image.new('RGB',(X,Y),(255,255,255))
i = 0
for y in range(Y):
  for x in range(X):
    if i<len(data) and data[i]:
      im.putpixel((x,y),(0,0,0))
    i+=1
  
if len(sys.argv)>1:
  im.save(sys.argv[1] + ".png", "PNG")
