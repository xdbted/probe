result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
with open('text.txt') as f:
    text = f.read()
    text2 = [text for text in text.encode('ascii')]
    print("  ".join(map(str, text2)), file=result)
result.close()
ResultEncode.close()