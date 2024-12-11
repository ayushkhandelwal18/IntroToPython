
'''f=open("evenum.txt","w")
nums=[1,3,5,50,9,40,50,60,66,33,31,12,0]
#data string form me jayega isliye ese krna hai
numasstring=" ".join(map(str, nums))
f.write(numasstring)'''

count = 0  
f = open("evenum.txt", "r")  
data = f.read()  

#yadi txt file me , lga rkaha hai to split by comma kardo
nums = data.split(",")  
for val in nums:
    if int(val) % 2 == 0:  
        count += 1 

f.close() 
print(count)