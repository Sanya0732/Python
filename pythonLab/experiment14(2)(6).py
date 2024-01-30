print(" initial Salary  : ")
initialSalary = int(input())
print(" percentage increase(in %) : ")
percentageIncrease = int(input())
print(" number of year (experience) : ")
years = int(input())

for i in range(1,years+1):
    increment = initialSalary*(2/100)
    initialSalary = initialSalary+increment
    print(" salary for: ",i ," is ", initialSalary)

