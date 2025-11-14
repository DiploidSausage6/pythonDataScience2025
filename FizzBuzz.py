# this is a program to print 1-100,but multiples of 3 are replaced by fizz, multiples of 5 are replaced by buzz, and multiples of both will be fizz buzz.

for number in range(1, 101):
  if number % 15 == 0:
    print("Fizz Buzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
