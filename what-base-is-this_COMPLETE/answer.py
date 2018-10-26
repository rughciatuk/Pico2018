#!/usr/bin/env python

import pwn
import re

host, port = '2018shell3.picoctf.com', 64706

s = pwn.remote(host, port)

prompt = s.recv()
binary_num = re.findall(r"([01]{8})", str(prompt))
s.sendline(''.join([chr(int(binary,2)) for binary in binary_num]))

prompt = s.recv()

hex_num = re.findall(r"([0-9a-e]{4,})", str(prompt))
s.sendline(''.join([chr(int(hex_num[0][index:index+2], 16)) for index in range(0, len(hex_num[0]), 2)]))

prompt = s.recv()

oct_num = re.findall(r"[0-8]{1,3}", str(prompt))
s.sendline(''.join([chr(int(number, 8)) for number in oct_num]))

prompt = s.recv()
print(re.search(r"picoCTF\{.*?\}", str(prompt)).group())