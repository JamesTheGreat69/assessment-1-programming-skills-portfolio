password="12345"          #first variable that store the correct password
i=5                       #i represent the maximum attempt
while i>0:                #if the i becomes 0 the loop stops
    attempt=input("\nEnter your password: ") #asking the user to input his password
    if attempt == password:    #if the password matches the value 
        print("Welcome to Mobile Legends!!") # this will be shown on the screen
        break;  #it means that the loop will stops immidiately after you enter the correct password
    else:   
        i-=1 #it will decreased the maximum attempt by 1 if you enter wrong password
        print("Your Password is Incorrect." "you have remaining",i) #and this will be shown your screen if you enter the password incorrectly and the i represent how many attempts left
