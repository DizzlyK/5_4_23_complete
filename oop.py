

class Character():
    def __init__(self, username, eyecolor, companion=None):
        self.username = username
        self.eyecolor = eyecolor
        #outfit will be a dictionary {shirt: , shoes: , pants: }
        self.outfit = {}
        self.companion = companion

    def change_username(self):
        newname = input("Enter you new username: ")
        self.username = newname
        return f'Successfull changed your username to {self.username}'
    
    def change_eyecolor(self):
        neweyes = input("Enter you new eyecolor: ")
        self.eyecolor = neweyes
        return f'Successfull changed your eyecolor to {self.eyecolor}'
    
    def change_outfit(self):

        if self.outfit:
            print("you are currently wearing: ")
            for key, value in self.outfit.items():
                print(key, ':', value)

        print("Let's build a new outfit")

        new_shoes = input("What shoes do you want to wear? ")
        new_shirt = input("What shirt do you want to wear? ")
        new_pants = input("What pants do you want to wear? ")
        
        new_fit = {'shirt': new_shirt, 'shoes': new_shoes, 'pants': new_pants}

        self.outfit = new_fit

        return 'Outfit saved!'
    
    def display(self):
        print(f'-----------{self.username}-----------')
        print(f'Eyecolor: {self.eyecolor}')
        print(f'Companion: {self.companion}')
        print("Outfit: ")
        if self.outfit:
            for key, value in self.outfit.items():
                print(key, ':', value)
        else:
            print('None')
            
    
    def runner(self):
        while True:
            print('Your Current Character:')
            self.display()

            respone = input(' Would you like to make any changes? (username, eyecolor, outfit, continue)').lower()

            if respone == 'continue':
                print('Lookin Good! Enjoy whatever this is for')
                break
            elif respone == 'username':
                self.change_username()
                continue
            elif respone == 'eyecolor':
                self.change_eyecolor()
                continue
            elif respone == 'outfit':
                self.change_outfit()
                continue
            else:
                'Invalid Response Try again'

            


dylan = Character('Hurricane', 'brown', 'Rhia')

dylan.runner()
