import random, os, time, datetime, argparse

rock = 0
paper = 0
scissors = 0
gamesPlayed = 0
i = 0

tempRockValue = 0
tempScissorsValue = 0
tempPaperValue = 0

longRockValue = 0
longScissorsValue = 0
longPaperValue = 0


parser = argparse.ArgumentParser(description="Simulate a rock paper scissors game for a certain number of rounds and display the results.")
parser.add_argument('-n', nargs=1)
parser.add_argument('-l', nargs=1)
parser.add_argument('-o', nargs=1)
args = parser.parse_args()

print("The following is a program that simulates a rock paper scissors game for a certain number of rounds, and displays the results.")

def askHowManyTimesToRepeat():
    timesToRepeat = int(input("Enter how many rounds of rock paper scissors you want to play: "))
    return timesToRepeat

def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? Y/N: ")
    if logFileYesOrNo.lower() == "y":
        logFileName = input("Log file filename: ")
    else:
        logFileName = "n"
    return logFileName

def askToShowVisualOutput():
    visualOutputYesOrNo = input("Would you like to visually output the result of each game? Y/N: ").lower()
    return visualOutputYesOrNo

def play(times):
	global gamesPlayed, rock, paper, scissors, tempRockValue, tempScissorsValue, tempPaperValue, longRockValue, longPaperValue, longScissorsValue
	for i in range(times):
		play = random.randrange(3)
		gamesPlayed += 1
		if play == 0:
			rock += 1
			tempRockValue += 1
			if longRockValue < tempRockValue:
				if longScissorsValue < tempScissorsValue:
					longScissorsValue = tempScissorsValue
				if longPaperValue < tempPaperValue:
					longPaperValue = tempPaperValue

				tempScissorsValue = 0
				tempPaperValue = 0
			else:
				tempScissorsValue = 0
				tempPaperValue = 0

		elif play == 1:
			paper += 1
			tempPaperValue += 1
			if longPaperValue < tempPaperValue:
				if longScissorsValue < tempScissorsValue:
					longScissorsValue = tempScissorsValue
				if longRockValue < tempRockValue:
					longRockValue = tempRockValue

				tempScissorsValue = 0
				tempRockValue = 0
			else:
				tempScissorsValue = 0
				tempRockValue = 0
		else:
			scissors += 1
			tempScissorsValue += 1
			if longScissorsValue < tempScissorsValue:
				if longScissorsValue < tempScissorsValue: 
					longRockValue = tempRockValue
				if longPaperValue < tempPaperValue:
					longPaperValue = tempPaperValue

				tempRockValue = 0
				tempPaperValue = 0

			else:
				tempRockValue = 0
				tempPaperValue = 0

		if visualOutputYesOrNo == "y":
			print(play, end=" ")


def outputAnalysis():
	global rockPercent, paperPercent, scissorsPercent, difference, longRockValue, longScissorsValue, longPaperValue, elapsedtime
	rockPercent = (100/timesToRepeat)*rock
	paperPercent = (100/timesToRepeat)*paper
	scissorsPercent = (100/timesToRepeat)*scissors



	elapsedtime = str(datetime.timedelta(seconds=round(time.time()-starttime, 2)))
	elapsedtime = elapsedtime[:-4]

	print("\n\n")
	print("Played", timesToRepeat, "rounds of rock paper scissors.")
	print("Total execution time:", elapsedtime)
	print("Opponent played rock", rock, "times, or", rockPercent, "% of the time.")
	print("Opponent played scissors", scissors, "times, or", scissorsPercent, "% of the time.")
	print("Opponent played paper", paper, "times, or", paperPercent, "% of the time.")
	#print("The difference between the two was", difference, ".")
	print("The longest string of rocks played by opponents in a row was:", longRockValue)
	print("The longest string of paper played by opponents in a row was:", longPaperValue)
	print("The longest string of scissors played by opponents in a row was:", longScissorsValue)


def outputLogFile():
	if logFileName.lower() != "n":
		logfile = open(os.getcwd()+'/'+logFileName, 'w')
		logfile.write("Played " + str(timesToRepeat) + " rounds of rock paper scissors.\n")
		logfile.write("Total execution time: " + str(elapsedtime) + "\n")
		logfile.write("Opponent played rock " + str(rock) + " times, or " + str(rockPercent) + "% of the time.\n")
		logfile.write("Opponent played paper " + str(paper) + " times, or " + str(paperPercent) + "% of the time.\n")
		logfile.write("Opponent played scissors " + str(scissors) + " times, or " + str(scissorsPercent) + "% of the time.\n")
		#logfile.write("The difference between the two was " + str(difference) + ".\n")
		logfile.write("The most consecutive times opponent played rock was " + str(longRockValue) + ".\n")
		logfile.write("The most consecutive times opponent played paper was " + str(longPaperValue) + ".\n")
		logfile.write("The most consecutive times opponent played scissors was " + str(longScissorsValue) + ".\n")
		#logfile.write("The amount of time taken to flip each coin on average was " + str(estimate) + ".\n")
		logfile.close()
		print("A logfile was published to ", os.getcwd()+'/'+logFileName)
	else:
		print("No log created.")

if args.n == None:
    timesToRepeat = askHowManyTimesToRepeat()
else:
    timesToRepeat = int(args.n[0])

if args.l == None:
    logFileName = askToLogOrNot()
elif args.l[0].lower() != "no" or args.l[0].lower() != "n":
    logFileName = args.l[0]
else:
    logFileName = "n"

if args.o == None:
    visualOutputYesOrNo = askToShowVisualOutput()
else:
    visualOutputYesOrNo = args.o[0].lower()

starttime = time.time()
play(timesToRepeat)
outputAnalysis()
outputLogFile()