
#1 write a program that takes 2 numbers as inout and prints their sum.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a+b
print("The sum of above number is",sum)

#2 write program whether the number is even or odd.
a=int(input("Enter any number :"))
if (a%2 == 0):
    print("The number is even")
else:
    print("The number is odd")


#3 write a program that calculates the factorial of a given number.
n=int(input("Enter the number:"))
factorial=1
if (n<0):
    print("Factorial is not defined !")
elif (n==0):
    print("Factorial is 1")
else:
    for i in range(1,n+1):
        factorial *= i
    print (factorial)


#4 write a program that asks the user for their name and then prints a greeting message .
name=input("Enter the name :")
print("Welcome to the program",name,"!")


#5 write a program that takes a string input from the user and writes it to a text file.
string=input("Enter a string : ")
file=open("student.txt","w")
file.write(string)


#6 Write a program that reads the content of a text file and prints it to the console.
file=open("novel.txt","r")
content=file.read()
print(content)


#7 write a program that takes a string as input and return its length.
string=input("Enter the string :")
strLength=len(string)
print("The length of the input string is",strLength)

#8 Write a python program that concatenates two strings and returns the result. 
str1=input("Input first string :")
str2=input("Input second string :")
concat=str1+str2
print("Resulting string after concatenation is",concat)

#9 Write a python program that checks if a substring is present in a given string. 
def findSubstring(string,substr):
    if substr in string:
        print("Yes, subtring is present in a given string.")
    else:
        print("No,subtring is not present in a given string.")

string=input("Input a string :")
substr=input("Input substring :")

findSubstring(string,substr)

#10 Write a python program that converts a given string to uppercase. 
string=input("Input a string :")
upstr=string.upper()
print("Original String :",string)
print("Uppercase String :",upstr)

#11 Write a python program that generates the first n numbers in the Fibonacci sequence. 
n=int(input("Enter a number :"))
num1 = 0
num2 = 1
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

#12 Write a python program that calculates the sum of the digits of a given number. 
def sumOfDigits(num):
    sum=0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10 
    return sum

num=int(input("Enter a number :"))
res=sumOfDigits(num)
print ("Sum of digits is :",res)

#13. Write a program that asks the user for their birth year and calculates their age. 
from datetime import date 
todaysDate=date.today()

current_year=todaysDate.year

birth_year=int(input("Enter your Birth year:"))
age=current_year - birth_year
print(age)

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. 
def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    return lines

def main():
    print("Enter lines of text. Press Enter on an empty line to finish.")
    user_lines = read_lines()
    for line in user_lines:
        print(line)

if __name__ == "__main__":
    main()

#15. Write a program that reads data from a CSV file and prints it to the console.
import csv
file=open("students.csv","r")
lines=csv.reader(file)
for line in lines:
    print(line)

# 16. Write a program in python that counts the frequency of each character in a string.
string=input("Enter a string:")
freq={}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Frequency of characters in given string :",freq)


#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
string=input("Enter a string:")
title=string.title()
print(title)

#18. Write a python program that checks if two strings are anagrams of each other. 
str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")

str1=str1.lower()
str2=str2.lower()

if len(str1)==len(str2):
    sort1=sorted(str1)
    sort2=sorted(str2)

    if sort1 == sort2:
        print("Given strings are anagrams of each other.")
    else:
        print("Given strings are not anagrams of each other.")
else:
    print("Given strings are not anagrams of each other.")
    


#19. Write a python program that removes all punctuation from a given string. 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
string=input("Enter a string:")
no_punctuation=""

for char in string:
    if char not in punctuations:
        no_punctuation += char

print(no_punctuation)


#20. Write a python program that takes a list of numbers and returns their sum. 
n=int(input("Enter no. of enteries:"))
numList=[]
sum = 0 
for i in range(n):
   num=int(input("Enter numbers :"))
   numList.append(num)
for number in numList :
    sum += number
    
print(sum)

#21. Write a python program that counts the occurrences of a specific element in a list. 
n=int(input("Enter no. of enteries:"))
List=[]
for i in range(n):
   num=input("Enter the value:")
   List.append(num)

val=input("Find occurance of value ? : ")
freq=0
for i in List:
   if i == val :
      freq += 1
print("Frequency of occurance is :",freq)

#22. Write a python program that returns the minimum and maximum values in a list of numbers. 
n=int(input("Enter no. of enteries:"))
List=[]
for i in range(n):
   num=int(input("Enter the value:"))
   List.append(num)
max_value=max(List)
min_value=min(List)

print("Maximum value in input list :",max_value)
print("Minimum value in input list :",min_value)

#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 
t=float(input("Enter temperature in celsius:"))
tempF=(1.8 * t)+32
print("Temperature in Fahrenheit:",tempF)

t=float(input("Enter temperature in Fahrenheit :"))
tempC=0.55*(t-32)
print("Temperature in Celsius:",tempC)

#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result. 
n1=float(input("Enter 1st value :"))
n2=float(input("Enter 2nd value :"))
operator=input("Enter operation (+,-,*,/) :")

if operator=='+':
    print("Addition:", n1+n2)
elif operator == '-' :
    print("Subration:",n1-n2)
elif operator == '*':
    print("Multiplication:",n1*n2)
elif operator == '/':
    print("Division:",n1/n2)
else:
    print("Invalid Operator !!!")


#25. Write a program that copies the contents of one text file to another. 
with open("source.txt","r") as firstfile , open("destination.txt", "a") as secondfile :
    for line in firstfile:
        secondfile.write(line)

#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
def check_start(string, prefix):
    return string.startswith(prefix)

def check_end(string, suffix):
    return string.endswith(suffix)

string=input("Enter a string :")
prefix=input("Enter the prefix to be checked :")
suffix=input("Enter the suffix to be checked :")
print(check_start(string, prefix))
print(check_end(string, suffix))

#27. Write a program in python that converts a string into a list of its characters.
string=input("Enter a string :")
lst=list(string)
print("Given string into a list of its character :",lst)