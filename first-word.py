def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    import string

    # it's deleting first not letter strings
    start = 0
    for element in text:
        if element in (" ", ",", ".", "'"):
            start += 1
        elif element in (string.ascii_uppercase + string.ascii_lowercase):
            break
    text = text[start:len(text)]

    # it's finding the first word
    counter = 1
    for letter in text:
        if letter in (" ", ",", "."):
            break
        else:
            counter += 1
    return text[0:counter - 1]


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")