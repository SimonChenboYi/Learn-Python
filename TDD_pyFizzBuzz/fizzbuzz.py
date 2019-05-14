#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
def fizzbuzz(number):
    if number%5 == 0 and number%3 ==0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else: return number


for i in range(1,100):
    print(fizzbuzz(i))
