#!/usr/bin/env python
import codecs

def perfect_root(root, number):
    start = 0
    end = number // 2
    current = number // 4


    while True:
        temp = current ** root
        if temp == number:
            return current
        elif temp < number:
            start = current
        else:
            end = current
        current = (end + start) //2


def main():
    target = 2205316413931134031046440767620541984801091216351222789180573437837873413848819848972069088625959518346568495824756225842751786440791759449675594790690830246158935538568387091288002447511390259320746890980769089692036188995150522856413797
    m = perfect_root(3,target)
    print(codecs.decode(hex(m)[2:],"hex").decode("ascii"))

if __name__ == '__main__':
    main()