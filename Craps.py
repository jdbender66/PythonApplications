
#Joe Bender
#This program is a hypothetical game of craps. It is a game played with two dice.

from random import *

#Asks user for name
name = input('What is your name?\n');

#displays name and describes program
print ("");
print ("Hi %s" % name);
print ("");
print ("This a program is an computerized game of craps.");
print ("In this game a shooter rolls two die, this is known as the 'come out' roll.");
print ("If the shooter rolls a 7 or 11, the player wins.");
print ("If the shooter rolls a 2,3, or 12, the player looses.");
print ("If the shooter rolls any other number,");
print ("the 'come out' roll becomes the 'point number'.");
print ("");
print ("The shooter then continues to roll the dice until one of two things happens:");
print ("- The shooter rolls a 7 and loses");
print ("- Or the shooter rolls the 'point number' again, and wins!");
print ("");

#function to roll a single die with a random number generator
def rollDice():
    return randrange(1,7)

#define a game variable to decide if the game is over or if more rolls are needed
game = 0;

#prompt user if they want to play themselves or have a computer play
type = input('Type "user" if you would like to play, or "computer" if you would like to simulate rounds of craps: ');

#computer generation
if type == 'computer':
	#asks user how many rounds they want computer to play
	roundNum = int(input('How many rounds of the game would you like the computer to play?: '));
	
	#counts how many rounds have been played
	counter = 0;
	
	#counts how many games were won
	score = 0;
	
	#while loop that keeps going until the counter equals the number of rounds the user wanted the computer to play
	while counter < roundNum:
	
		print ("");

		
		#the random numbers assigned to two dice
		die1 = rollDice()
		die2 = rollDice()
					
					
		#calc total of comeout roll
		comeout = die1 + die2;
		print("The total of the come out roll is %s" % comeout);
		print ("");

		#determines if computer has won or lost on the comeout roll, if not then subsequent rolls are needed
		if comeout == 7 or comeout == 11:
			print ("You rolled a %s! CONGRATULATIONS! You have won the game!" % comeout)
			print ("");
			counter += 1;
			score += 1;
			print ("");
			game = 0;
		elif comeout == 2 or comeout == 3 or comeout == 12:
			print ("You rolled a %s! I'M SO SORRY! You have lost the game!" % comeout)
			print ("");
			counter += 1;
			print ("");
			game = 0;
		else:
			print ("You rolled a %s! You have not won or lost yet. You have to roll again!" % comeout)
			game = 1;
			print ("The point number is now %s" % comeout)
			print ("");
				
		#while loop for subsequent rolls
		while game == 1:
					
				
			print ("");

			die3 = rollDice()
			die4 = rollDice()

			subRoll = die3 + die4;

			#determines if computer has won or lost on subsequent rolls, if not then more rolls are needed
			if subRoll == comeout:
				print ("You rolled a %s! CONGRATULATIONS! You have won the game!" % subRoll)
				print ("");
				counter += 1;
				score += 1;
				print ("");
				game = 0;
			elif subRoll == 7:
				print ("You rolled a %s! I'M SO SORRY! You have lost the game!" % subRoll)
				print ("");
				counter += 1;
				print ("");
				game = 0;
			else:
				print ("You rolled a %s, which is not a 7 or the Point Number. You have to roll again!" % subRoll)
				print ("");
				
		#tells user how many games out of x the computer has won
		print("The computer won ");
		print(score);
		print("games out of ");
		print(counter);
	
#user plays the game
else:
	#all of this is pretty much the same as the computer part, except with prompts for user input throughout
	while game == 0:

		while game == 0:
			input("*Press Enter to roll the dice (Come-Out Roll)*");
			print ("");


				
			die1 = rollDice()
			die2 = rollDice()
				
				

			comeout = die1 + die2;
			print("The total of the come out roll is %s" % comeout);
			print ("");


			if comeout == 7 or comeout == 11:
				print ("You rolled a %s! CONGRATULATIONS! You have won the game!" % comeout)
				print ("");
				input("*Press Enter to play again!*");
				print ("");
				game = 0;
			elif comeout == 2 or comeout == 3 or comeout == 12:
				print ("You rolled a %s! I'M SO SORRY! You have lost the game!" % comeout)
				print ("");
				input("*Press Enter to play again!*");
				print ("");
				game = 0;
			else:
				print ("You rolled a %s! You have not won or lost yet. You have to roll again!" % comeout)
				game = 1;
				print ("The point number is now %s" % comeout)
				print ("");
			
			
		while game == 1:
				
			input("*Press Enter to roll the dice again!*");
			print ("");

			die3 = rollDice()
			die4 = rollDice()

			subRoll = die3 + die4;


			if subRoll == comeout:
				print ("You rolled a %s! CONGRATULATIONS! You have won the game!" % subRoll)
				print ("");
				input("*Press Enter to play again!*");
				print ("");
				game = 0;
			elif subRoll == 7:
				print ("You rolled a %s! I'M SO SORRY!You have lost the game!" % subRoll)
				print ("");
				input("*Press Enter to play again!*");
				print ("");
				game = 0;
			else:
				print ("You rolled a %s, which is not a 7 or the Point Number. You have to roll again!" % subRoll)
				print ("");


			





