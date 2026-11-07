evensum=0
oddsum=0
for i in range(1,51):

  if i%2==0:
    evensum +=i
else:
    oddsum +=i
    
    print("Even sum is:",evensum)
    print("Odd sum is:",oddsum)
