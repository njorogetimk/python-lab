from random import randint

'''
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle
'''

def intro():
    print("""
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

    I have thought up a number.

    You have 10 guesses to get it.
    """)

def secret_digits():
    secret = []
    for i in range (3):
        a = randint(0,9)
        secret.append(str(a))
    
    return secret

def get_input_and_split():
    the_guess = input(" ")
    the_guess = the_guess.strip(" ")
    the_guess_digits = []
    for digit in the_guess:
        the_guess_digits.append(digit)
    return the_guess_digits

def compare (secret, guess):
    result = []
    
    for digit in guess:
        # Loop through all digits in the guess
        if digit in secret:
            # Is the digit in the secret
            if secret.index(digit) == guess.index(digit):
                # is the digit in the right positon
                result.append('fermi ')
            else:
                result.append('pico ')
        else:
            result.append('bangels')
    
    return result

def evaluate():
    secret = secret_digits()
    for i in range (10):
        print(f"\nGuess #{i+1}")
        guess = get_input_and_split()
        
        result = compare(secret, guess)

        if result.count('fermi ') == len(result):
            print(f"{result[0]}{result[1]}{result[2]}")

            another_try = input('Want another try?[y/n]  ')
            if another_try == 'y':
                evaluate()
            else:
                print("\n\nBye Bye!!\n")
        
            break

        elif result.count('bangels') == len(result):
            print('Bangels')
        else:
            while 'bangels' in result:
                result.remove('bangels')
            
            
            if len(result) > 1:
                new_result = ''
                for value in result:
                    new_result = new_result + value
                print(f"{new_result}")
            else:
                print(result[0])

        
        if  i == 9:
            another_try = input('Want another try?[y/n]  ')
            if another_try == 'y':
                evaluate()
            else:
                print("\n\nBye Bye!!\n")
  
def main():
    intro()
    
    evaluate()


if __name__ == '__main__':
    main()
