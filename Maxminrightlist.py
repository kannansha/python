n=int(input())
l=list(map(int,input().split()))
k=int(input())
l.sort()
a=l[-k:]
print("max and min diff of calculated last k")
print(max(a)-min(a))
