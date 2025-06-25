#!/usr/bin/env python3

def happy_new_year():
    # Countdown from 10 to 1 and then print "Happy New Year!"
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    # Return a new list with the squares of each integer
    return [i ** 2 for i in int_list]

def fizzbuzz():
    # Print numbers 1 to 100 with FizzBuzz logic
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
