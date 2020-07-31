import random
play = True
win_count = 0
lose_count = 0
tie_count = 0
rock_count = 0
scissors_count = 0
paper_count = 0

cpu_win_rock = 0
plr_win_rock = 0
cpu_win_scis = 0
plr_win_scis = 0
cpu_win_pap = 0
plr_win_pap = 0

cpu_rock_count = 0
cpu_paper_count = 0
cpu_scissors_count = 0

while play == True:
    played = False
    print("It's time for Rock Paper Scissors!")
    print("Choose:")
    print("1.) Rock")
    print("2.) Paper")
    print("3.) Scissors")
    string_choice = "Unchosen"
    string_move = "Unchosen"
    result = "Unkown"
    choice = int(input())
    if choice == 1: #player chooses rock
        string_choice = "Rock"
        move = random.randint(1,3)
        played = True
        rock_count = rock_count + 1
        if move == 1: #cpu chooses rock
            string_move = "Rock"
            result = "Tie!"
            tie_count = tie_count + 1
            cpu_rock_count = cpu_rock_count + 1
        elif move == 2: #cpu chooses paper
            string_move = "Paper"
            result = "You Lose!"
            lose_count = lose_count + 1
            cpu_win_pap = cpu_win_pap + 1
            cpu_paper_count = cpu_paper_count + 1
        elif move == 3: #cpu chooses Scissors
            string_move = "Scissors"
            result = "You Win!"
            win_count = win_count + 1
            plr_win_rock = plr_win_rock + 1
            cpu_scissors_count = cpu_scissors_count + 1
    elif choice == 2: #player chooses paper
        string_choice = "Paper"
        move = random.randint(1,3)
        played = True
        paper_count = paper_count + 1
        if move == 1: #cpu chooses rock
            string_move = "Rock"
            result = "You Win!"
            win_count = win_count + 1
            plr_win_pap = plr_win_pap + 1
            cpu_rock_count = cpu_rock_count + 1
        elif move == 2: #cpu chooses paper
            string_move = "Paper"
            result = "Tie!"
            tie_count = tie_count + 1
            cpu_paper_count = cpu_paper_count + 1
        elif move == 3: #cpu chooses Scissors
            string_move = "Scissors"
            result = "You Lose!"
            lose_count = lose_count + 1
            cpu_win_scis = cpu_win_scis + 1
            cpu_scissors_count = cpu_scissors_count + 1
    elif choice == 3: #player choose scissors
        string_choice = "Scissors"
        move = random.randint(1,3)
        played = True
        scissors_count = scissors_count + 1
        if move == 1: #cpu chooses rock
            string_move = "Rock"
            result = "You Lose!"
            lose_count = lose_count + 1
            cpu_win_rock = cpu_win_rock + 1
            cpu_rock_count = cpu_rock_count + 1
        elif move == 2: #cpu chooses paper
            string_move = "Paper"
            result = "You Win!"
            win_count = win_count + 1
            plr_win_scis = plr_win_scis + 1
            cpu_paper_count = cpu_paper_count + 1
        elif move == 3: #cpu chooses Scissors
            string_move = "Scissors"
            result = "Tie!"
            tie_count = tie_count + 1
            cpu_scissors_count = cpu_scissors_count + 1
    else:
        print("Invalid Choice")

    if played == True:
        print("You chose ", string_choice)
        print("The computer chose ", string_move)
        print(result)

    print("Play again?")
    print("(y)es")
    print("(n)o")
    chosen = False
    while chosen == False:
        play_again = input()
        if play_again == "y" or play_again == "Y":
            chosen = True
        elif play_again == "n" or play_again == "N":
            chosen = True
            play = False
        else:
            print("Invalid Choice, please type y or n.")

print("You won", win_count, "times, lost", lose_count, "times, and tied", tie_count, "times." )
print("You played rock", rock_count, "times, scissors", scissors_count, "times, and paper", paper_count, "times.")

plr_win = plr_win_rock + plr_win_scis + plr_win_pap
cpu_win = cpu_win_rock + cpu_win_scis + cpu_win_pap

if plr_win > cpu_win:
    most = 0
    string_most = "unknown"
    if plr_win_rock > most:
        most = plr_win_rock
        string_most = "Rock."
    if plr_win_scis > most:
        most = plr_win_scis
        string_most = "Scissors."
    if plr_win_pap > most:
        most = plr_win_pap
        string_most = "Paper."
    print("You won the most rounds!")
    print("You won the most rounds using", string_most)
else:
    most = 0
    string_most = "unknown"
    if cpu_win_rock > most:
        most = cpu_win_rock
        string_most = "Rock."
    if cpu_win_scis > most:
        most = cpu_win_scis
        string_most = "Scissors."
    if cpu_win_pap > most:
        most = cpu_win_pap
        string_most = "Paper."
    print("The Computer won the most rounds!")
    print("The Computer won the most rounds using", string_most)

most = 0
string_best = "unknown"
if cpu_scissors_count > most:
    most = cpu_scissors_count
    string_best = "Rock."
if cpu_paper_count > most:
    most = cpu_paper_count
    string_best = "Scissors."
if cpu_rock_count > most:
    most = cpu_rock_count
    string_best = "Paper."

print("Your maximum wins would have been achieved with:", string_best)
