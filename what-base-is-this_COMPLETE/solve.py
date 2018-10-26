
def bianry_to_text(num):
    num = num.strip()
    return ''.join([chr(int(binary,2)) for binary in num.split(" ")])

def hex_to_text(num):
    num = num.strip()
    return ''.join([chr(int(num[index:index+2], 16)) for index in range(0, len(num), 2)])

def oct_to_text(num):
    num = num.strip()
    return ''.join([chr(int(number, 8)) for number in num.split(" ")])

def main():
    print("Hello!")
    binary_num = input("Enter binary num: ")
    print("The word is", bianry_to_text(binary_num))
    hex_num = input("Enter hex num: ")
    print("The word is", hex_to_text(hex_num))
    dec_num = input("Enter dec num: ")
    print("The word is", oct_to_text(dec_num))

if __name__ == "__main__":
    main()