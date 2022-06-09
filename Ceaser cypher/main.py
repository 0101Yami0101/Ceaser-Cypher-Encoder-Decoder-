#Ceaser-Cypher   #Encoder-Decoder
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Encode algorithm
def encrypt(plain_text,shift_amount):
   cypher_text = ""   #Enpty string to add cypher text
   for character in plain_text:
      if character in alphabet: #Ensures the encoding of alphabets only
         old_position = alphabet.index(character)
         new_position = old_position + shift_amount
         shifted_letter = alphabet[new_position]
         cypher_text += shifted_letter
      else:       #Append characters other then alphabets to the encoded text
         cypher_text += character
   print(f"The encoded text is {cypher_text}")
   
#Decode Algorithm
def decrypt(plain_text,shift_amount):
   cypher_text = ""  #Enpty string to add cypher text
   for character in plain_text:
      if character in alphabet: #Ensures the decoding of alphabets only 
         old_position = alphabet.index(character)
         new_position = old_position - shift_amount
         shifted_letter = alphabet[new_position]
         cypher_text += shifted_letter
      else:      #Append characters other then alphabets to the encoded text
         cypher_text += character 
   print(f"The decoded text is {cypher_text}")

#Loop program to re-run until user exits/change flag to false
should_continue = True #Flag to run loop
while should_continue:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))



   shift = shift % 26  #If shift number is greater then 26(number of letters present), it takes modulus 


   #Cypher Direction Check
   if direction == "encode":
      encrypt(plain_text=text,shift_amount=shift)
   elif direction == "decode":
      decrypt(plain_text=text,shift_amount=shift)
   else:
      print(f"Invalid direction entered - {direction}")

   ask_if_continue = input("Type 'yes' if you want to continue, else type 'no' \n") #Condition to change flag to exit while loop if needed
   if ask_if_continue == "no":
      should_continue = False
      print("Goodbye")
   

   #Alternatively the two functions encrypt() and decrypt() can also be molded into a single function but this one is more understandable

