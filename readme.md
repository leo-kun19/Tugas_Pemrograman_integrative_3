# Sum Numbers and BMI Calculator

This project consists of two Python scripts: one to read integer numbers from a text file and calculate their sum, and another to implement a BMI calculator using a class.

## Files Included

- `sum_numbers.py`: This script reads integer numbers from a text file named `indata.txt`, calculates their sum, and prints the result with comma separators and two decimal places.

- `bmi.py`: This script contains a class `BMI` which is used to calculate Body Mass Index (BMI) given the weight and height of a person.

- `indata.txt`: This text file contains integer numbers which are used as input for the `sum_numbers.py` script.

## How to Use

1. Ensure you have Python installed on your system.
2. Place all the files (`sum_numbers.py`, `bmi.py`, and `indata.txt`) in the same directory.
3. Run `sum_numbers.py` using Python. This will read the numbers from `indata.txt`, calculate their sum, and print it with comma separators and two decimal places.
4. Use the `BMI` class from `bmi.py` in your own scripts as needed. Instantiate the class with weight and height values, and use the `BMI_Value()` method to calculate BMI.
5. Modify `indata.txt` with your own numbers if you wish to calculate the sum of different integers.

## Example

If `indata.txt` contains the following numbers:
10
1000
20

Running `sum_numbers.py` will output:
1,030.00
