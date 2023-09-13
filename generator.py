import random
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
        while True:
            if inputData.isdigit():
                inputData = int(inputData)
            else:
                print("Invalid characters, try again....")
                
            return inputData
        
    def password(self):
        i=0
        for self.noofPassword in range(self.noOfPasswords):
            passwords = ''
            for self.noOfCharacter in range(self.noOfCharacters):
                passwords += random.choice(self.passwordCharacters)
            print("\nHere is your password:","(",i+1,")",passwords)
            i+=1

    def run(self):
        self.requestInput()
        self.password()
    
    
        
    


passwordGenerator = Generators()
passwordGenerator.run()