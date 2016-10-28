__author__ = 'taek6'
anstable =[]
for i in range(22):
    anstable.append(0)
userin = raw_input()
userin = userin.split(" ")
t1 = int(userin[0])
t2 = int(userin[1])
n = int(userin[2])
anstable[1]=t1
anstable[2]=t2
for i in range(3,n+1):
    anstable[i] = anstable[i-2]+anstable[i-1]*anstable[i-1]
print(anstable[n])
