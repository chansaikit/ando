'''
Created on Dec 14, 2015

@author: Saikit.Chan
'''
N = int(raw_input())+1
M1 = raw_input()
x_M1 = raw_input()
M2 = raw_input()
y_M2 = raw_input()

shelf=[0]*(N) 
output=[]
book=x_M1.split(' ')
buy=y_M2.split(' ') 
for b in book:
    shelf[int(b)] = 1
for b in buy:
    shelf[int(b)] = shelf[int(b)] -1
for b in range(N):
    if shelf[b] < 0:
        output.append(str(b))
        
if not output:
    print 'None'
else:
    print ' '.join(output)