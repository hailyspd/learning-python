#My very first game

from random import randint
num = randint(1,100) #Generation of a random number

print("Welcome to Guess Me Challenge!!")
print("I'll guess a number from 1 to 100")
print("If your first guess is within 10 of the number guessed, I'll return WARM")
print("If your first guess is futher than 10 of the number guessed, I'll return COLD")
print("If your subsequent guess is closer to the number guessed, I'll return WARMER")
print("If your subsequent guess is futher to the number guessed, I'll return COLDER")
print("Let's begin!!!")

guesses = [0] #making an list of the number guesses

while True: 
  x = int(input("Enter your guess: "))
  if x < 1 or x > 100:  
    print("Out of Bounds. Try again")
    continue
  
  if x == num:    #if number guessed by computer and player are equal
    print(f"Congratulations you have guessed the number in only {len(guesses)} guesses")    #f for format
    break   #break the loop after the correct number is guesses 
  guesses.append(x)   #if not the correct number, include the number of guess in the list of guesses

  if guesses[-2]:   #guesses[-2] gives the previous guess
    if abs(num-x) < abs(num-guesses[-2]):  #abs = absolute value
      print("WARMER")                       #comparing the current guess to the number while simultaneously comparing the absolute difference-  
    else:                                     #-between the number and the previous guess and the number
      print("COLDER")
  else:
    if abs(num-x)<=10:            
      print("WARM")
    else:
      print("COLD")