#!/usr/bin/env python


answer = 0x28
cond = 0x7

while cond <= 0xa1de:
    answer += 0x1
    cond += 0x76

print(hex(answer))
