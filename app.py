print("Please enter the details below")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("Your name is " + name + " and your age is", age, "and you live in " + city)

input("Press Enter to exit the program...")
print("Program exited")

num1 = int(input("Enter first number  : "))
num2 = int(input("Enter second number  : "))

addition = num1 + num2

print("Addition is ", addition)

sentence = input("Enter a sentence : ")

word1 = input("Enter a word to replace : ")
word2 = input("Enter a word to replace with " + word1 + " : ")

print("Your new sentence is : " + sentence.replace(word1, word2))

fruits = ["a", "b", "c", "d"]
vegetables = list(("hi", 2, False, "hello"))
print("The type of list is : ", type(vegetables[0]))

from typing import Any, List

list1: List[Any] = [1, 2, 4, 3, 5]
list2: List[Any] = ["a", "b", "c", "d", "e"]

list1.extend(list2)
print("Combined list is : ", list1)

list1.sort()
print(list1)

numbers = (1, 2, 3)
print(type(numbers))

age = int(input("Enter your age : "))

if age > 18:
    print("You are an adult")
else:
    print("You are a kid")


def sayHello(userName):
    print("Welcome " + userName)


sayHello("Aftab")


def hello():
    return 1 + 1


print(hello())

my_dictionary = {
    "name": "Aftab",
    "age": 21,
    "city": "Solapur",
    "skills": ["MERN", "Tailwind", "My SQL", "Next Js"],
}

print(my_dictionary["name"])

i = 1

while i < 6:
    print(i)
    i += 1

fruits = ["apple", "banana", "chickoo"]

my_dictionary = {
    "name": "Aftab",
    "age": 21,
    "city": "Solapur",
    "skills": ["MERN", "Tailwind", "My SQL", "Next Js"],
}

for values in my_dictionary:
    print(values)

for x in range(100):
    print(x)
else:
    print("Finished")


myList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lists in myList:
    for values in lists:
        print(values)
