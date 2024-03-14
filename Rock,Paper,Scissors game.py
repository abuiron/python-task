import random
while True:
    print('\n\t .....Rock,Paper,Scissor game.....')
    choice=input('\nEnter your choice :')

    game_choices=['rock','paper','scissor']

    opposite=random.choice(game_choices)
    print('\n ENEMY :',opposite)

    if(choice=='rock' and opposite=='scissor' or choice=='scissor' and opposite=='paper' or choice=='paper' and opposite=='rock'):
        print('\n Your win :)')
    elif(choice==opposite):
        print('\n Tie')
    else:
        print('\nYou lose :(')

