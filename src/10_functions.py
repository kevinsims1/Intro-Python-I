# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if(x%2 == 0):
        print("True")

n = 6
print(is_even(n))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even(c):
    if c % 2 == 0:
        print("Even")
    if c % 2 != 0:
        print("Odd")

print(even(num))
# nOTE in my console log i get a recurring None from my last print ask team lead about this 