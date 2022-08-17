from operator import truediv
import random
mylist = ["r", "s", "p"]


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
    print("user: " + user+ "    pc: " + pc)
    return winner

winner = play()

if(winner == "pc"):
    print("the pc has won, try again")
elif(winner == "user"):
    print("Congrats! you've won ")
else:
    print("it's a draw, you should play again")    