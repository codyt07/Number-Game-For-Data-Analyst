#Number guessing game for Data Analysis Project
import random
from statistics import mode, median

#Scorecard for mean, median, mode
SCORE = []

def welcome():
    print('''\n*** Welcome to Guess The Number! ***
        \r*** The game will create a random number between 1 - 100 ***
        \r*** Try to guess the number in the least amount of tries! ***''')
    
def main_game():
    winning_number = random.randint(1,100)
    if len(SCORE) > 0:
        best_score = min(SCORE)
        print(f'\n** You best score so far is {best_score}!')
    guesses = 1
    while True:
        player_guess = input('\nPlease Enter a number between 1 - 100: ')
        try:
            int_guess = int(player_guess)
            if int_guess > 100 or int_guess < 1:
                print("You did not enter a number between 1 - 100")
            elif int_guess > winning_number:
                    print('The number is lower!')
                    guesses += 1 
            elif int_guess < winning_number:
                    print('The number is higher!')
                    guesses += 1
            else:
                SCORE.append(guesses)
                print(f'''You guessed the correct number {winning_number}!
                \nIt took you {guesses} Tries!''')
                new_game() 
                break       
        except ValueError:
            print('A valid number was not entered!')

def new_game():
    #mean
    total = sum(SCORE)
    divide = len(SCORE)
    mean = total / divide
    #median
    game_median = median(SCORE)
    #mode
    game_mode = mode(SCORE)
    #best score
    best_score = min(SCORE)
    print(f'''\nThe Mean/Average of your scores is {mean}
    \rThe Median of your scores is {game_median}
    \rThe Mode of your scores is {game_mode}
    \rYour best score is {best_score}''')
    
    while True:
        new_game = input('''\nDo you want to play again?
            \rEnter A to play again
            \rEnter B to quit
            \rEnter: ''')
        if new_game.lower() == 'a':
            main_game()
            break
        elif new_game.lower() == 'b':
            print(" *** Thank you for playing! ***")
            exit()
        else:
            print("\n**** Invalid selection! ****")

if __name__ == '__main__':
    welcome()
    main_game()