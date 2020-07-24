import math
def primeFactorization(number):
  prime_factor = []
  while number % 2 == 0:
    number = number // 2
    prime_factor.append(2)
  end = int(math.ceil(math.sqrt(number)))
  print(end)
  for i in range(3,end+1, 2):
    while number % i == 0:
      number = number // i
      prime_factor.append(i)
  if number > 1:
    prime_factor.append(number)
  # print(prime_factor)
  return prime_factor
print(primeFactorization(91))
