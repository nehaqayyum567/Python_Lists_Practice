#Create a list of 10 random numbers.

numbers = [10 , 80 , 45, 67, 82, 61, 23, 76, 43, 52]
print("Original numbers are: ", numbers)

#Slice the first 5 and last 5 numbers separately

first_five = numbers[0 : 5]
print("first_five numbers are", first_five)
last_five = numbers[-5:]
print("last_five numbers are:", last_five)

#Sort the list in ascending order, then in descending order.

numbers.sort()
print("ascending_order is:", numbers)

descending_order = numbers.sort(reverse = True)
print("descending_order is:", numbers)

#Remove one element using remove() and another using pop().
numbers.remove(45)
print(numbers)

numbers.pop(1)
print(numbers)