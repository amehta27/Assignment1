def fizzbuzz():
    number = input("Enter the number:")
    number = int(number)
    if number % 3 == 0 and number % 5 == 0:
        print ("Fizz Buzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print("invalid input")


fizzbuzz()
