

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def function (message,radix,command):
    if command == "decode":
        radix *= -1
    new_word = ""
    for index in range (len(message)):
        if message [index] not in letters:
            new_letter = message[index]
        else:
            letter_index = letters.index(message [index])
            new_letter_index = letter_index + radix
            if new_letter_index > 25:
                new_letter_index -= 26
            elif new_letter_index <-26:
                new_letter_index += 26
            new_letter = letters[new_letter_index]
        new_word += new_letter
    
    if command == "decode":
        print (f"\"{new_word}\" is the decoded message.")
    else:
        print (f"\"{new_word}\" is the encrypted message.")

cont = True

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print (logo)

while cont == True:
    encrypt_or_decrypt = input ("Welcome to the Caeser Cipher! Would you like to encrypt or decrypt a code? Type 'encode' to encrypt and 'decode' to decrypt: ").lower()

    if encrypt_or_decrypt == "encode":
        word = input ("Please enter your message: ").lower()
    elif encrypt_or_decrypt == "decode":
        word = input ("Please enter the encrypted message: ").lower()
    else: 
        print ("An error occured. Please check the spelling of your instructions.")
        break
    shift_number = int (input ("Please enter the shift number: "))

    shift_number = shift_number % 26

    function(word,shift_number,encrypt_or_decrypt)

    carry_on = input ("Would you like to continue? Type 'Y' for yes and 'N' for no: ").lower()

    print ("\n")

    if carry_on == "n":
        cont = False
        print ("Thank you for using this encryption software! :)")
