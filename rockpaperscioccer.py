import random

choices = ['r', 'p', 's']

choice_meaning = {
    'r': 'Rock',
    's': 'Scissors',
    'p': 'Paper'
}
user_score = 0
ai_score = 0

loop_times = int(input('How many times do you want play?: '))

for i in range(loop_times):

    user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')

    ai_choice = random.choice(choices)
        
    if user_choice in choices:
        print(f'Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
       
        if user_choice == ai_choice:
            print('Tie')
        elif user_choice == 'r' and ai_choice == 's':
            print('user+1!')
            user_score+=1
        elif user_choice == 'p' and ai_choice == 'r':
            print('user+1!')
            user_score+=1
        elif user_choice == 's' and ai_choice == 'p':
            print('user+1!')
            user_score+=1
        else:
            print('AI+1!')
            ai_score+=1
    else:
        print('Invalid input')
    print(f'user score is {user_score} and AI score is {ai_score}')
    print('\n','-'*15,'\n')

if user_score > ai_score:
    print(f'user win! ,user score: {user_score}')
elif ai_score < ai_score:
    print(f'AI win and AI score: {ai_score}')
else:
    print(f'tie , score is {user_score}')

    

