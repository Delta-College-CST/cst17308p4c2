# This program demonstrates various string operations

chant = "Let\'s Go Red Wings"

# Write length of string
print(len(chant))    

# Convert to upper case
chant = chant.upper()

# Extract 'RED'
color = chant[9:12]
print(color)

# Add an exclamation to the original string
chant += "!"

# Print final string
print(chant)
