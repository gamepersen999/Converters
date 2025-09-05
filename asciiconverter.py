def ASCIICONVERT(txt):
    return ord(txt)

def asccvrt():
    text = input("Enter Character: ")
    print(f"ASCII Value: {ASCIICONVERT(text)}") if len(text) == 1 else print("Invalid.")

if __name__ == '__main__':
    asccvrt()