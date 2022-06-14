num=int(input("Number of Fabonacci Series "))
if num<3:
   print(":( :(")
   raise SystemExit
   
MyList = []
MyList.append(1)
MyList.append(1)
MyList.append(MyList[0] + MyList[1])

count=len(MyList)-1

while num-3 > 0:
   MyList.append(MyList[count-1] + MyList[count])
   num=num-1
   count=count+1

for i in range(0, len(MyList)-1): 
    print(MyList[i], end=", ")

print(len(MyList))
print("\r")
