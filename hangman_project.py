class Hangman:

    # wrong=0
    # word="pretty"
    stages=['','_____','|  |','|  O','| /|\\','|  |','| / \\']
    # letters=word
    # board=list('_'*len(word))
    # evalBoard = "".join(board)
    

    def __init__ (self,word):
        self.wrong=0
        self.letters = word
        self.board = list('_'*len(word))
        self.evalBoard= "".join(self.board)
        self.character=''
        self.input=''
        self.run=True


    def startScreen(self):
        print('''\nHello player. Welcome to 

            H   H      A      N     N  G G G G  M         M      A      N     N
            H   H     A A     N N   N  G        M M     M M     A A     N N   N
            H H H    A   A    N  N  N  G   G G  M  M   M  M    A   A    N  N  N
            H   H   A A A A   N   N N  G     G  M   M M   M   A A A A   N   N N
            H   H  A       A  N     N  G G G G  M    M    M  A       A  N     N 

Your life is at stake, so beware :)
Below is the word you have to guess.''')
        print(self.evalBoard)

    def updateBoard(self):
        return "".join(self.board)

    def printErrorMessage(self,msg):
        print(msg)
        print('Board:',self.evalBoard)

    def evalEndCondition(self):
        '''
            check against wrong and win
            if wrong -> run = false; 
        '''
        if( self.wrong > len(self.stages)-1):
            print('\nThe word was {word}.\nDoes not matter tho, cause you already dead.\nGood luck in the afterlife.\n'.format(word=self.letters.upper()))
            self.run = False
        
        if(self.evalBoard==self.letters or self.character == self.letters):
            print('\nThe word was {word}.\nCongratulations on guessing it right my friend, you may now leave alive.\n'.format(word=self.letters.upper()))
            self.run = False

    def getInputCharacter(self):
        '''
            Get Input character asks user to input their 'guess' into terminal,
            Then we check for errors: if errors -> print ErrorMessage
            return gameContext
        '''
        print('\n'+'Guess a letter or type in the full word (if you dare).')
        self.character=input('Your guess: ').lower()

        if len(self.character) == len(self.letters):
            if self.character == self.letters:
                print('\nNot bad.')
                self.evalEndCondition()
                return
            else:
                print('\nClose, but not quite. (The word you guessed has the same length as the answer)')

            
        
        #Checks for character length
        elif len(self.character) != 1:
            self.character = ''
            self.printErrorMessage('\nType only one character if you don\'t truly know the answer gonk.')

        #checks if self.character not in [A-Z]
        elif(not self.character.isalpha()):
            self.character = ''
            self.printErrorMessage('\nType only alphabetic letters gonk.')

    def wrongGuess(self,msg):
        print(msg)
        print('\n{}'.format(self.evalBoard))
        print('\n'.join(Hangman.stages[:self.wrong]))

        


    def evalInputCharacter(self):
        '''
            Take character (argument) and then checks if character is in word.
            If in word -> update temp_board
        '''

        if self.character in self.input and self.character != '':
            print('\nYou have already guessed this letter! Try another one.')
            print('Board: {}'.format(self.evalBoard))
             

        elif self.character in self.letters and (self.character != '') and not self.character == self.letters:
            self.input+=self.character
            for i in range(len(self.letters)):
                if self.character==self.letters[i]:
                    self.board[i]=self.character
                    self.evalBoard = self.updateBoard()
                else:
                    continue
            if self.evalBoard == self.letters:
                self.evalEndCondition()
            else:
                print('\n'+'Good guess friend. Keep it going'+'\n')
                print('Board: {}'.format(self.evalBoard))
            

        elif self.character not in self.letters and not len(self.character) == len(self.letters):
            self.wrong+=1
            self.input+=self.character
            if self.wrong> len(self.stages)-1:
                self.wrongGuess('Your last guess is up my friend.')
                self.evalEndCondition()
            else:
                self.wrongGuess('Bad guess. You\'re one step closer to dying my friend.')

    def hangman(self):
        self.startScreen()
        
        
        while self.run:
            self.getInputCharacter()
            self.evalInputCharacter()
            # evalEnd = evalEndCondition(gameContext)

            # if(evalEnd):
            #     break


hangman_1 = Hangman('conscious')
hangman_1.hangman()