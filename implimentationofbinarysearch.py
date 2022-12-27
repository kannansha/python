arr = [int(x) for x in input("Enter the list of elements, separated by spaces: ").split()]
arr.sort()
x = int(input("Enter the target element: "))
low = 0
high = len(arr) - 1
result = -1
while low <= high:
  mid = (high + low) // 2
  if arr[mid] < x:
    low = mid + 1
  elif arr[mid] > x:
    high = mid - 1
  else:
    result = mid
    break
if result != -1:
  print(f"Element {x} is present at index {result}")
else:
  print("Element is not present in the array")
