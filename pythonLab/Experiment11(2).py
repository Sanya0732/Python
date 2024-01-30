print("enter the first side of your triangle ")
longestSide=int(input())
print("enter the second side of your triangle ")
secondSide=int(input())
print("enter the third side of your triangle ")
thirdSide=int(input())



if(longestSide**2 == (secondSide**2 + thirdSide**2)):
    print("it is an right angle triangle")
else:
    print("it is not an right angle triangle ")



