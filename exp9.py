
f=open("python.txt","r")
print(f.readlines())
f.close()
f=open("python.txt","a")
f.write("cancel it")
f.close()
f=open("python.txt","r")
print(f.readlines())
f.close()
f=open("python.txt","r")
print(f.readlines())
f.close()

