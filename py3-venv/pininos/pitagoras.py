## TRYIT: Import the required math functions
import math
# TRYIT: Create variables to store the triangle sides input by the user
# TRYIT: Use the int() function to convert the input string values to integers

slide1=int(input("What is the first slide of the triangle"))
slide2=int(input("What is the second slide of the triangle"))

# TRYIT: Calculate the values
slidelen = int(math.sqrt((slide1**2)+(slide2**2)))
angle = int(math.degrees(math.atan(slide1/slide2)))

# TRYIT: Create a Boolean variable to store true or false if the slide length meets safety standards
slidesafe = False
# TRYIT: Create an if...elif...else statement to test the measurements of the slide

if angle > 40:
    slidesafe = False
elif slide1 > 6:
    slidesafe = False
else:
    slidesafe = True

# TRYIT Use an if...else statement to test whether the Boolean variable is True or False, and print the results
if slidesafe == True:
    print("Safe! The angle is: " + str(angle) + " degrees and your slide length is: " + str(slidelen))
else:
    print("Unsafe! The angle is: " + str(angle) + " degrees and your slide length is: " + str(slidelen))

