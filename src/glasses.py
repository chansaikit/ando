'''
Created on Dec 15, 2015

@author: Saikit.Chan
'''
MatrixLen=int(raw_input())
Matrix=[[0 for x in range(MatrixLen)] for x in range(MatrixLen)] 
for k in range(MatrixLen):
    temp = [int(n) for n in raw_input().strip().split(' ')] 
    for i in range(len(temp)): 
        Matrix[k][i]=temp[i]
pattermLen=int(raw_input())
patterm=[[0 for x in range(pattermLen)] for x in range(pattermLen)] 
for k in range(pattermLen):
    temp = [int(n) for n in raw_input().strip().split(' ')]
    for i in range(len(temp)): 
        patterm[k][i]=temp[i] 
        
for x in range(0,MatrixLen-pattermLen+1):
    for y in range(0,MatrixLen-pattermLen+1):
        if Matrix[x][y]==patterm[0][0]:
            match=True
            for k in range(x,x+pattermLen):
                for m in range(y,y+pattermLen):
                    if not Matrix[k][m] == patterm[k-x][m-y]:
                        match=False
                        break
                if not match:
                    break
            if match:
                print x,y
