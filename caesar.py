import time
def cipher(text, key, mode='e'):
    #e = encrypt, d = decrypt
    result = ""
    for c in text:
        if c.isalpha():
            ascstart = ord('a') if c.islower() else ord('A')
            if mode == 'e':
                shifted = (ord(c) - ascstart + key) % 26
            else:
                shifted = (ord(c) - ascstart - key) % 26
            result += chr(ascstart + shifted)
        else:
            result += c
    return result
def CaC():
    chc = input("Choose one\n[1] Encryption\n[2] Decryption\n >>> ")
    while chc != '1' and chc != '2':
        if not chc.isdigit():
            print("Invalid Input.")
            chc = input("Choose one\n[1] Encryption\n[2] Decryption\n >>> ")
        else:
            print("Not one of the modes.")
            chc = input("Choose one\n[1] Encryption\n[2] Decryption\n >>> ")
    chc = int(chc)
    usrtxt = input("Enter text\n >>> ")
    brute = 2
    if chc == 2:
        brute = input("Would you like to brute force?\n[1] Yes\n[2] No\n >>> ")
        while brute != '1' and brute != '2':
            print("Invalid Input.")
            brute = input("Would you like to brute force?\n[1] Yes\n[2] No\n >>> ")
        brute = int(brute)
    if brute == 2:
        validkey = False
        usrkey = input("Enter key: ")
        while validkey == False:
            while not usrkey.isdigit():
                print("Invalid key. Key must be between 1 and 26.")
                usrkey = input("Enter key: ")
            usrkey = int(usrkey)
            while usrkey < 1 or usrkey > 26:
                print("Key must be between 1 and 26.")
                usrkey = input("Enter key: ")
            validkey = True
        if chc == 1:
            print(f"Original: {usrtxt}")
            print(f"Encrypted: {cipher(usrtxt, usrkey, mode='e')}")
        else:
            print(f"Original: {usrtxt}")
            print(f"Decrypted: {cipher(usrtxt, usrkey, mode='d')}")
    else:
        print(f"Original: {usrtxt}")
        print("Decoding", end='', flush=True)
        for i in range(3):
            time.sleep(0.33)
            print(".", end='', flush=True)
        print()
        for i in range(0, 26):
            print(f"Key of {i + 1}: {cipher(usrtxt, (i + 1), mode='d')}")

if __name__ == '__main__':
    CaC()