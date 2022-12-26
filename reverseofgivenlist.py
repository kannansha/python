n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split( )))

def reverse_list(l):
  start = 0
  end = len(l) - 1
  while start <= end:
    l[start], l[end] = l[end], l[start]
    start += 1
    end -= 1
  return l

print(reverse_list(l))
