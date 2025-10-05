# Write a function to reverse a string

# Ask the user to enter something
string = input("Enter anything you want! :) : ")

# To reverse it I think I need to break it up into chunks first that I can look at backwards.
# A function to reverse the string:
def reverseIt(name):
    # To reverse it I need to break it into smaller parts first so I'll make it a list
    nameCharactersList = list(name)
    print(nameCharactersList)
    # now I can reverse that list like reading it backwards
    # I found that Python has a built in reversed function to reverse lists for you
    nameCharsReversed = list(reversed(nameCharactersList))
    print(nameCharsReversed)
    # I don't want it as a list so need to combine back into a string
    reversedName = "".join(nameCharsReversed)
    return reversedName # send back the reversed one

reversedString = reverseIt(string) # here I call the function

print("And here it is combined back into a string")
print(reversedString)
