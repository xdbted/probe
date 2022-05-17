result = open('result.txt', 'w')
result_encode = open('result-encode.txt', 'w')
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
        qwe = tekst1.encode('utf-8')
        print(qwe, end=" ", file=result_encode)
result_encode.close()
