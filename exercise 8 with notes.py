names=["Jake","Zac","Ian","Ron","Sam","Dave"] #list of names
find=input("Who are you looking for:? ")      #asking the users who is looking for 

if find in names:  #using if for finding if the person he is searching is in the list
    print(f"{find} Congrats you found it!!") #this will print if the user matches who are in the list 
    
else:
    print(f"{find} The person you are looking for is unattended pls try again !!")#this will displayed if the user enter the names that are not belong on the list