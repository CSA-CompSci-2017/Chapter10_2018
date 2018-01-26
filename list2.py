#Andrew Hilton 1/17/18
personal = ["Andrew", "Fith", "February", "2001", "Phoenix AZ"]
y = -1
for x in personal: #Prints list
    y = y+1
    print(personal[y])
y = -1
print("I was born in", personal[4])
print("The month was", personal[2])
personal[1:1] = ["Aaron"]
for x in personal: #Prints new list
    y = y+1
    print(personal[y])
