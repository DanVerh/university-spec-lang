class InputException(Exception):
    pass

def inputText():
    text = ""
    while not text.isalpha():
        try:
            text = input("Enter the text that you want to format (only English letters): ")
            if not text.isalpha():
                raise InputException("EXCEPTION: PROVIDE ONLY ENGLISH LETTERS")
        except InputException as error:
            print(error)
    return text

def inputSize(text):
    size = ""
    while not size.isdigit() or int(size) < len(text):
        try:
            size = input("Enter the desired size: ")
            if not size.isdigit() or int(size) < len(text):
                raise InputException("EXCEPTION: PROVIDE ONLY POSITIVE INTEGER > TEXT LENGTH")
        except InputException as error:
            print(error)
    return size