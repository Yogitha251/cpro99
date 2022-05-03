import os
import shutil
import stat
import time

path='C:\Users\veena\OneDrive\Pictures\Saved Pictures'

days=3
seconds=time.time()-(days*24*60*60)


list=os.listdir(path)
print(list)

for file in list:
    name,ext=os.path.splitext(file)
    #print(name)
    #print(ext)
    
    ext=ext[1:]
    
    #print(ext[1:2])

    
    if ext=='':
        continue

    if os.path.exists(path+'/'+ext):
      # shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
      for folders,files in os.walk(path):
          

    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)