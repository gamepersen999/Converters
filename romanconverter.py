def ITR(num):
    roman_nums = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),  (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = ''
    for val, sym in roman_nums:
        while num >= val:
            result += sym
            num -= val
    
    return result

def RTI(roman):
    romnums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in reversed(roman):
        curval = romnums[c]
        if curval < prev:
            total -= curval
        else:
            total += curval
        prev = curval
    return total

def RC():
    func = input("Which converter would you like?\n[1] Number to Roman\n[2] Roman to Number\n >>> ")
    while func != '1' and func != '2':
        print("Invalid converter.")
        func = input("Which converter would you like?\n[1] Number to Roman\n[2] Roman to Number\n >>> ")
    func = int(func)
    if func == 1:
        try:
            print(ITR(int(input("Enter integer: "))))
        except ValueError:
            print("Not an integer.")
    else:
        print(RTI(input("Enter Roman Numerals: ")))

if __name__ == '__main__':
    RC()