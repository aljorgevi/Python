import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or any other number to exit.\n"))

        if user_choice < 0 or user_choice > 2:
            print("Invalid input. Exiting the game.")
            break  # Exit the loop if the user enters an invalid input or any other number
        else:
            print(game_images[user_choice])

            computer_choice = random.randint(0, 2)
            print("Computer chose:")
            print(game_images[computer_choice])

            if user_choice == computer_choice:
                print("It's a draw")
            elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
                print("You win!")
            else:
                print("You lose")
    except ValueError:
        print("Invalid input. Please enter a number (0, 1, 2, or any other number to exit).")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break  # Exit the loop if the user does not want to play again
