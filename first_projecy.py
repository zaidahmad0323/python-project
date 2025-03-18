print("Choose 0 for rock 1 for paper and 2 for scissor")
import random
user_choice=int(input("Select the number : ")) 
computer_choice=random.randint(0,2)
print(computer_choice)
if user_choice>2 or user_choice<0:
    print("Invalid entry, you lost the match ")
else :
    if user_choice==0 and computer_choice==2:
        print("The computer won the match ")
    elif user_choice==2 and computer_choice==0:
        print("The user won the match ")
    elif user_choice>computer_choice:
        print("The user won the match ")  
    elif computer_choice>user_choice:
        print("The computer won the match")
    else:
        print("The match has dropped ")                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    