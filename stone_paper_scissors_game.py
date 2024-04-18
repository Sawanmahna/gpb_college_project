'''
Date: 18/04/2024
@author: Sawanmahna
'''
def game():
    import random

    # Generate a random integer between 1 and 3
    mac = random.randint(1, 3)


    print("Stone = 1 , Paper = 2 , Scissor = 3 \n")

    human = int(input("Enter your input: "))


    print("\n\t\t[You]\t\t\t\t\t\t","[Computer]")

    #print User Input

    if(human==1):
        print("\t\tStone",end="\t\t\t\t\t\t ")
    elif(human==2):
        print("\t\tPaper",end="\t\t\t\t\t\t ")
    elif(human==3):
        print("\t\tScissor",end="\t\t\t\t\t\t ")
    else:
        return 0
        
        
    #Print System input
    if(mac==1):
        print("Stone\n")
    elif(mac==2):
        print("Paper\n")
    elif(mac==3):
        print("Scissor\n")
    


    if((human==1 and mac==3) or (human==2 and mac==1) or (human==3 and mac==2)):
        print("\t\t\t\t\tYou win !")
    elif((human==1 and mac==2) or (human==2 and mac==3) or (human==3 and mac==1)):
        print("\t\t\t\t\tYou loss !")
    elif(human==mac):
        print("\t\t\t\t\tTie !")

    print("Do you want to play again?, Press 1 to start again else 0 : ")
    a=int(input())
    #print("")
    if(a==1):
        game()
    
        
print("[Welcome to Stone, Paper & Scissor Game]\n")

game()




















