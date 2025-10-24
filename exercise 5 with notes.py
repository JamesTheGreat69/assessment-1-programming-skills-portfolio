month = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sept':30,'Oct':31,'Nov':30,'Dec':31, }
name = input("Choose a month: ")
for i in month:
    if i == name:
        print("The number of days in", name,"are", month.get(name))

#the first line will be the dictionary of the month and each month has each value for the number days of that month
#second line asking the user to input the month name 
#third line is using loop to search in the dictionary that I created
#fourth line checking the current key that can matches the users input and if it matches the program will print the number of the days
