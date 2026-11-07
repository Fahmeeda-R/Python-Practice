a=int(input("Enter mark1:"))
b=int(input("Enter mark2:"))
c=int(input("Enter mark3:"))
d=int(input("Enter mark4:"))
e=int(input("Enter mark5:"))
total=a+b+c+d+e
print("Total:",total)
average=total/5
print("Average:",average)
if average>=90:
    print("Grade A")
elif average>=75:
    print("Grade B")
elif average>=60:
    print("Grade C")
elif average>=40:
    print("Grade D")
else:
    print("Fail")
