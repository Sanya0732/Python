sum=0
count=0
print("the total numbers u want to add : ")
while(True):
    num = int(input())
    sum=sum+num
    count=count+1
print("the number of count to enter number is finished")

print("sum is ",sum)
if(count>0):
   average = sum/count
   print(average)



