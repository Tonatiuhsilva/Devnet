# Fill in this file with the code from the introduction to Python
import math
import random
# TRYIT: Write a print statement that displays both the type and value of Pi
print("pi is", type(math.pi), "with a value of", math.pi)
# TRYIT: Write a conditional to print out if `i` is less than or greater than 50
i=20

if i<=50:
  print("i is not greater than 50")
elif i>50:
  print("i is greater than 50")
# TRYIT: Write a conditional that prints the color of the picked fruit

picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("The fruit is orange")
elif picked_fruit == 'strawberry':
    print("The fruit is red")
elif picked_fruit == 'banana':
    print("The fruit is yellow")

# TRYIT: Write a function that multiplies two numbers and returns the result

def multiply(num1, num2):
    """Multiply two numbers and return the result."""
    result = num1 * num2
    return result
# TRYIT: Now call the function a few times to calculate the following answers
print("12 x 96 =", multiply(12, 96))
print("48 x 17 =", multiply(48, 17))
print("196523 x 87323 =", multiply(196523, 87323))
