# Quiz strings:
easyq = '''Earth is our home planet. Scientists believe Earth and its ___1___ formed around the same
time as the rest of the solar system. They think that was about 4.5 ___2___ years ago.
Earth is the fifth-largest planet in the solar system. Its diameter is about 8,000 miles.
And Earth is the third-closest planet to the sun. Its average ___3___ from the sun is
about 93 million miles. Only Mercury and ___4___ are closer.'''
mediumq = '''Despite the common conceptions of deserts as ___1___ and hot, there are cold deserts as well.
The largest hot desert in the world, northern Africa's ___2___, reaches temperatures of 
up to 122 degrees Fahrenheit (50 degrees Celsius) during the ___3___. But some deserts are
always cold, like the ___4___ desert in Asia and the desert on the continent of Antarctica.
Others are mountainous. Only about 10 percent of deserts are covered by ___5___ dunes.'''
hardq = '''___1___ was the first national park ever to exist, designated in ___2___. Its status
sparked an idea that ___3___ across the country and then across the world. National parks
were spaces that ___4___ deemed precious and worth protecting. ___5___, Mount Rainier,
Wind Cave and Mesa Verde all gained status too, until eventually, in 1916, the National
Parks System was created. One ___6___ charged with overseeing all aspects of these wildernesses.'''

#Quiz answers:
easyans = ['moon', 'billion', 'distance', 'Venus']
mediumans = ['dry', 'Sahara', 'day', 'Gobi', 'sand' ]
hardans = ['Yellowstone', '1872', 'spread', 'humankind', 'Yosemite', 'entity']

# Blank spaces placeholder
blanks = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___']

# Define maximum tries.
maxtries = 3

'''
This function replaces all the blanks that was answered. Based on part_of_the_speech quiz on lesson 13.
Inputs are the current quiz(quiz), current answer list(answers) and number of blanks to be replaced (index).
The output is the quiz with the blank replaced.
'''
def update_quiz (quiz, answers, index):
	replaced = []		#initial empty list that will eventually contain the current quiz
	blank_index = 0		#index of the blanks that needs to be filled up
	split_quiz = quiz.split()
	for word in split_quiz:
		if blank_index <= index and blanks[blank_index] in word:
			if word != blanks[blank_index]:
				word = answers[blank_index] + word[-1] #fix for blanks with symbol
			else:
				word = answers[blank_index]				
			replaced.append(word)
			blank_index += 1
		else:
			replaced.append(word)
	return " ".join(replaced)

'''
This function will get user answer and compared it to the answer key.
Inputs are the current quiz(quiz), current answer (answer) and current question number (blank_index).
Output is true if the answer is correct and false if wrong.
'''
def getans_and_check (quiz, current_answer, blank_index):
	useranswer = raw_input('\nWhat is your answer for ' + str(blank_index) + ' ? ')
	if useranswer.lower() == current_answer.lower(): #to avoid being case sensitive
		print '\nYou are right.\n'
		return True
	else:
		print '\nSorry, you are wrong.\n'
		return False

'''
This function gets the outcome of the game. Returns true user won and false if user lost.
Input is the current (quiz) and answer list (answers)
'''
def get_outcome (quiz, answers):
	tries = maxtries
	index = 0
	print quiz #print initial quiz with all blanks
	while tries != 0 and index < len(answers):
		if getans_and_check(quiz, answers[index], index + 1):
			print update_quiz(quiz, answers, index) # print quiz with current correct answers
			index += 1
		else:
			tries -= 1
			print 'You have ' + str(tries) + ' tries left.'
	if tries == 0:
		return False
	else:
		return True

#This function will return quiz and answer based on the level selected. 
def level_selector():
	print 'Select the level of difficulty to begin.'
	level = raw_input('Level (1)easy (2)medium (3)hard: ')
	if level == '1':
		print '\nLets start easy level..\n'
		return easyq, easyans
	elif level == '2':
		print '\nLets start medium level..\n'
		return mediumq, mediumans
	elif level == '3':
		print '\nLets start hard level..\n'
		return hardq, hardans
	else:
		print '\nLevel out of range, please select from 1 to 3.\n'
		return level_selector()

'''
This is the game main procedure or function. This will get the current quiz and answer list.
Get the outcome of the game and print the results.
'''
def main_game():
	print '\nPlaying Fill-In-The-Blank Game...\n'
	quiz, answers = level_selector()
	if get_outcome(quiz, answers):
		print '\nCongratulations, you WON!'
	else:		
		print '\nGame over. Sorry, you LOST.'

main_game ()