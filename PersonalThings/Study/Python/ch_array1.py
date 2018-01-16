userin = raw_input()
userin = userin.split(' ')
jrow = int(userin[0])
jcol = int(userin[1])
mlist = [[ 0 for r in range(jcol)] for c in range(jrow)]
value = 1
for row in range(jrow):
  for col in range(jcol):
    mlist[row][col] = value
    value += 1

for curlist in mlist:
  for v in curlist:
    print "{} ".format(v),
  print ""