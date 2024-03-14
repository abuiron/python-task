import random
while True:
    print('\n\t .....Rock,Paper,Scissor game.....')
    choice=input('\nEnter your choice :')

    game_choices=['stone','paper','scissor']

    opposite=random.choice(game_choices)
    print('\n ENEMY :',opposite)

    if(choice=='stone' and opposite=='scissor' or choice=='scissor' and opposite=='paper' or choice=='paper' and opposite=='stone'):
        print('\n Your win :)')
    elif(choice==opposite):
        print('\n Tie')
    else:
        print('\nYou lose :(')

