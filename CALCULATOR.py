def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def exit(a,b):
    return 'exit'
    
print('\t .....CALCULATOR..... \n')
while True:
    a=int(input('\nEnter first value :'))
    b=int(input('\nEnter second value :'))
    
    print('\n\t 1. ADDITION (+) \n\t 2. SUBTRACTION (-) \n\t 3. MULTIPLE (X) \n\t 4. DIVISION (/) \n\t 5.EXIT')
    
    def switch(argument, a,b):
        choices={
            1: add,
            2: sub,
            3: mul,
            4: div,
            5: exit
        }
        return choices.get(argument,a,b)
    while True:
        choice=int(input('Enter your choice :'))
        final=switch(choice, a,b)
        if choice==5:
            print('\nEXITED..')
            break            
        else:
            print('\n Result :',final)
    