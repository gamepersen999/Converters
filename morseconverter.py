def MC():
    MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
    }
    def convert_to_morse(text):
        convertedText = []
        for c in text.upper():
            if c in MORSE_CODE_DICT:
                convertedText.append(MORSE_CODE_DICT[c])
            else:
                pass
        return ' '.join(convertedText)
    
    def intepret_morse(text):
        MORSE_CODE_DECODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
        intepretedMorse = []
        morseChars = text.split(' ')
        for m in morseChars:
            if m in MORSE_CODE_DECODE_DICT:
                intepretedMorse.append(MORSE_CODE_DECODE_DICT[m])
            else:
                pass

        return ''.join(intepretedMorse)
    choice = int(input("Do you want:\n[1] Morse Code Converter\n[2] Morse Code Intepreter\n >>> "))
    while choice != 1 and choice != 2:
        print("Invalid.")
        choice = int(input("Do you want:\n[1] Morse Code Converter\n[2] Morse Code Intepreter\n >>> "))
    usertext = input("Type the text you want to be converted into morse code.\n >>> ").lower()
    if choice == 1:
        text = convert_to_morse(text=usertext)
    else:
        text = intepret_morse(text=usertext)
    print(f"Converted: {text}")

if __name__ == '__main__':
    MC()