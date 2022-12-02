wrong=0
word="pretty"
stages=['','_____','|  |','|  O','| /|\\','|  |','| / \\']
letters=word
board=list('_'*len(word))
evalBoard = "".join(board)

def startScreen():
    print('''\nHello player. Welcome to 

         H   H      A      N     N  G G G G  M         M      A      N     N
         H   H     A A     N N   N  G        M M     M M     A A     N N   N
         H H H    A   A    N  N  N  G   G G  M  M   M  M    A   A    N  N  N
         H   H   A A A A   N   N N  G     G  M   M M   M   A A A A   N   N N
         H   H  A       A  N     N  G G G G  M    M    M  A       A  N     N 

Your life is at stake, so beware :)
Below is the word you have to guess.''')
    print(evalBoard)

def updateBoard():
    return "".join(board)

def getInputCharacter():
    '''
        Get Input character asks user to input their 'guess' into terminal,
        Then we check for errors: if errors -> print ErrorMessage and return None
        If no errors -> call evalInputCharacter and progress with game
    '''
    print('\n'+'Guess a letter (if you dare).')
    character=input('Your guess: ').lower()

    #Checks for character length
    if len(character) != 1:
        printErrorMessage('Type only one letter you choom.', evalBoard)
        return

    #checks if character not in [A-Z]
    if(not character.isalpha()):
        printErrorMessage('Type only alphabetic letters you choom.', evalBoard)
        return
    
    return { "word": word, "wrong": wrong, "board": board, "evalBoard": evalBoard, "stages": stages, "letters": letters}

def evalInputCharacter(character, gameContext):
    '''
        Take character (argument) and then checks if character is in word.
        If in word -> update temp_board
    '''
    if character in gameContext["letters"]:
        for i in range(len(gameContext["letters"])):
            if character==gameContext[letters][i]:
                board[i]=character
                evalBoard = updateBoard()
            else:
                continue
        # updated_board=''.join(temp_board)
        letters=word.replace(character,'$')
        print('\n'+'Good guess g. Keep it going'+'\n')
        print('Board: {}'.format(evalBoard))
        

    elif character not in letters:
        wrong+=1
        print('\nBad guess. You\'re one step closer to dying cous')
        print('\n',board,'              ','Wrong guesses:',wrong)
        print(''.join(stages[:wrong]))

    return evalBoard, wrong

def evalEndCondition(evalBoard, wrong):
    '''
        check against wrong and win
        if wrong -> run = false; 
    '''
    print(wrong)
    if( wrong > len(stages)):
        print('\nThe word was {word}.\nDoes not matter tho, cause you already dead.\nGood luck in the afterlife.'.format(word=word.upper()))
        return True
    
    if(evalBoard == word):
        print('\nThe word was {word}.\nCongratulations on guessing it right choom, you may now leave alive.'.format(word=word.upper()))
        return True
    
    return False

def printErrorMessage(msg, temp_board):
    print(msg)
    print('Board:'+ ''.join(temp_board))

def hangman(word):
    startScreen()
    
    while True:
        gameContext = getInputCharacter()
        gameContext = evalInputCharacter(gameContext)
        evalEnd = evalEndCondition(evalBoard, wrong)

        if(evalEnd):
            break


hangman(word)
