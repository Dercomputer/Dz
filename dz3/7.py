from collections import Counter


def pabtext(text):
    p = max(text, key=len)
    o = Counter(text)  # create dict, elements - key and count - value
    c = o.most_common(1)[0][0]
    return p, c

text = input().split()

print(pabtext(text))
