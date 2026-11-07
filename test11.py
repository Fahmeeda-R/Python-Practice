a=input("Enter a sentence:")
lower=a.lower()
vowels="aeiou"
count=0
for ch in a:
    if ch in vowels:
        count += 1
words=a.split()
reverse=a[::-1]
print("Vowels:",count)
print("Words:",len(words))
print("Reverse:",reverse)