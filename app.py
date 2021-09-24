#game game
from random import randint
import time
import os

guess_count = 5
hint_count = 3
def end_screen():
  print("\nSee ya later loser! \n")
  time.sleep(1)
  exit()
  

def counters(guess_count, hint_count):
  print(f"\nNumber of guess left = {guess_count}")
  print(f"Number of hints left = {hint_count}")

def hint(correct,user_guess):
  global hint_count 

  if hint_count != 0:
    if_hint = input("\nDo you want to use hint ? (Y/N): ").lower()
    if if_hint == 'y':
      hint_count -= 1
      if user_guess < correct:
        print(f"\nHINT: your guess {user_guess} is lower than the answer")
      if user_guess > correct:
        print(f"\nHINT: your guess {user_guess} is higher than the answer")
  else:
    is_hint_left = False


def main():
  game_running = True
  is_hint_left = True
  is_guess_left = True
  global guess_count 
  global hint_count 
  
  print("\n---------------------------")
  print("welcome to Guess the number")
  print("---------------------------")
  counters(guess_count, hint_count)


  is_enter = input("\nPress [Enter] to play: ")
  if is_enter == "":
    random_number = randint(0,100)
    while game_running == True:
      correct = random_number
      try:
        user_guess = int(input("\nEnter your guess: "))
        if user_guess == correct:
          print("🏆 Correct!")
          game_running = False
          print("\n----------------------------------")
          play_again = input("Do you want to play again ? (Y/N): ").lower()
          if play_again == 'y':
            os.system('cls')
            guess_count = 5
            hint_count = 3
            main()
          else:
            end_screen()
            
        else:
          print("-------------------\n")
          print("❌ Incorrect")
          print(f"Your guess = {user_guess}")
          
          guess_count -= 1
          if guess_count == 0:
            is_guess_left = False
            game_running = False
            print(f"The correct answer was {correct}")
            print("\n----------------------------------")
            play_again = input("Do you want to play again ? (Y/N): ").lower()
            if play_again == 'y':
              os.system('cls')
              guess_count = 5
              hint_count = 3
              main()
            else:
              end_screen()
          if is_guess_left == True:
            counters(guess_count, hint_count)
          if is_hint_left == True: 
            hint(correct,user_guess)
      except ValueError:
        pass
  else:
    end_screen()
    
main()