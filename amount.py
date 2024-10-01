amount=int(input("enter the total amount"))
a=amount//1000
print("number of 1000 rupee notes is",a)
rem=amount%1000
b=rem//500
print("number of 500 rupee notes is",b)
rem1=amount%500
c=rem1//100
print("number of 100 rupee notes is",c)