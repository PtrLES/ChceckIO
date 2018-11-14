def to_encrypt(text, delta):
    import string
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    code=[]
    for letter in text:
        if letter in alphabet:
            number= ord(letter)+delta
            if number<97:
                number+=26
            elif number > 122:
                number-=26
            code.append(chr(number))
        else:
            code.append(letter)
    print code
    return ''.join(code)

if __name__ == '__main__':


    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")