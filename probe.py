result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
i = 0
with open('text.txt') as text:
    text = text.read()
    text2 = [text for text in text.encode('ascii')]
    # print("  ".join(map(str, text2)), file=result)
    print(text2, file=result)
    while i != len(text2):
        q = i + 1
        print(q, end=" ", file=result)
        i += 1
result.close()
with open('result.txt', 'r') as r:
    for g in r.readlines(1):

        print(g, file=ResultEncode)