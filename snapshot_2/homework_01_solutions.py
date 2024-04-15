# Exercise 1: Write a Python script that prints "Hello, World!" to the console.
print("Hello, World!")
print('-' * 20)

# Exercise 2: Create variables to store your name, age, and favorite color. Then, print out a message using these
# variables.
name = "Stefan"
age = 25
favorite_color = "blue"
print("My name is", name, "I am", age, "years old, and my favorite color is", favorite_color)
print('-' * 20)

# Exercise 3: Write a program that calculates the area of a rectangle.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)
print('-' * 20)

# Exercise 4: Write a program that converts temperatures from Fahrenheit to Celsius.
temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
temperature_celsius = (temperature_fahrenheit - 32) * 5/9
print("Temperature in Celsius:", temperature_celsius)
print('-' * 20)

# Exercise 5: Create a program that asks the user to enter two numbers and then prints out the sum, difference, product,
# and quotient of those numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print('-' * 20)

# Exercise 6: Write a program that prompts the user to enter a radius and then calculates and prints the area and
# circumference of a circle with that radius.
PI = 3.14  # Close enough, alternatively you can import the `math` package and use `math.pi` but we haven't covered this
radius = float(input("Enter the radius of the circle: "))
area = PI * radius ** 2  # Also OK to just use 3.
circumference = 2 * PI * radius
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
print('-' * 20)

# Exercise 7: Create a program that checks whether a given number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
print('-' * 20)

# Exercise 8: Write a program that prompts the user to enter their age and then determines and prints out whether they
# are eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print('-' * 20)

# Exercise 9: Create a program that prompts the user to enter a string and then prints out the length of the string.
string = input("Enter a string: ")
print("Length of the string:", len(string))
print('-' * 20)

# Exercise 10: Write a program that prompts the user to enter two strings and then concatenates them together and prints
# out the result.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
concatenated_string = string1 + string2
print("Concatenated string:", concatenated_string)
print('-' * 20)
