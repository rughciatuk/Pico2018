import pwn
import re

a = ')\x06\x16O+50\x1eQ\x1b[\x14K\x08]+P\x14]\x00\x19\x17YR]'
b = 'You have now entered the Duck Web,'
# answer = []
# for i in range(len(a)):
#     answer.append(chr(ord(a[i]) ^ ord(b[i])))
# print(''.join(answer))

print(re.findall(r'picoCTF{.*?}',pwn.xor(a,b).decode('utf-8'))[0])
