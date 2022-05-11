# print('писька')
# print('Егор писька')
# text = open('text.txt')
result = open('result.txt', 'w')
ResultEncode = open('result-encode.txt', 'w')
# text_bytes = text.encode('utf-8')
# result.close()
# text.close()
# ResultEncode.close()
# text = open('text.txt')
with open('text.txt', 'r') as text:
    for chore in text:
        print(chore.encode('utf-8'), file=result)

