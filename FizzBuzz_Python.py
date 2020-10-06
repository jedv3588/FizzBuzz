# FizzBuzz in Python
def FizzBuzz():
    value = ""
    if i % 5 == 0 and i % 3 == 0: value = "FizzBuzz"
    elif i % 5 == 0:value = "Buzz"
    elif i % 3 == 0: value = "Fizz"
    else: value = str(i)
    return value

for i in range(0,101):
    print(str(i) + " " + FizzBuzz())

