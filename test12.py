marks=[80,75,95,58,99]
marks.append(100)
marks.remove(75)
marks.sort()
print("Marks:",marks)
print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Average:",sum(marks)/len(marks))