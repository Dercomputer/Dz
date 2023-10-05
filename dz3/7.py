text = input()
text = text.split()
P = max(text, key=len)
c = 0
for i in text:
    a = text.count(i)
    if a > c:
        c = a
        b = i
    

print("Самое длинное: " + P + ", самое частое: " + b)
