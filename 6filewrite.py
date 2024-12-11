#overwrite krega pahle ka data delte krke new likh dega 
f=open("demo.txt","w")
f.write("I am now learning python for lab exam")

#append krenge matlab end me likh dega
f=open("demo.txt","a")
f.write("\nI am completed python course.")

#yaadi koe file nahi bani hue to
#ham write (w ,a) mode me open 
#krenge to file create ho jayegi

nf=open("newfile.txt","w")
nf.write("New file banadi\ndirect write mode me open krke")
nf.close()


f.close()