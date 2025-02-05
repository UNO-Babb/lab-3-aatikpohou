#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play = "Y"
  while play == "Y":
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    player = input("Enter choice (R/P/S): ")
    computer = random.choice(["R", "P", "S"] )
    if computer == "R":
      print ("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")

    if player == "R":
      print ("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    else:
      print("Player chose Scissors")
  #Ask the user if they would like to play again.

    

    if player == "R":
      if computer == "R":
        print("TIE")
        ties = ties + 1

      if computer =="P":
        print("You lose")
        losses = losses + 1 

      if computer == "S":
        print ("You win")
        wins = wins + 1

    if player == "P":
      if computer == "P":
        print("TIE")
        ties = ties + 1

      if computer =="S":
        print("You lose")
        losses = losses + 1 

      if computer == "R":
        print ("You win")
        wins = wins + 1
      
    if player == "S":
      if computer == "S":
        print("TIE")
        ties = ties + 1

      if computer =="R":
        print("You lose")
        losses = losses + 1 

      if computer == "P":
        print ("You win")
        wins = wins + 1
    play = input("Play again? (Y/N): ")
    #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
