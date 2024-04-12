 ################################
 #YourName
 #YourSection
 #YourStudentIDNumber
 ################################
 #REFERENCES
 #Linksthatyoureferredwhilesolving
 #theproblem
 #http://link.to.an.article/video.com
 ################################
 #SOLUTION
 #YourSolutionScore:
 #Putyournumberhere
 ################################
 
def read_input(game_filename):
    outcome_data = []
    with open (game_filename, "r") as game_file:
        for l in game_file:
            computer_choice, user_choice = l.strip().split()
            outcome_data.append([computer_choice, user_choice])
    return outcome_data
    
def calculate_score(outcome_data):
    final_score = 0
    for computer_choice, user_choice in outcome_data:
        if computer_choice == "A":
            choice_score = 1
        elif computer_choice == "B":
            choice_score = 2
        elif computer_choice == "C":
            choice_score  = 3

        if user_choice == "X":
            decision_score = 0
        elif user_choice == "Y":
            decision_score = 3
        elif user_choice =="Z":
            decision_score = 6
        
        final_score += choice_score + decision_score
    return final_score

file = read_input ("input_7_cap1.txt")
final_score = calculate_score (file)
print("Total score: ", final_score)
     

