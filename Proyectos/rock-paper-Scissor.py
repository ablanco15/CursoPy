from operator import truediv
import random
mylist = ["r", "s", "p"]
pc_points, user_points = 0,0


def play():
    def review(use,pcs):
        if(use == "r" and pcs == "s"):
            return "user"
        elif(use == "s" and pcs == "r"):
            return "pc"

        if(use == "r" and pcs == "p"):
            return "pc"
        elif(use == "p" and pcs == "r"):
            return "user" 

        if(use == "p" and pcs == "s"):
            return "pc"
        elif(use == "s" and pcs == "p"):
            return "user"  

        if(use == pcs):
            return "equal"

    correct = False
    while(not correct):
        user = input("introduce an option: rock(r), paper(p), scissor(s): ")
        if(user in mylist):
            correct=True
    posi = random.randint(0,2)
    pc = mylist[posi] 
    winner = review(user,pc)
    print()
    print("user: " + user+ "    pc: " + pc)
    print()
    return winner

def score(pc, user):
    print()
    print("Score")
    print()
    print("pc: " + str(pc_points) + " user: "+ str(user_points) )
    print()

         
counter = 0   
while( pc_points < 2  and user_points < 2 ):
    score(pc_points,user_points)
    winner = play()
    if(winner == "pc"):
        pc_points+=1
        print("pc got 1 point")
        print()
    elif(winner == "user"):
        user_points+=1
        print("user got 1 point")
        print()
    else:
        print("it's a draw, anyone got points") 
    counter+=1       
score(pc_points,user_points)
if(user_points > pc_points):
    print("Congrats! you've won ")
else:
    print("the pc has won, try again")
