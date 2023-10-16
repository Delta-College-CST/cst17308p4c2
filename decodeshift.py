# This program decrypts a coded character string.
# Precondition:  Input will exclusively be alpha.

SHIFT_POSITION_COUNT = 3

# Capture code input from user
coded = input("Enter coded string: ")

# Begin decryption
length = len(coded)
message = ""
for i in range(length):
    newChar = coded[i].upper()
    newCharInt = ord(newChar) - SHIFT_POSITION_COUNT
    if newCharInt < ord("A"):
        newCharInt = newCharInt + 26
    message += chr(newCharInt)

# Output encrypted message
print(message)
    

