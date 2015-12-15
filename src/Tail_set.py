'''
Created on Dec 14, 2015

@author: Saikit.Chan
'''
input1 = [float(n) for n in raw_input().split(' ')]
input2 = [float(n) for n in raw_input().split(' ')]

if [x / y for x,y in zip(input1,input1[1:])] >= [x / y for x,y in zip(input2,input2[1:])]:
    print '1'
else:
    print '2'
