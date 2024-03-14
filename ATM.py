class ATM:
    def __init__ (self,balance):
        self.balance=balance

    def check_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount >0:
            self.balance=self.balance+amount
            return f"{amount} deposited successfully."
        else:
            return "Invalid deposit amount. Please enter a positive numbver."
        
    def withdraw(self,amount):
        if amount >0:
            if self.balance >=amount : 
                self.balance=self.balance-amount
                return f"{amount} withdrawn successfully."
            else:
                return "Invalid withdrawl amount. Please enter a positive number"
            
def main():
    atm=ATM()

    while True:
        print("\n \t Menu")
        print("\n \t 1. Check Balance")
        print("\n \t 2. Deposit")
        print("\n \t 3. Withdraw")
        print("\n \t 4. Quit")

        choice=input('\n\t Enter your choice :')

        if choice==1:
            print("Current Balance :",atm.check_balance())

        elif choice ==2:
            amount=float(input('Enter the amount to deposit :'))
            print(atm.deposit(amount))

        elif choice ==3:
            amount=float(input('Enter amount to withdrawl :'))
            print(atm.withdraw(amount))
        
        elif choice==4:
            print('Exiting program..')
            break

        else:
            print("Invalid choice . Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()