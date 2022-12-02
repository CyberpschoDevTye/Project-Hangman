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

def updateBoard(gameContext):
    return "".join(gameContext["board"])

def getInputCharacter(gameContext):
    '''
        Get Input character asks user to input their 'guess' into terminal,
        Then we check for errors: if errors -> print ErrorMessage
        return gameContext
    '''
    print('\n'+'Guess a letter (if you dare).')
    character=input('Your guess: ').lower()

    #Checks for character length
    if len(character) != 1:
        printErrorMessage('\nType only one letter you choom.', gameContext)

    #checks if character not in [A-Z]
    if(not character.isalpha()):
        printErrorMessage('\nType only alphabetic letters you choom.', gameContext)
    
    return (character, gameContext)

def evalInputCharacter(character, gameContext):
    '''
        Take character (argument) and then checks if character is in word.
        If in word -> update temp_board
    '''
    if character in gameContext["letters"]:
        for i in range(len(gameContext["letters"])):
            if character==gameContext["letters"][i]:
                gameContext["board"][i]=character
                gameContext["evalBoard"] = updateBoard(gameContext)
            else:
                continue
        # updated_board=''.join(temp_board)
        gameContext["letters"]=word.replace(character,'$')
        print('\n'+'Good guess g. Keep it going'+'\n')
        print('Board: {}'.format(gameContext["evalBoard"]))
        

    elif character not in gameContext["letters"]:
        gameContext["wrong"]+=1
        print('\nBad guess. You\'re one step closer to dying cous')
        print('\n{}'.format(gameContext["evalBoard"]))
        # print('\n',board,'              ','Wrong guesses:',gameContext["wrong"])
        # print(''.join(stages[:gameContext["wrong"]]))
        print(gameContext["stages"][:gameContext["wrong"]])

    return gameContext

def evalEndCondition(gameContext):
    '''
        check against wrong and win
        if wrong -> run = false; 
    '''
    if( gameContext["wrong"] > len(gameContext["stages"])):
        print('\nThe word was {word}.\nDoes not matter tho, cause you already dead.\nGood luck in the afterlife.'.format(word=gameContext["word"].upper()))
        return True
    
    if(gameContext["evalBoard"] == gameContext["word"]):
        print('\nThe word was {word}.\nCongratulations on guessing it right choom, you may now leave alive.'.format(word=gameContext["word"].upper()))
        return True
    
    return False

def printErrorMessage(msg, gameContext):
    print(msg)
    print('Board:'+ ''.join(gameContext["board"]))

def hangman(word):
    startScreen()
    gameContext = { "word": word, "wrong": wrong, "board": board, "evalBoard": evalBoard, "stages": stages, "letters": letters}
    
    while True:
        character, gameContext = getInputCharacter(gameContext)
        gameContext = evalInputCharacter(character, gameContext)
        evalEnd = evalEndCondition(gameContext)

        if(evalEnd):
            break


hangman(word)