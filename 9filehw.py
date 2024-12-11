#f=open("hw1.txt","w")
#f.write("I learn python")
#f.write("\nI learn file handling")

#->jha pe bhi file me learn likha hai vha done likhna hai
'''f=open("hw1.txt","r")
data=f.read()

new_data=data.replace("learn","done")
print(new_data)

#replace to krdiya ab overwrite krdenge newdata ke sath 
f=open("hw1.txt","w")
f.write(new_data)'''

#->file me handling word search krna hai
'''f=open("hw1.txt","r")
data=f.read()

word="handling"

if(data.find(word)!=-1):
    print("Found")
else:
    print("not found")'''

#->file me handling word sabse pahle kis line me aa rha hai
def check_for_line():
    word="handling"
    data=True
    lineNo=1
    f=open("hw1.txt","r")
    while data:
        data=f.readline()
        if(word in data):
            print(lineNo)
            return
        lineNo+=1
    return -1

check_for_line()