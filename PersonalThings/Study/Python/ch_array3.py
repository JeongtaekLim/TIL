# -*- coding: utf-8 -*-

userin = raw_input()
jsize = int(userin[0])
mlist = [[ -1 for col in range(jsize)] for row in range(jsize)]
valule = 1

curPos = [0, 0]
ROW = 0
COL = 1

value = 1
# curCol -> [0, 1, 2]
for curCol in range(jsize):
  # curRow -> [0, 1, 2, 3, 4]
  for curRow in range(curCol+1):
    curPos = [curRow, curCol - curRow]
    print curPos
    mlist[curPos[ROW]][curPos[COL]] = value
    value += 1

for row in mlist:
  for value in row:
    if value > 0:
      print "{} ".format(value),
  print ''
  