import random
import sys

class Generators:
    
    
    def __init__(self):
        
        self.passwordCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:'<>,./?\|~`"
        
        print("\n********* Welcome to Password Generator *********\n")
        
    
    def requestInput(self):
        
            
        self.noOfPasswords = input("No of passwords need: ")
    
        self.noOfPasswords = self.validate(self.noOfPasswords)
            
        self.noOfCharacters = input("No of characters need: ")
        
        self.noOfCharacters = self.validate(self.noOfCharacters)
   
    def validate(self,inputData):
        
        if inputData.isdigit():
            inputData = int(inputData)
        else:
            print("Invalid characters, try again....\n")
            sys.exit()
            
        return inputData
        
    def password(self):
        i=0
        try:
            for self.noofPassword in range(self.noOfPasswords):
                passwords = ''
                for self.noOfCharacter in range(self.noOfCharacters):
                    passwords += random.choice(self.passwordCharacters)
                print("\nHere is your","(",i+1,")", "password:",passwords)
                i+=1
        except Exception as e:
            print("Try again, error occured:",e)
        

    def run(self):
        
        self.requestInput()
        self.password()
    

