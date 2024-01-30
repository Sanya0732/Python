totalNumbers = 0
totalSum = 0

print("Enter numbers separated by spaces. Press Enter when done:")

while True:
    userInput = input()
    if userInput == "":
        break
    else:
            totalNumbers = totalNumbers + 1
            totalSum = totalSum + int(userInput)



print("Total numbers entered:", totalSum)


# if totalNumbers > 0:
#     average = totalSum / totalNumbers
#     print("Average of the numbers:", average)
