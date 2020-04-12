import random



res = 'y'
while res == 'y':
	guess = 0
	random_num= random.randint(1,10)
	x = int(input("Guess the No:"))
	while x!= random_num:
	
		if x>random_num:
			print("Too High")
			guess+=1
			x = int(input("Guess the No:"))
		elif x < random_num:
			print("Too Low")
			x = int(input("Guess the No:"))
			guess+=1
	print(f"Correct Guess with no of {guess} guesses")
	res = input("Do you want to play again? (y/n)")
		
