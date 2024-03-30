import module1
ar=[]
num=int(input("Enter max number:\n"))
for i in range (1,num):
    member=int(input("Enter new member:\n"))
    ar.append(member)
    if(member==num):
        break
print(ar[0])
module1.len(ar)
print("Done")
