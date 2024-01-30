print("Initial number of organisms: ")
initialPopulation = int(input())
print("Rate of growth of organisms (rate > 0): ")
rateOfGrowth = float(input())
print("Number of hours it takes to achieve this rate: ")
hoursToAchieveRate = int(input())
print("Number of hours during which the population grows: ")
numberOfHoursToGrow = int(input())
print("Total number of hours: ")
totalHours = int(input())

hoursElapsed = 0
population = initialPopulation

while hoursElapsed < totalHours:
    if hoursElapsed < numberOfHoursToGrow:
        population *= rateOfGrowth ** (hoursElapsed // hoursToAchieveRate)
    else:
        population *= rateOfGrowth ** (numberOfHoursToGrow // hoursToAchieveRate)
    hoursElapsed += hoursToAchieveRate

print("Total population after", totalHours, "hours:", int(population))
