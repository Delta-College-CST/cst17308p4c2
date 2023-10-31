# This program formats phone numbers and social security numbers

phone = "(989)-686-9140"
ssn   = "123456789"

# Remove special characters from phone
newphone = phone[1:4] + phone[6:9] + phone[10:]

# Add dashses to social security number
newSSN = ssn[0:3] + "-" + ssn[3:5] + "-" + ssn[6:]

# Display resulting info
print("Phone:",phone,"==>",newphone)
print("SSN:  ",ssn,"==>",newSSN)
