result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
i = 0
with open('text.txt') as text:
    text1 = text.read()
    for text2 in text1.encode('ascii'):
        text3 = str(text2)
        print("  ".join(map(str, text3)), file=result)
    # print(text2, file=result)
    while i != len(text3):
        q = i + 1
        print(q, end="   ", file=result)
        i += 1
result.close()
with open('result.txt', 'r') as r:
    for g in r.readlines(1):

        print(g, file=ResultEncode)