import os 
filepath= os.listdir('./textfiles')
for path in filepath:
    content=open('./textfiles/' + path,'r').readlines()
    linecount=len(content)
    
    print(path, ": linecount: ",linecount)