'''
Created on Dec 14, 2015

@author: Saikit.Chan
 
'''
vote=0
for x in range(5):
    if(raw_input().lower() == 'yes'):
        vote=vote+1
if vote > 2:
    print 'yes'
else:
    print 'no'