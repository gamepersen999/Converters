def BC():
    choice = int(input("Do you want:\n[1] Binary Converter\n[2] Binary Intepreter\n >>> "))
    while choice != 1 and choice != 2:
        print("Invalid.")
        choice = int(input("Do you want:\n[1] Binary Converter\n[2] Binary Intepreter\n >>> "))
    if choice == 1:
        dec_no = int(input("Enter number\n >>> "))
        bin_no = bin(dec_no)[2:]
        print("Binary:", bin_no)
    else:
        bin_no = input("Enter binary number\n >>> ")
        dec_no = int(bin_no, 2)
        print("Number:", dec_no)

if __name__ == '__main__':
    BC()