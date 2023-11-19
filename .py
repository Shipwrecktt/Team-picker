import random                                                                   

print("welcome to my team allocator")                                           
players =["Player1","Player2","Player3","Player4","Player5","Player6","Player7","Player8"]        #modify the names to whatever you want ^^
while True: 
    random.shuffle(players) 

    response = input("is this Team or individual? \nType team or individual \n")
    if response == "team":

        team1 = players[:len(players)//2]
        print("team 1 captin:" + random.choice(team1))
        print("team 1: ")
        for player in team1:
            print(player)

        team2 = players[len(players)//2:]
        print("\nteam 2 captin:" + random.choice(team2))
        print("team 2: ")
        for player in team2:
            print(player)

        response = input("if you want to go again press y if not press n ")
        if response == "n":
            break

    else:
        for i in range(0, 20, 2):                                 
            print(players[i]+ " vs " + players[i+1])
            start = random.randrange(i, i+2)
            print(players[start] + " starts")

            response = input("would you like to go again if so press y if not press n ") #program will crash if you continue pressing Y
            if response == "n":
                break




