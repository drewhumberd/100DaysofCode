alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    result = "" # sets result to empty string
    if shift > 25:
        large_shift = int(shift / 26)
        shift = shift - large_shift * 26
    for x in text:
        if x in alphabet:
            y = alphabet.index(x) # determines position of letter in alphabet from text input
            if direction == "encode":
                z = y + shift # sets position forward by offset defined by shift
                if z > 25:
                    z = z - 26 # allows looping through alphabet if result would be out of bounds
            elif direction == "decode":
                z = y - shift # sets position backward by offset defined in shift
                if z < 0:
                    z = z + 26 # allows looping through alphabet if result would be out of bounds
            result += alphabet[z] # adds each letter to result string
        else:
            result += x
    print(f"The {direction}d text is {result}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") # user input to determine whether encoding or decoding
    text = input("Type your message:\n").lower() # plain-text message if encoding or encoded message if decoding
    shift = int(input("Type the shift number:\n")) # number by which to shift the characters through the alphabet

    caesar(text, shift, direction)
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break