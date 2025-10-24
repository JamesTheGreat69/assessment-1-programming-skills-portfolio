def even(num):                          #this function will check if the number is even.
    return num %2 ==0                 # then I utilize modulo to check the remainder when the (num) is divided by 2.

def main():                           #using this the program will ask the user to input a number.
    user=int(input("Enter your number: ")) #this will ask the user to input a number.
    num=int(user)          
    if even(num) :                       # this will check the number that the user input if its correct then.
        print(num, "is even number.")    # if the user put a even number this will displayed.
        
    else:                 # and if false this will be the outcome.
        print(num, "is odd number. ") # if the user input an odd number this will be displayed.
        
if __name__ == "__main__":        #this will make sure that the main() function will runs when the file is executed directly.
    main() 