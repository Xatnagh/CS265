import os 
filepath= os.listdir('./textfiles')
total_line=0
for path in filepath:
    content=open('./textfiles/' + path,'r').readlines()
    total_line+=len(content)
    
print('Total line count for all files in textfiles:', total_line)   