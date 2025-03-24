import random


emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}
choices=['r','p','s']

def get_user_choice():
    while True:
     user_choice= input("rock,paper,scissors :(r,p,s) ").lower()
     if user_choice not in choices:
        print("Invalid choice")
        return get_user_choice()
     return user_choice
    
def dispaly_choices(user_choice,computer_choice):
         print(f'your choice: {emojis[user_choice]}')
         print(f'computer choice: {emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("It's a tie") 
    elif (
     (user_choice=='r' and computer_choice=='s')or
     (user_choice=='p' and computer_choice=='r')or
     (user_choice=='s' and computer_choice=='p')):
     print("You win!")
    else: 
     print("You lose!")
def play_game():
 while True:
     user_choice=get_user_choice()
     computer_choice = random.choice(choices)
     dispaly_choices( user_choice,computer_choice)  
     determine_winner(user_choice,computer_choice)
     should_continue=input("continue :(y/n) ").lower()
     if should_continue=='n':
            break

play_game()



    