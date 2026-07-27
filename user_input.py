#Ask the user to enter 5 numbers.

numbers = input("Enter 5 numbers separetd by space:").split()
print("Your list is:", numbers)

#Sort the list.
numbers.sort()
print("ascending order is:", numbers)

#Print the first and last element using slicing.

first_element = numbers[:1]
print("first element is:", first_element)

last_element = numbers[-1:]
print("last element is:", last_element)

#Remove the smallest number and print the updated list.
 
numbers.pop(0)
print("updated list is:", numbers)