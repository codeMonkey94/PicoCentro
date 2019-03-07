
#THIS IS THE PICA CENTRO PROJECT:
	#CREATED BY: HILL, DARNELL
	#DATE: FEBURARY 20, 2014
	#BUILDABLE STATE:
	#LAST MODIFIED FUNCTION:
	#COMMENTS:
#********************************************************************************************************************************************************************************************************************************************
import os 
import random
def main():
	continueGame = greeting()
	if continueGame == 0:
		return
	#os.system('cls')
	mode = userMode()
	if mode == 1:
		skillLevel = difficulty()        
		if skillLevel == 2:
			secretNumberSize = input("ENTER THE SIZE OF THE SECRET NUMBER (THE MAXIMUM  SIZE IS 5):")
			secretNumber = RNG(secretNumberSize)
			theGuess = input("\nENTER A GUESS: ")
			gameOver = specialCompareNumbers(secretNumber,secretNumberSize,theGuess)
			attempts = 0
			#print("%d") % (secretNumber)
			while gameOver == False:
				attempts += 1
				theGuess = input("\n ENTER A GUESS: ")
				gameOver = specialCompareNumbers(secretNumber,secretNumberSize,theGuess)
			if attempts == 0:
				print("\nYOU'VE BEAT THE ODDS...\nYOU GUESSED THE SECRET NUMBER ON THE FIRST TRY.")

		else:
			#SINGLE PLAYER MODE: EASY            
			secretNumberSize = 0            
			os.system('cls')	
			print("\nSINGLE PLAYER MODE: ON\n")
			instructions()
			secretNumber = RNG(secretNumberSize)
			theGuess = input("\nENTER A GUESS: ")
			gameOver = compareNumbers(secretNumber,theGuess)
			attempts = 0
			while gameOver == False:
				attempts += 1
				theGuess = input("\n ENTER A GUESS: ")
				gameOver = compareNumbers(secretNumber,theGuess)
			if attempts == 0:
				print("\nYOU'VE BEAT THE ODDS...\nYOU GUESSED THE SECRET NUMBER ON THE FIRST TRY.")
			print("THE SECRET NUMBER IS: %d") % (secretNumber) 	
	else:
		print("\nMULTIPLAYER MODE: ON\n")
		os.system('cls')
		secretNumber = input("\nPLAYER 1: ENTER YOUR SECRET NUMBER: ")
		os.system('cls')
		instructions()	
		theGuess = input("PLAYER 2: ENTER A GUESS: ")
		gameOver = compareNumbers(secretNumber,theGuess)
		attempts = 0
		while gameOver == False:
			attempts += 1
			theGuess = input("PLAYER 2: ENTER A GUESS: ")
			gameOver = compareNumbers(secretNumber,theGuess)
		if attempts == 0:
			print("\nYOU'VE BEAT THE ODDS...\nYOU GUESSED THE SECRET NUMBER ON THE FIRST TRY.")

				
#********************************************************************************************************************************************************************************************************************************************		
def greeting():#NOTE: THIS FUNCTION JUST EXPLAINS THE OBJECTIVE OF THE GAME TO THE USER
	print ("WELCOME TO PICA CENTRO!!!\n")
	theirChoice = input("PRESS\n1. INSTRUCTIONS\n2. TO EXIT GAME\n")
	if theirChoice == 2:
		return 0
	elif theirChoice == 1:
		print("OBJECTIVE: TO  SHARPEN THE USERS SKILLS WITH DEDUCTIVE REASONING\n")
		print("THE USER IS TO GUESS WHAT THE SECRET NUMBER IS THROUGH PROCESS OF\n")
		print("ELIMINATION THE USER WILL BE GIVEN HINTS THROUGHOUT THE GAME\n\n")
		print("SCORING:\n")
		print("\tPICA: MEANS ONE OF THE DIGITS IS CORRECT, BUT IN THE WRONG PLACE\n ")
		print("\tCENTRO: MEANS ONE OF THE DIGITS IS CORRECT, AND THAT DIGIT IS IN THE CORRECT PLACE.\n")
		print("**NOTE: THE OBJECTIVE IS TO USE DEDUCTIVE REASONING; THEREFORE IF NEITHER A PICA\n")
		print("OR CENTRO WAS ALLOTTED IT MEANS YOUR GUESS WAS COMPLETLEY INCORRECT.\n")
		x = os.system('pause')
		return theirChoice
#********************************************************************************************************************************************************************************************************************************************		
def instructions():
	print("PICA: MEANS ONE OF THE DIGITS IS CORRECT, BUT IN THE WRONG PLACE\n ")		
	print("CENTRO: MEANS ONE OF THE DIGITS IS CORRECT, AND THAT DIGIT IS IN THE CORRECT PLACE.\n")
#********************************************************************************************************************************************************************************************************************************************
def userMode():
	mode = input("MODE:\n\t1.SINGLE PLAYER\n\t2.MULTIPLAYER")
	if mode == 1:
		return 1
	else:
		return 2	
	return	
#********************************************************************************************************************************************************************************************************************************************
def compareNumbers(secretNumber, theGuess):#THIS FUNCTION IS FOR MULTIPLAYER ONLY IT CHECKS THE GUESSED NUMBER AGAINST THE SECRETNUMBER
	masterSecretNumber = secretNumber
	masterTheGuess = theGuess
	lastIndex = secretNumber % 10
	secretNumber = secretNumber / 10
	middleIndex = secretNumber % 10
	secretNumber = secretNumber / 10
	firstIndex = secretNumber % 10
	lastIndex2 = theGuess % 10
	theGuess = theGuess / 10
	middleIndex2 = theGuess % 10
	theGuess = theGuess / 10
	firstIndex2 = theGuess % 10
	gameOver = False#USED WITH IN MAIN() TO SEE WHEN THE GAME IS FINISHED
	#PICA & CENTRO ARE USED AS ACCUMULATORS
	centro = 0
	pica = 0
	if masterSecretNumber == masterTheGuess:#CHECKS FOR RARE CASE AND PRINTS NICE MSG
		print("\nYOU GUESSED THE SECRET NUMBER CONGRATULATIONS!!!!\n")
		gameOver = True	
	if lastIndex == lastIndex2:
		centro += 1
	if  (middleIndex == lastIndex2) or (firstIndex == lastIndex2) and (lastIndex != lastIndex2):
		pica += 1
	if middleIndex == middleIndex2:
		centro += 1
	if (lastIndex == middleIndex2) or (firstIndex == middleIndex2) and (middleIndex != middleIndex2):	
		pica += 1
	if firstIndex == firstIndex2:
		centro += 1
	if (lastIndex == firstIndex2) or (middleIndex == firstIndex2) and (firstIndex != firstIndex2):		
		pica += 1
	displayResults(pica, centro, masterSecretNumber, masterTheGuess)
	return gameOver	
#********************************************************************************************************************************************************************************************************************************************
def specialCompareNumbers(secretNumber,secretNumberSize, theGuess):#STRICTLY USED FOR SINGLE PLAYER MODE OF EXPERT DIFFICULTY
	if secretNumberSize == 4:#OPTION 1. 4 NUMBERS INSTEAD OF 3
		masterSecretNumber = secretNumber
		masterTheGuess = theGuess
		lastIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		middleIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		secondMiddleIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		firstIndex = secretNumber % 10
		lastIndex2 = theGuess % 10
		theGuess = theGuess / 10
		middleIndex2 = theGuess % 10
		theGuess = theGuess / 10
		secondMiddleIndex2 = theGuess % 10
		theGuess = theGuess / 10
		firstIndex2 = theGuess % 10
		gameOver = False
		centro = 0
		pica = 0
		if masterSecretNumber == masterTheGuess:
			print("\nYOU GUESSED THE SECRET NUMBER CONGRATULATIONS!!!!\n")
			gameOver = True	
		if lastIndex == lastIndex2:
			centro += 1
		if  ((middleIndex == lastIndex2) or (secondMiddleIndex == lastIndex2) or (firstIndex == lastIndex2)) and (lastIndex != lastIndex2):
			pica += 1
		if middleIndex == middleIndex2:
			centro += 1
		if ((lastIndex == middleIndex2) or (firstIndex == middleIndex2) or (secondMiddleIndex == middleIndex2)) and (middleIndex != middleIndex2):	
			pica += 1
		if secondMiddleIndex == secondMiddleIndex2:
			centro += 1
		if ((lastIndex == secondMiddleIndex2) or (firstIndex == secondMiddleIndex2) or (middleIndex == secondMiddleIndex2)) and (secondMiddleIndex != secondMiddleIndex2):	
			pica += 1
		if firstIndex == firstIndex2:
			centro += 1
		if ((lastIndex == firstIndex2) or (middleIndex == firstIndex2) or (secondMiddleIndex == firstIndex2)) and (firstIndex != firstIndex2):	
			pica += 1
		displayResults(pica, centro,masterSecretNumber, masterTheGuess)	
		return gameOver	
	elif secretNumberSize == 5:	#OPTION 2. 5 NUMBERS INSTEAD OF 3 OR 4

		masterSecretNumber = secretNumber
		masterTheGuess = theGuess
		lastIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		secondlastIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		middleIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		secondMiddleIndex = secretNumber % 10
		secretNumber = secretNumber / 10
		firstIndex = secretNumber % 10
		lastIndex2 = theGuess % 10
		theGuess = theGuess / 10
		secondlastIndex2 = theGuess % 10
		theGuess = theGuess / 10
		middleIndex2 = theGuess % 10
		theGuess = theGuess / 10
		secondMiddleIndex2 = theGuess % 10
		theGuess = theGuess / 10
		firstIndex2 = theGuess % 10
		gameOver = False
		centro = 0
		pica = 0
		
		if masterSecretNumber == masterTheGuess:
			print("\nYOU GUESSED THE SECRET NUMBER CONGRATULATIONS!!!!\n")
			gameOver = True	
		if lastIndex == lastIndex2:
			centro += 1
		if  ((middleIndex == lastIndex2) or (secondMiddleIndex == lastIndex2) or (firstIndex == lastIndex2) or (secondlastIndex == lastIndex2)) and (lastIndex != lastIndex2):
			pica += 1
		if secondMiddleIndex == secondlastIndex2:
			centro += 1
		if  ((middleIndex == secondlastIndex2) or (lastIndex == secondlastIndex2) or (firstIndex == secondlastIndex2) or (secondlastIndex == secondlastIndex2)) and (secondMiddleIndex != secondlastIndex2):
			pica += 1
		if middleIndex == middleIndex2:
			centro += 1
		if ((lastIndex == middleIndex2) or (firstIndex == middleIndex2) or (secondMiddleIndex == middleIndex2) or (secondlastIndex == middleIndex2)) and (middleIndex != middleIndex2):	
			pica += 1
		if secondMiddleIndex == secondMiddleIndex2:
			centro += 1
		if ((lastIndex == secondMiddleIndex2) or (firstIndex == secondMiddleIndex2) or (middleIndex == secondMiddleIndex2) or (secondlastIndex == secondMiddleIndex2)) and (secondMiddleIndex != secondMiddleIndex2):	
			pica += 1
		if firstIndex == firstIndex2:
			centro += 1
		if ((lastIndex == firstIndex2) or (middleIndex == firstIndex2) or (secondMiddleIndex == firstIndex2) or (secondlastIndex == firstIndex2)) and (firstIndex != firstIndex2):		
			pica += 1
		displayResults(pica, centro, masterSecretNumber, masterTheGuess)
		return gameOver	

#********************************************************************************************************************************************************************************************************************************************	
def difficulty():
	skillLevel = input("\nSELECT YOUR SKILL LEVEL:\n\t1: BEGINNER\n\t2. EXPERT\n")
	return skillLevel	
#********************************************************************************************************************************************************************************************************************************************	
def RNG(secretNumberSize):#RANDOM NUMBER GENERATOR() RECIEVE THE SECRETNUMBERSIZE TO DETERMINE THE LENGTH OF THE RANDOMIZE SECRETNUMBER
	if secretNumberSize == 4:
		secretNumber = random.randint(1000, 10000)
	elif secretNumberSize == 5:
		secretNumber = random.randint(10000, 100000)
	else:
		secretNumber = random.randint(100, 1000)
	return secretNumber 
#********************************************************************************************************************************************************************************************************************************************	
def displayResults(pica, centro, masterSecretNumber, masterTheGuess):
	if masterTheGuess == masterSecretNumber:
		print("%d | PICA COUNT: %d CENTRO COUNT: %d") % (masterTheGuess, pica,centro)
	else:
		print("%d | PICA COUNT: %d CENTRO COUNT: %d") % (masterTheGuess, pica,centro)
	
main()