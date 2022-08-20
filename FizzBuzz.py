"""
Write a short program that prints each number from 1 to 20 on a
new line.

For each multiple of 3, print "Fizz" instead of the number.

For each multiple of 5, print "Buzz" instead of teh number.

For numbers which are multiples of both 3 and 5, print "FizzBuzz"
instead of the number.

"""
for number in range(1,21):
    #if number % 15 == 0:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

