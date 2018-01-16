# -*- coding: utf-8 -*-
# N*M의 2차원 배열이 주어지고, 주어진 2차원 배열의 [A][B]에는 어떠한 값이 있는지 출력하는 프로그램을 작성해보자. 
# (단, 2차원 배열을 활용할 것)

userin = raw_input()
userin = userin.split(' ')
jrow = int(userin[0])
jcol = int(userin[1])

mlist = [[ 0 for col in range(jcol)] for row in range(jrow)]
value = 1

for row in range(jrow):
  userin = raw_input()
  userin = userin.split(' ')
  for col in range(jcol):
    mlist[row][col] = int(userin[col])

userin = raw_input()
userin = userin.split(' ')
print mlist[int(userin[0])][int(userin[1])]