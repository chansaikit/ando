'''
Created on Jan 5, 2016

@author: Saikit.Chan
'''

input_lines = raw_input().split(' ')
x=int(input_lines[0])
y=int(input_lines[1])
z=int(input_lines[2])
n=int(input_lines[3])

arrayx=[0,x]
arrayy=[0,y]

for x in range(n):
    input_lines = raw_input().split(' ')
    d=int(input_lines[0])
    a=int(input_lines[1])
    if not d:
        arrayx.append(a)
    else:
        arrayy.append(a)
 
arrayx.sort()
arrayy.sort() 
x=  min([j-i for i, j in zip(arrayx[:-1], arrayx[1:])])
y=min([j-i for i, j in zip(arrayy[:-1], arrayy[1:])])
print x*y*z