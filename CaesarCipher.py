# this is a program to encrypt a string via the Ceasar Cipher
beforeMessage = input("enter message you wish to be encrypted:") # take the message that is going to be encrypted
key = input("enter amount of letters to skip in order to encrypt:") # take the key to encrypt

def Encryptor (beforeMessage, key)
  alphabet = ["abcdefghijklmnopqrstuvwxyz"] # make a list of the alphabet to use index numbers later
  for character in beforeMessage: # make a for loop
    if character in alphabet: # check if the entered character(s) is a letter
      character = letter
      beforeIndex = alphabet.find(letter) # determine the index of the letter(s)
      afterIndex = (beforeIndex + key) % len(alphabet) # add the key to the index of the letter(s) and use the modulo operator to make sure the final message starts over in case of later letter(s)
      afterMessage += alphabet[afterIndex] # assign the proper letters to the determined afterIndex
    else:
      character = non-letter
      afterMessage += non-letter # if the character is not a letter, move on, leaving it unchanged
  return afterMessage
Encryptor (beforeMessage, key):
print ("afterMessage")
