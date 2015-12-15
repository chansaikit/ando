'''
Created on Dec 14, 2015

@author: Saikit.Chan
'''
# coding: utf-8  
input_lines = raw_input()
n=int(input_lines)
total=str(n)
for i in range(n-1,0,-1):  
    total = str(int(total) * i).strip('0')[-10:]
print total[-9:].strip('0') 