'''
Created on Dec 18, 2015

@author: Saikit.Chan
'''
input_lines = int(raw_input()) 
print reduce(lambda x,y: x*y, range(1,input_lines+1))