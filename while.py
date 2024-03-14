

#number converted to a float to allow all non integer values to be considered
count = 0
total = 0
number = float(input("Enter a number:"))

#while loop tallies values for count and total until -1 is entered
while number != -1:
    count += 1
    total += number
    number = float(input("Enter another number:"))

#prevent division by zero error
if count == 0:
    count = 1

print(total/count) 
