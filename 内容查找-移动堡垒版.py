import os
a=input("dir:")
b=input("text:")
for dir,_,files in os.walk(a):
    for filename in files:
        file_path=os.path.join(dir,filename)
        with open(file_path,'rb') as f:
            content=str(f.read())
            if b in content:
                print(f"found!dir:{file_path}")

input()
