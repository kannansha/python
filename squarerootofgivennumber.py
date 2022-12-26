num=int(input('Enter the value:'))

def print_square_root(num):
  sqrt = num / 2
  
  while True:
    new_sqrt = (sqrt + num / sqrt) / 2
    if abs(new_sqrt - sqrt) < 1e-10:
      break
    sqrt = new_sqrt
  if sqrt>10:
      return 'Hello'
  else:
      return 'Hi'

print(print_square_root(num))
