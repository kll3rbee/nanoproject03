# Quiz strings:
easyq = '''Earth is our home planet. Scientists believe Earth and its ___1___ formed around the same
time as the rest of the solar system. They think that was about 4.5 ___2___ years ago.
Earth is the fifth-largest planet in the solar system. Its diameter is about 8,000 miles.
And Earth is the third-closest planet to the sun. Its average ___3___ from the sun is
about 93 million miles. Only Mercury and ___4___ are closer.'''
mediumq = '''Despite the common conceptions of deserts as dry and hot, there are ___1___ deserts as well.
The largest hot desert in the world, northern Africa's ___2___, reaches temperatures of 
up to 122 degrees Fahrenheit (50 degrees Celsius) during the ___3___. But some deserts are
always ___1___, like the ___4___ desert in Asia and the desert on the continent of Antarctica.
Others are mountainous. Only about 10 percent of deserts are covered by ___5___ dunes.'''
hardq = '''___1___ was the first national park ever to exist, designated in ___2___. Its status
sparked an idea that ___3___ across the country and then across the world. National parks
were spaces that human kind deemed ___4___ and worth protecting. ___5___, Mount Rainier,
Wind Cave and Mesa Verde all gained status too, until eventually, in 1916, the National
Parks System was created. One ___6___ charged with overseeing all aspects of these wildernesses.'''

#Quiz answers:
easyans = ['moon', 'billion', 'distance', 'Venus']
mediumans = ['cold', 'Sahara', 'day', 'Gobi', 'sand' ]
hardans = ['Yellowstone', '1872', 'spread', 'precious', 'Yosemite', 'entity']

# Blank spaces 
blanks = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___']

# Tries 
maxtries = 3


def level_selector():
	print 'Select the level of difficulty to begin.'
	level = raw_input('Level (1)easy (2)medium (3)hard: ')
	if level == '1':
		print '\nLets start easy level..\n'
		return int(level), easyq, easyans
	elif level == '2':
		print '\nLets start medium level..\n'
		return int(level), mediumq, mediumans
	elif level == '3':
		print '\nLets start hard level..\n'
		return int(level), hardq, hardans
	else:
		print '\nLevel out of range, please select from 1 to 3.\n'
		return level_selector()

# replace blanks with answer
#def replace_blank (blank_number, useranswer):

#def get_answer (level, quiz, answers):

def main_game():
	print '\nPlaying Fill-In-The-Blank Game...\n'
	level, quiz, answers = level_selector()
#	print level
#	print quiz
#	print answers
#	print len(answers)	
	tries = maxtries
	number_of_blanks = len(answers)
	while tries != 0 or 
		

'''
    if outcome():
       	print 'Congratulations, you won!'
	else:		
		print 'Sorry, you lost.'
'''
main_game ()