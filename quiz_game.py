print ("Welcome to my computer quiz!")

playing = input("Do you want to play? ") #input is asking a question to the user, ie input cause it needs an input from the user to continue 

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!! ")
score = 0 # keep track of how many questions users gets right

answer = input("What does CPU stand for? ") # answer is asking the user what's does a CPU stand for, and it prompt the user to answer too
if answer.lower() == "central processing unit": #.lower() means whatever the answer is it will take it and make it all lower case. so that the user to type in all caps and still be fine
    print('Correct!') # doesn't matter if you use single or double quotes just be consistent with that you use
    score += 1
else: 
    print('Incorrect!')

answer = input("What does GPU stand for? ") 
if answer.lower() == "graphics processing unit": 
    print('Correct!') 
    score += 1
else: 
    print('Incorrect!')

answer = input("What does PSU stand for? ") 
if answer.lower() == "power supply unit": 
    print('Correct!') 
    score += 1
else: 
    print('Incorrect!')

answer = input("Who has the best pc ever? ") 
if answer.lower() == "raag patel": 
    print('Correct!') 
    score += 1
else: 
    print('Incorrect!')

print ("you got " + str(score) + "questions right! ") #numbers of questions gotten correctly 
print ("you got " + str((score/4) * 100) + "%! ") #gives the quiz percentage