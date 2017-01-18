
#Joe Bender
#This program is a game of hangman
#The user is guessing letters of a secret word. 
#When an incorrect letter is guessed, a limb is added to the hangman
#If the hangman is completed, 

#import random to generate random numbers
import random

#open file of words
f = open('words.txt', 'r')

#take in all lines in an array
lines = f.readlines()
		
#close file
f.close()






#restart variable set to 1 to initiate first round of game
restart = 1;

while restart == 1:
	#random int generator to select random word
	chooser = random.randint(0, 4)
	
	#selects random line of file for word
	secretwordFull = lines[chooser]

	#makes array of letters from secret word
	secretword = list(secretwordFull)
	
	
	guessedletters = []
	del guessedletters[:]

	restart = 0;
	#describes program
	print ("")
	print ("Hello!")
	print ("")
	print ("This a program is an computerized game of Hangman.")
	print ("")
	print ("The user will guess letters of a secret word until the word is completely revealed")
	print ("")
	print ("If the user guesses a letter that is not in the secret word, an extremity will be added to the hangman")
	print ("")
	print ("If the hangman is completed before the secret word is guessed, the man is 'hanged' and the game is over")
	print ("")
	input("Press Enter to begin game...")

	print ("")
	print ("Game Begin")


	
	#checks to see how many blanks are needed for guessed word
	counterguessed = len(secretword)
	#creates guessed word
	guessedword = ['_'] * (counterguessed - 1)
	
	
	

	#strikes varible holds how many inncorrect guesses the user has
	strikes = 0
	#hold a temporary index for the location of a correct guess
	indexspot = 0


	#array of hangman pictures. Depending on how many strikes the user has, a more or less complete hangman will be displayed
	HANGMANPICS = ['''
	  +---+
	  |   |
		  |
		  |
		  |
		  |
	=========''', '''
	  +---+
	  |   |
	  O   |
		  |
		  |
		  |
	=========''', '''
	  +---+
	  |   |
	  O   |
	  |   |
		  |
		  |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|   |
		  |
		  |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
		  |
		  |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 /    |
		  |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 / \  |
		  |
	=========''']

	#a win varibale to be set to either 0 or 1, it will determine the status of the users completeness of the game
	win = 0;

	#while the user hasnt won yet, prompt for a letter
	while win == 0:

		#prompt for guess
		allow = 1
		
		while allow == 1:
		
			
			guess = input("Type a letter to guess, or try to guess the secret word, and then press Enter: ")
			
			
		
			print ("")
			#convert to lowercase
			finalguess = guess.lower();
			
			if finalguess in guessedletters:
				print("You already guessed that letter! Please choose another:")
				allow = 1
			else:
				
				guessedletters.append(finalguess)
				allow = 0
			
			
			
			
		#underscore string variable, will check if guessed word contains this later. It determines if the user has won
		underscore = '_'
		#counter used to iterate through the guessed and secret words
		counter = 0

		#display current guess
		print('Your guess:'+ finalguess)
		
		print ("")

		#iterate through secret word 
		for x in secretword:
			#searching for match to user guess
			if finalguess == x:
				print('Guess Correct!')
				#Store which index was a match
				indexspot = secretword.index(x)
				#change underscore at index of correct guess to the correct letter
				guessedword[indexspot] = finalguess
				#feedback on where guess was found
				print ('This letter was found at index: %s' %indexspot)
				
				
				#accumulator to see if user has won
				counter2 = 0
				#for each element in guessed word...
				for x in guessedword:
					#if an underscore exists, the game is not over and the user is sent back to guess
					if underscore == x:
						print ('Keep Guessing to Win!')
						print('')
						break
						
					else:
						#if the element is not an underscore, add to the accumulator
						counter2+=1
						#once the accumulator is the length of the guessed word, that means there are no more underscores in the guessed word and the user has won.
						if counter2 == len(guessedword):
							print('You have won the game!! The secret word is complete!')
							print ('Progress: %s' %guessedword)
							#change win variable to 1, ends game
							win = 1
							
							#asks if user wants to play again
							playagain = input('Enter Y to play again or N to exit game: ')
							
							#if statement to set restart variable to 1 is you want to play again, this reinitializes the loop and the game is played again
							if playagain == 'Y' or playagain == 'y':
								restart = 1
							else:
								#if Y not selected, restart is set to 0, the loop is allowed to end, and the game ends
								restart = 0
							
				
				
				break
				
			else:
				#if the guess does not match that specific index element, add to accumulator
				counter+=1
				#if the accumulator reaches the length of the secret word, that means that the guess is not in the secret word
				if counter == len(secretword):
					print('No match!')
					#add a strike
					strikes+=1
					#print corresponding hangman
					print('')
					print(HANGMANPICS[strikes])
					print('')
					#if you reach six strikes and the hangman is complete, the game is over
					if strikes == 6:
						print('You have lost the Game! Please try again')
						
						win = 1
						#asks if user wants to play again
							playagain = input('Enter Y to play again or N to exit game: ')
							
							#if statement to set restart variable to 1 is you want to play again, this reinitializes the loop and the game is played again
							if playagain == 'Y' or playagain == 'y':
								restart = 1
							else:
								#if Y not selected, restart is set to 0, the loop is allowed to end, and the game ends
								restart = 0
				
				
				
		
		#print the guessed word/user progress
		print('')
		print ('Progress: %s' %guessedword)
		print('')








