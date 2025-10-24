name=input("What is yout name:? ")      # asking the user to inputhis or her name
hometown=input("What is your hometown:? ") # asking the user to input his or her hometown

while True:                     # checking the coindition if true
    age=input("How old are you:? ")  #asking the user to input her or his age
    
    if age.isdigit():   #this is if its true
        age=int(age)      #this will convert the string age into integer
        break     # this will stop the loop
    else:    # this is if its false
        print("Invalid pls try again!! ") # this will be displayed if you enter a wrong 
        continue  # this will continue the loop until the condition is being met
    
    #this section will be the biograpgy where you can store the users input in a dictionary 
a={"Name": name,
   "Hometown": hometown,
    "Age": age   }

print("your name is: ", name, "\nYour Hometown is in: ", hometown, "\nYou are",age,"years old") 
#this will print or shown after all the inputs and \n this will separate
    
        
