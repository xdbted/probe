from sys import getdefaultencoding
result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
with open('text.txt') as f:
    text = f.read()
    print(text.encode('ascii'), file=result)
result.close()
ResultEncode.close()

