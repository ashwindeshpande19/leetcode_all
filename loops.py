"Q1: Write a Python program that takes a list of numbers as input and prints the square of each number using a for loop."

numbers = [1,2,3,4,5]
def square_of_num(numbers):
    squared_list = []
    for n in numbers:
        m = n * n
        squared_list.append(m)
        
    print(squared_list)

square_of_num(numbers)

"Q2: Write a Python program that takes a string as input and prints each character of the string on a new line using a for loop."

string = "abcdefg"
def char_in_str(string):
    for c in string:
        print(c)
        
char_in_str(string)
        
        
