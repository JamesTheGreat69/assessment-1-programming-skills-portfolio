def hello():     #this is a function that defines hello
    print("hello")  #this will be printed when it is being called

def main(): #this defines another function that named main
   hello() #this is the first function that is being called 

if __name__=="__main__": #this will check if the script run directly or imported as a module
    main() #this will run only if the file is executed directly (not imported)
    
    
    


