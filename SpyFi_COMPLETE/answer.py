#!/usr/bin/env ipython

import pwn
import codecs
import string

alphanumaric = "_" + string.ascii_lowercase + string.digits + "}{!@#$%^&*()-+=|<>,.?[]" + string.ascii_uppercase

host, port = '2018shell3.picoctf.com', 30399

def format_16(string):
    return [string[i:i+16] for i in range(0,len(string),16)]


def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message


def get_message_and_code(message, code):
    # assert len(message) == len(code)
    return zip(message, map(lambda row: codecs.encode(row, "hex").decode("utf-8"), code))


def get_char(base=""):

    data_base =  'a' * (11)
    data_base += "fying code is: "
    data_base += "picoCTF{@g3nt6_1"
    data_base += "$_th3_c00l3$t_12"[len(base):]

    data_base += base
    for letter in alphanumaric:
        data = data_base
        print(letter)
        data += letter
        data += "a" * (32 - len(base))
        message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: picoCTF{{@g3nt6_1$_th3_c00l3$t_12asdfasdfasdf}}.
Down with the Soviets,
006
""".format(data).replace('\n', "~")

        message = pad(message)
        text = format_16(message)

        s = pwn.remote(host, port)

        prompt = s.recv().decode("utf-8")
        prompt = s.recv().decode("utf-8")

        s.sendline(data)
        code = s.recv().strip()
        print("data:", data)
        temp = format_16(codecs.decode(code, "hex"))
        # print(list(zip(text, map(lambda x: codecs.encode(x,"hex"),temp))))

        if temp[6] == temp[12]:
            return letter
        s.close()

def main():
    answer = ""
    while not answer or answer[-1] != "}":
        answer += get_char(answer)
        print("current", answer)

if __name__ == "__main__":
    pwn.context.log_level = 'error'
    main()