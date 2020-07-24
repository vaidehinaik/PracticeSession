# Solution 1

# def fizzBuzz(num):
#     arr = list()
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     return num
# for n in range(1,20):
#     print(fizzBuzz(n))


# if __name__  == "__main__":
#     for n in range(1,20):
#         print(fizzBuzz(n))


# Solution 2
from pprint import pformat
def fizzBuzz(n):
    res = list()
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res
print(fizzBuzz(100))

