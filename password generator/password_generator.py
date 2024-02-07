import random
# import string

class PasswordGenerator:
    def __init__(self):
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                          'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                          'U', 'V', 'W', 'X', 'Y', 'Z']
        self.symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '=']
    
    def getPassword(self, length):
        password = ""
        combined = self.numbers + self.lowercase + self.uppercase + self.symbols
        for _ in range(length):
            password += str(random.choice(combined))
        return password
        



if __name__ == "__main__":
    pg = PasswordGenerator()
    length = int(input(">>> Enter desired length of random password : "))
    print(">>> Randomly Generated Password : " + pg.getPassword(length=length))
