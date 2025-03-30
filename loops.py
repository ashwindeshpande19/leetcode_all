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
        
        
"Q1: Write a Python program that takes a number as input and prints all numbers from that number down to 1 using a while loop."

number = 5
def count_to_one(number):
    while number >= 1:
        print(number)
        number = number - 1
        
count_to_one(number)

"Q2: Write a Python program that takes a string as input and prints each character of the string on a new line using a while loop."

strings = "abcdefg"
def each_char_of_strings(strings):
    s = 0
    while s < len(strings):
        print(strings[s])
        s = s + 1
        
each_char_of_strings(strings)




