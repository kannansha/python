n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split( )))

def arrange_elements(l):
  for i in range(len(l)):
    min_index = i
    for j in range(i+1, len(l)):
      if l[j] < l[min_index]:
        min_index = j
    l[i], l[min_index] = l[min_index], l[i]
  return l

print(arrange_elements(l))


