from art import logo

def caesar(text, shift, direction):
    finalText = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            index = alphabet.index(i)
            newIndex = index + shift
            finalText += alphabet[newIndex]
        else:
            finalText += i
    print(f"Here's the {direction}d result: {finalText}")


# def encrypt(text, shift):
#     encryptedMessage = ""
#     for i in text:
#         index = alphabet.index(i)
#         newIndex = shift + index
#         encryptedMessage += alphabet[newIndex]
#     print(f"The encoded text is {encryptedMessage}")


# def decrypt(text, shift):
#     decryptedMessage = ""
#     for i in text:
#         index = alphabet.index(i)
#         newIndex = index - shift
#         decryptedMessage += alphabet[newIndex]
#     print(f"The decoded text is {decryptedMessage}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# printing logo from art.py file
print(logo)

shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)

    runAgain = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if runAgain == "no":
        shouldContinue = False
        print("Good Bye")
