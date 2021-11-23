# Bubble_Sort


Percentage = []
number = int(input("Enter Total Number of Students:\n"))
for i in range(number):
    value = float(input("Enter Percentage:\n "))
    Percentage.append(value)

for i in range(number-1):
    for j in range(number-i-1):
        if (Percentage[j]>Percentage[j+1]):
            temp = Percentage[j]
            Percentage[j] = Percentage[j+1]
            Percentage[j+1] = temp

print("The Top scores are:",Percentage)
minimum = len(Percentage)-6
maximum = len(Percentage)-1
index = 1
for i in range(maximum,minimum,-1):
    if i>=0:
        print(f"{index} Top Scorer:",Percentage[i],"\n")
        index+=1
