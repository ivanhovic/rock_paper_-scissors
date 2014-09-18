import random

def number_to_name(number):
    # convert number to a name using if/elif/else
    
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else: print ("you need to imput a number between 0-4")

def name_to_number(name):
    # convert name to number using if/elif/else
    
    if name == "rock":
        number = 0
        return number
    elif name == "spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else: print ("you need to imput a correct string")

def rpsls(name):

    # convert name to player_number using name_to_number
    print ("Player chooses", name)
    number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5,1)
    print ("Computer chooses", number_to_name(comp_number))
    
    # compute difference of player_number and comp_number modulo five
    # use if/elif/else to determine winner
    if number == comp_number:
        print ("Player and computer tie!")
    elif (number - comp_number)%5<=2:
        print ("PLAYER WINS!!")
    else: print ("COMPUTER WINS!!")

    # convert comp_number to name using number_to_name
    # print results
    print ("")


def play():
    print ('rock, spock, paper, lizard or scissors?')
    name = input()
    rpsls(name)

play()