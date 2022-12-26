def find_max_min_primes(l):
  min_prime = None
  max_prime = None
  for num in l:
    is_prime = True
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      if min_prime is None or num < min_prime:
        min_prime = num
      if max_prime is None or num > max_prime:
        max_prime = num
  print(f"Minimum prime: {min_prime}")
  print(f"Maximum prime: {max_prime}")

n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split( )))
print(find_max_min_primes(l))

