#Andrew Hilton 4th pd 1/25/18
def assignment(): #Creates list from string
    x = "My name is Jose"
    y = list(x)
    print(y)
    assignment2()#Moves to next function
def assignment2():#Splits function into string using ; as parameter
    x = "user1;user2;user3"
    y = x.split(";")
    print(y)
    assignment3()#Moves to next function
def assignment3():
    x = ['this','is','a','sentence'] #Splits into a string and prints with spaces
    glue = " "
    y = glue.join(x)
    print(y)
assignment()#Moves to next function
