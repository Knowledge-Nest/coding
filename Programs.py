# Program for factorial of a number
def factorial(number):
    fact = 1
    while number>1:
        fact = fact * number
        number = number - 1
    print(fact)

factorial(int(input("Enter a number for which factorial needs to be calculated : ")))
