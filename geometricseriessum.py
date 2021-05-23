r = int(input("Please Enter the integer base r"))
n= int(input("Please Enter the number of terms n"))
Series=[]
for i in range(n):
    Series.append(1+(r^(i)))
print(Series[-1])
