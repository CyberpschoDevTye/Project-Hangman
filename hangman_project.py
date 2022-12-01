print('''\nHello player. Welcome to 

         H   H      A      N     N  G G G G  M         M      A      N     N
         H   H     A A     N N   N  G        M M     M M     A A     N N   N
         H H H    A   A    N  N  N  G   G G  M  M   M  M    A   A    N  N  N
         H   H   A A A A   N   N N  G     G  M   M M   M   A A A A   N   N N
         H   H  A       A  N     N  G G G G  M    M    M  A       A  N     N 

         Your life is at stake, so beware :)
         Below is the word you have to guess.''')

def printErrorMessage(msg, temp_board):
    print(msg)
    print('Board:'+ ''.join(temp_board))

def hangman(word):
    wrong=0
    stages=['','_____','|  |','|  O','| /|\\','|  |','| / \\']
    letters=word
    # letters=list(word)
    board='_'*len(word)
    temp_board=list('_'*len(word))
    print (board)
    win=0
    while wrong < len(stages) and '_' in temp_board:
        print('\n'+'Guess a letter (if you dare).')
        character=input('Your guess: ').lower()

        #Checks for character length
        if len(character) != 1:
            printErrorMessage('Type only one letter you choom.', temp_board)
            continue

        #checks if character not in [A-Z]
        if(not character.isalpha()):
            printErrorMessage('Type only alphabetic letters you choom.', temp_board)
            continue

        if character in letters:
            for i in range(len(letters)):
                if character==letters[i]:
                    temp_board[i]=character
                else:
                    continue
            # updated_board=''.join(temp_board)
            letters=word.replace(character,'$')
            print('\n'+'Good guess g. Keep it going'+'\n')
            print('Board:'+ ''.join(temp_board))
            win+=1

        elif character not in letters:
            wrong+=1
            print('\nBad guess. You\'re one step closer to dying cous')
            print(board)
            print('\n'.join(stages[:wrong]))

    if win > 0:
        print('\nThe word was {word}.\nCongratulations on guessing it right choom, you may now leave alive.'.format(word=word.upper()))

    else:
        print('\nThe word was {word}.\nDoes not matter tho, cause you already dead.\nGood luck in the afterlife.'.format(word=word.upper()))

        
        

            

    




print(hangman('pretty'))
#     for stage in stages:
#         print(stage)

# print(hangman())





   
