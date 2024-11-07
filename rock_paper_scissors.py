#Description: This program allows the user to play rock, paper, scissors with the computer(random choices).
if __name__ == '__main__':

    import sys
    from random import choice, seed
    if len(sys.argv) >= 2:
        seed(sys.argv[1])

    the_choice = choice(['rock', 'paper', 'scissors'])
    option = ['rock', 'paper', 'scissors']
    

    user_choice= input('Enter rock, paper, scissors or stop to quit:').lower().strip()
    while user_choice != 'stop':
        
        if user_choice not in option:
            print('Invalid choice, enter rock, paper or scissors.')
        else:
            if user_choice == the_choice:
                print('It is a tie.')
            elif (user_choice == 'rock' and the_choice == 'scissors') or \
                (user_choice == 'scissors' and the_choice == 'paper') or \
                (user_choice == 'paper' and the_choice == 'rock'):
                print('You win!')
            else:
                print('You lose!')
        user_choice = input('Enter rock, paper, scissors or stop to quit:').lower().strip()
            


