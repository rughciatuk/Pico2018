#!/usr/bin/env python

def fib(number):
    fib = [0,1]
    for i in range(number):
        fib.append(fib[i]+fib[i+1])
    return fib[number]

def main():
    print(fib(1026))

if __name__ == '__main__':
    main()