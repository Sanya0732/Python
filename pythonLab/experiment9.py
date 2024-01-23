print(" Name : Sanya Srivastava")
print(" Class : IT-B1 ")
print(" URN : 2203889")

print("HOURLY WAGE")
hourly_wage = int(input())
print(" total number of regular hours : ")
regular_hours = int(input())
print(" Over time if any : ")
over_time = int(input())
total_overTimePay = over_time * (1.5*hourly_wage)
totalWeeklyPay = (hourly_wage*regular_hours)+total_overTimePay
print("total weekly pay: ",totalWeeklyPay)

