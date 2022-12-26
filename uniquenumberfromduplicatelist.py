n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split( )))

def find_unique(l):
  count = {}
  for number in l:
    if number in count:
      count[number] += 1
    else:
      count[number] = 1
  for number, occur in count.items():
    if occur == 1:
      return number
  return None

print(find_unique(l))


