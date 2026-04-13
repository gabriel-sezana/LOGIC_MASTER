"""
example of conditionals in Python

if, elif, else

example:

x = 10
if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")

"""

age = int(input("Enter your age: "))

if age >=18:
    print("You are an adult.")

else:
    print("You are a minor.")


language = input('Type a language: ')

if language == 'Python':
    print('Python is good!')

elif language == 'Java':
    print('Java is hard!')

elif language == 'Cobol':
    print('Cobol is old!')

else:
    print('Unidentified language!')