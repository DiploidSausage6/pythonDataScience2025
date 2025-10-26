# this is a program to encrypt a string via the Ceasar Cipher
beforeMessage = input("enter message you wish to be encrypted:") # take the message that is going to be encrypted
key = input("enter amount of letters to skip in order to encrypt:") # take the key to encrypt
def Encryptor (beforeMessage, key):
  beforeMessage = beforeMessage.lower()
  afterMessage = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz" # make a list of the alphabet to use index numbers later
  if key.isdigit():
    key = int(key) # makes key an integer
  else:
    return "please make your key a number"
  for character in beforeMessage: # make a for loop
    if character in alphabet: # check if the entered character(s) is a letter
      beforeIndex = alphabet.find(character) # determine the index of the letter(s)
      afterIndex = (beforeIndex + key) % len(alphabet) # add the key to the index of the letter(s) and use the modulo operator to make sure the final message starts over in case of later letter(s)
      afterMessage += alphabet[afterIndex] # assign the proper letters to the determined afterIndex
    else:
      afterMessage += character # if the character is not a letter, move on, leaving it unchanged
  return afterMessage
print(Encryptor (beforeMessage, key))
