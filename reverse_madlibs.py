QUIZ = ["__0__ is a computer programming language.__0__ was invented to write an operating system called __1__. A __0__ program can vary from 2 lines to millions of lines and it should be written into one or more text files with __2__ \".c \". for example, hello.c. The first __0__ program is however, hello world!.c. __0__ language consists of loops, if-statements, __3__, strings, functions, __4__ .",

"The __0__ programming __1__, is a structure oriented programming __1__, developed by Dennis Ritchie. The UNIX operating system, the __0__ __2__, and essentially all UNIX application programs have been written in  __0__.In order to run a __0__ program, you need a __2__. __2__ change source __3__ to object __3__ and creates executable __4__.  __0__ can be compiled on a variety of computer platforms.",

"__0__ is a Structured __1__. The __2__ you create with your editor are called the __3__ files and they contain the program __3__ codes. The __3__ files for __0__ programs are typically named with the __4__ \".c\".The __3__ code written in __3__ __2__ is the human readable __3__ for your program. It needs to be \"compiled\", into machine __1__ so that your CPU can actually execute the program as per the instructions given"]


ANS = [['c', 'unix', 'extension', 'arrays','pointers'], ['c', 'language', 'compiler', 'code', 'file'], ['c', 'language', 'file', 'source', 'extension']]

def ask_level():
# this function, ask_level doesn't take any input. It asks the user which level they want to enter, till they enter one of these 3 specific
# levels and returns the index value of that level.And if the user enter a wrong choice the prompt appears which says your choice is wrong
# and again asks the user for a specific level from the given levels only.
	levels= ["easy", "medium", "hard"]
	user_input= raw_input("Please select the game dificulty by typing it in\n" + "Posible choices include " + str(levels)+ ":--->> \t")
	for index in xrange(0,3):
		if  levels[index] == user_input:
			return index
	print "wrong choice.\nPlease type correct choice."
	ask_level()

def check_answer(user_input,ans):
# this function, check_answer checks if the user_input is the correct answer or not and pass the message to the user about their answer.
# and returns the value as 1 or 0 if the answer is correct or wrong to the main function (final_quiz).
	if ans == user_input:
		flag=1
		print "Congratulations! Your answer is correct\n So far so good"
		return flag
	else:
		flag = 0
		print "Sorry, wrong answer! Please try again"
		return flag

def question(index_value):
#this function, question asks the question from the user about the quiz. and gets users answer, which is then returned to the main function (final_quiz).
	user_input = raw_input("\n\twhat would come in place of __" + str(index_value)+ "__ ?\t")
	return user_input

def replacement(index_value,user_input,quiz):
#the replacement function replaces the fill_in_blank with users correct answer and returns the now solved quiz.
	blank = "__"+ str(index_value)+"__"
	quiz= quiz.replace(blank, user_input)
	return quiz

def end_of_quiz(level):
# this functions ends our quiz when the level completed by the user is last and when the level completed by the user
# is not last then this function also asks the user if they want to try more levels or not before ending the quiz.
# and if the user want to try more levels, then it returns 1 to the main function (final_quiz).
	print "Congratulations! this level has been completed\n"
	if level!= 2:
		print "if you want to try next level\n"
		user_input = raw_input("Press Y/N for yes or no please.")
		if user_input == 'Y' or user_input == 'y':
			return 1
		elif user_input == 'N' or user_input== 'n':
			return 0
	else:
		print "you are at the end of this quiz.\n\n"
		user_input= raw_input("Press ENTER to end the quiz. \n")
		return 0



def final_quiz(QUIZ, ANS):
#this function is the main body of this program which uses all the above functions for differnt purposes.
	answer = 1
	while answer == 1:
		index=0
		level = ask_level()
		quiz= QUIZ[level]
		ans = ANS[level][index]
		print "\n"
		print quiz
		max_no_of_blanks = 5
		while index < max_no_of_blanks:
			ans = ANS[level][index]
			input1 = question(index)
			answer_flag = check_answer(input1,ans)
			if answer_flag == 1:
				replacing = replacement(index,input1,quiz)
				quiz= replacing
				print "\n"
				print quiz
				index += 1
		answer = end_of_quiz(level)
	print "Thanks for solving the quiz :-)"


print "\t\tWELCOME TO THE FILL_IN_THE_BLANKS QUIZ :-)"
print "\n all answers are in small alphabets\n"
print("\t\t ALL THE VERY BEST")
final_quiz(QUIZ, ANS)
