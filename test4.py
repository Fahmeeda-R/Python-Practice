a=float(input("Enter num1:"))
b=float(input("Enter num2:"))
op=input("Enter an operator:")
if op == "+":
 print(a+b)
elif op == "-":
 print(a-b)
elif op == "*":
 print(a*b)
elif op == "/":
 if b!=0:
  print(a/b)
 else:
  print("Cannot divide by zero")

else:
 print("Invalid operator")
