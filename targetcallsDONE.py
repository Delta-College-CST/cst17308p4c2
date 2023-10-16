# This program reads a file of first and last names and phone
# numbers and writes the name of all people with a 989 area code.

TARGET_AREA_CODE = "989"

phonefile = open("phonedata.txt", "r") # Open file for reading

# File processing loop
for line in phonefile:

    # Read one line of data and split data tokens out
    firstname, lastname, phone = line.split(",")

    # Determine area code within phone
    areaCode =  phone[0:3]

    # If area code matches target area code, write info
    if areaCode == TARGET_AREA_CODE:
        print(firstname,lastname,phone)


