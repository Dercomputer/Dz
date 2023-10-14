from collections import Counter


def pabtext(text):
    P = max(text, key=len)
    o = (Counter(text))  # create dict, elements - key and count - value
    c = max(o, key=lambda x: o[x])
    print(Counter(text))
    print("Самое длинное: " + P + ", самое частое: " + c)
text = input().split()

pabtext(text)
