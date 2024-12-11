f=open("demo.txt","r")

#data=f.read(10)
#print(data)
#print(type(data))

line1=f.readline()
print(line1)

line2=f.readline()
print(line2)

data=f.read()
print(data)


f.close()