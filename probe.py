result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
i = 0
with open('text.txt') as f:
    text = f.read()
    text2 = [text for text in text.encode('ascii')]
    print("  ".join(map(str, text2)), file=result)
    for id, val in enumerate(text2):
        print(id + 1, end="   ", file=result)
result.close()
with open('result.txt') as r:
    tekst = r.readlines(1)
    for tekst1 in tekst:
        qwe = tekst1
        qwe = qwe.split()
        for qwe1 in qwe:
            qwe2 = qwe1
            qwe3 = int(qwe2)
            qwe4 = chr(qwe3)
            print(qwe4, end="", file=ResultEncode)
ResultEncode.close()
