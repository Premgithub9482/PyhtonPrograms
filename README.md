## Python Program to Add Two Numbers
This Python program demonstrates two methods for adding two numbers:

### Method 1: Using Pre-defined Variables
In this method, two pre-defined variables (`num1` and `num2`) are assigned with numeric values (in this case, `20` and `10`). The sum of these two numbers is then calculated and printed to the console using the `print` statement.

### Method 2: User Input for Dynamic Calculation
In this method, the program prompts the user to input two numeric values, either integers or floating-point numbers. The `float()` function is used to convert the user input to floating-point numbers, allowing for the addition of both integer and decimal values. The sum is then calculated and displayed using the `print` statement.

### Example Output
For both methods, the result is printed to the console, showcasing the sum of the given numbers.
This simple program serves as an introductory example for basic arithmetic operations in Python and demonstrates the use of both pre-defined variables and user input for dynamic calculations.

-------------------------------------------------------------------------------------------
## Python Program to Calculate Square Root
This Python program illustrates two methods to calculate the square root of a given integer:

### Method 1: Using the `math` Module
The program utilizes the `math` module, which provides a `sqrt()` function. In this method, the user is prompted to input an integer, and the square root of the entered number is calculated using the `math.sqrt()` function. The result is then printed to the console.

### Method 2: Using Exponential Operator
In this method, the program prompts the user to input an integer. The square root is calculated using the exponential operator (`**`), with the exponent set to `0.5`. This method demonstrates an alternative approach to calculating the square root without relying on external modules. The result is printed to the console.

### Example Output
For both methods, the program prints the square root of the entered integer to the console.
This program serves as a simple example to showcase different approaches for calculating the square root in Python. 
-------------------------------------------------------------------------------------------

## Python Program to Calculate the Area of a Triangle
This Python program calculates the area of a triangle using the formula: ((height*base)/2)

### Method:
1. The program prompts the user to input the height and base of the triangle, both represented as floating-point numbers.
2. The area of the triangle is then calculated using the formula ((height*base)/2)
3. The result is printed to the console.

### Example Output:
For the given height and base values, the program calculates and displays the area of the triangle.
This program serves as a basic example of calculating the area of a triangle in Python. You can use and modify this code as needed for your own projects or educational purposes.
-------------------------------------------------------------------------------------------

## Python Program to Swap Two Variables
This Python program demonstrates two methods for swapping the values of two variables.

### Method 1: Using a Temporary Variable
1. Two variables (`var1` and `var2`) are initialized with numeric values.
2. The values of the variables are displayed before the swap.
3. A temporary variable (`temp_var`) is used to store the value of `var1`.
4. The value of `var1` is then updated with the value of `var2`.
5. Finally, the value of `var2` is updated with the value stored in the temporary variable.
6. The program displays the values of the variables after the swap.

### Method 2: Without Using a Temporary Variable
1. Two variables (`var1` and `var2`) are initialized with numeric values.
2. The values of the variables are displayed before the swap.
3. The values of `var1` and `var2` are swapped directly using a tuple unpacking assignment (`var1, var2 = var2, var1`).
4. The program displays the values of the variables after the swap.

### Example Output
For both methods, the program prints the values of the variables before and after the swap, demonstrating the swapping of variable values.
-------------------------------------------------------------------------------------------

## Python Program to Convert Kilometers to Miles
This Python program converts a distance value from kilometers to miles using the conversion factor: 1 kilometer = 0.621371 miles.

### Method:
1. The program prompts the user to input a distance value in kilometers, represented as a floating-point number.
2. The distance in miles is calculated by multiplying the input kilometers by the conversion factor (0.621371).
3. The program displays the original value in kilometers and the equivalent value in miles.

### Example Output:
For the given input in kilometers, the program calculates and prints the equivalent value in miles.
-------------------------------------------------------------------------------------------

## Python Program to Check if a Number is Positive, Negative, or Zero
This Python program determines the nature of a given numeric input—whether it is positive, negative, or zero.

### Method:
1. The program prompts the user to input a number, which is represented as a floating-point value.
2. Using an `if-elif-else` structure, the program checks the value of the input:
    - If the number is greater than 0, it is classified as a positive number.
    - If the number is equal to 0, it is classified as zero.
    - If the number is less than 0, it is classified as a negative number.
3. The program prints the result based on the classification.

### Example Output:
For the given input number, the program determines and prints whether it is positive, negative, or zero.
This program provides a fundamental example of using conditional statements in Python to analyze and categorize numeric values. 
-------------------------------------------------------------------------------------------

## Python Program to Check if a Number is Odd or Even
This Python program determines whether a given integer is odd or even.

### Method:
1. The program prompts the user to input an integer.
2. Using the modulo operator (`%`), the program checks if the remainder when dividing the input by 2 is zero.
    - If the remainder is zero, the number is classified as an even number.
    - If the remainder is not zero, the number is classified as an odd number.
3. The program prints the result based on the classification.

### Example Output:
For the given input integer, the program determines and prints whether it is odd or even.
This program demonstrates a basic use of conditional statements in Python to determine the parity of an integer. 
-------------------------------------------------------------------------------------------

## Python Program to Check if a Year is a Leap Year
This Python program determines whether a given year is a leap year or not.

### Method:
1. The program prompts the user to input a year as an integer.
2. Using conditional statements, the program checks the conditions for a leap year:
    - If the year is divisible by 400 and also divisible by 100, it is a leap year.
    - If the year is divisible by 4 but not divisible by 100, it is a leap year.
    - If the year does not meet the above conditions, it is not a leap year.
3. The program prints the result based on the leap year classification.

### Example Output:
For the given input year, the program determines and prints whether it is a leap year or not.
This program provides a basic example of determining leap years in Python based on the rules of the Gregorian calendar. 
-------------------------------------------------------------------------------------------

## Python Program to Find the Largest Among Three Numbers
This Python program determines the largest among three given numbers.

### Method:
1. The program prompts the user to input three numbers as floating-point values.
2. Using conditional statements, the program compares the numbers to find the largest one:
    - If `num1` is greater than both `num2` and `num3`, then `num1` is the largest.
    - If `num2` is greater than both `num1` and `num3`, then `num2` is the largest.
    - Otherwise, `num3` is the largest.
3. The program prints the result indicating the largest number among the three.

### Example Output:
For the given input numbers, the program determines and prints the largest among them.
This program demonstrates a basic use of conditional statements in Python to compare numbers and find the largest among them.
-------------------------------------------------------------------------------------------

## Python Program to Check if a Number is Prime
This Python program determines whether a given integer is a prime number or not.

### Method:
1. The program prompts the user to input an integer.
2. The program checks if the input is equal to 1. If so, it declares that 1 is not a prime number.
3. If the input is greater than 1, the program uses a `for` loop to iterate from 2 to the input number (exclusive).
4. Inside the loop, the program checks if the input number is divisible by any number in the iteration range.
    - If it is divisible, the program declares that the number is not a prime number and breaks out of the loop.
5. If the loop completes without finding a divisor, the program declares that the number is a prime number.
6. The program prints the result based on the prime number classification.

### Example Output:
For the given input number, the program determines and prints whether it is a prime number or not.
This program provides a basic example of checking prime numbers in Python using a loop and conditional statements.
-------------------------------------------------------------------------------------------

## Python Program to Generate a Random Number
This Python program allows the user to interactively generate random numbers between 1 and 100. The user is presented with a menu to either generate a random number or exit the program.

### Method:
1. The program utilizes the `random` module to generate random integers.
2. Inside a `while` loop, the user is prompted to choose an option:
   - Press "1" to generate a random number between 1 and 100.
   - Press "2" to exit the program.
3. If the user selects "1," a random number is generated and displayed.
4. If the user selects "2," the program breaks out of the loop, terminating the execution.
5. For any other input, an "invalid choice" message is displayed.

### Example Output:
The program provides an interactive experience, allowing the user to generate random numbers or exit the program based on their choice.
This program showcases the use of loops, conditional statements, and the `random` module in Python. 
-------------------------------------------------------------------------------------------

## Python Program to Print Prime Numbers in an Interval
This Python program takes user input for the lower and upper limits of an interval and prints all prime numbers within that range.

### Method:
1. The program prompts the user to input the lower and upper limits of the desired interval.
2. Using a `for` loop, it iterates through the numbers in the specified range.
3. For each number greater than 1, it checks if it is a prime number:
   - It iterates through the numbers from 2 to the number itself.
   - If the number is divisible by any of these values, it breaks out of the loop.
   - If the loop completes without finding a divisor, the number is prime and is printed.
4. The program displays all prime numbers within the specified interval.

### Example Output:
For the given input interval, the program calculates and prints all prime numbers within that range.
This program provides a basic example of finding prime numbers using nested loops and conditional statements in Python.
-------------------------------------------------------------------------------------------

## Python Program to Convert Celsius to Fahrenheit
This Python program converts temperature from Celsius to Fahrenheit using the formula: \( Fahrenheit = (Celsius \times \frac{9}{5}) + 32 \).

### Method:
1. The program prompts the user to input the temperature in Celsius as a floating-point number.
2. Using the conversion formula, the program calculates the equivalent temperature in Fahrenheit.
3. The program then displays the original temperature in Celsius and the corresponding temperature in Fahrenheit.

### Example Output:
For the given input temperature in Celsius, the program calculates and prints the equivalent temperature in Fahrenheit.
This program serves as a basic example of unit conversion in Python, specifically converting Celsius to Fahrenheit.