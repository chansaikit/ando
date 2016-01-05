'''
Created on Jan 5, 2016

@author: Saikit.Chan
'''
n = int(raw_input())
m = int(raw_input()) 

array=['R'*n for i in range((m/n)+1)]
array[1::2] = [('W' *n)] * (int(len(array)/2))  
print ''.join(array)[:m]