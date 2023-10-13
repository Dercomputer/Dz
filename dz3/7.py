from collections import Counter

text = input().split()
def pabtext(text):
    P = max(text, key=len)
    c = max(Counter(text))  # create dict, elements - key and count - value
    print("Самое длинное: " + P + ", самое частое: " + c)


pabtext(text)

