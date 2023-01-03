x=int(input('Enter the x value:'))
y=int(input('Enter the y value:'))
z=int(input('Enter the z value:'))
n=int(input('Enter the n value:'))
l=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
print(l)


