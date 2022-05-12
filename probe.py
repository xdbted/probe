result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
i = 0
with open('text.txt') as f:
    text = f.read()
    text2 = [text for text in text.encode('ascii')]
    print("  ".join(map(str, text2)), file=result)
    while i != len(text2):
        q = i + 1
        print(q, end="  ", file=result)
        i += 1
result.close()
with open('result.txt') as r:
    r = r.read()
    for g in enumerate(r):
        print(g, file=ResultEncode)