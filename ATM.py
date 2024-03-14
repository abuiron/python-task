class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} deposited successfully."
        else:
            return "Invalid deposit amount. Please enter a positive number."
        
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount: 
                self.balance -= amount
                return f"{amount} withdrawn successfully."
            else:
                return "Invalid withdrawal amount. Please enter a positive number."
def main():
    atm = ATM()

    while True:
        print("\n\tMenu")
        print("\t1. Check Balance")
        print("\t2. Deposit")
        print("\t3. Withdraw")
        print("\t4. Quit")

        choice = input('\nEnter your choice: ')

        if choice == '1':
            print("Current Balance:", atm.check_balance())

        elif choice == '2':
            amount = float(input('Enter the amount to deposit: '))
            print(atm.deposit(amount))

        elif choice == '3':
            amount = float(input('Enter amount to withdraw: '))
            print(atm.withdraw(amount))
        
        elif choice == '4':
            print('Exiting program...')
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
