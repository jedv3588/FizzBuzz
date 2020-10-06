# FizzBuzz in Python with scalability and maintainability
def fizzbuzz(max_num=101):
    for i in range(max_num):
        value = ""
        if i % 3 == 0: value += "Fizz"
        if i % 5 == 0: value += "Buzz"
        yield value if value else i

for number, burp in enumerate(fizzbuzz()):
    print (number, burp)
