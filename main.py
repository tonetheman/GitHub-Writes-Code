#!/usr/bin/env python3
#Might as well get this started again
class PurpleBananaMonkey:  
    def __init__(self, monkey_type = "Chimpanzee", color = "Purple"):
        self.monkey_type = monkey_type
        self.color = color
     
    def christmas_is_coming():
        pass
    
    def isMonkey(monkey_type):
        if (monkey_type):
            return True


def main():
    print('\n'.join(' ' * (10-x) + '*' * (x * 2 + 1) for x in range(10)) + '\n' + '\n'.join(' ' * 8 + '|' * 5 for x in range(4)))
    print("Let's get started!")   

    choice = int(input("Please choose from the following\n1. GitHub\n2. Facebook\n3. Twitter\n")) # Add more choices here
    
    if choice == 1:
        print("https://github.com")
    elif choice == 2:
        print("https://facebook.com")
    elif choice == 3:
        print("https://twitter.com/")

    monkey = PurpleBananaMonkey()
    if monkey.isMonkey():
        print("i am a monkey")

if __name__ == "__main__":
    main()
