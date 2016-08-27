from classes import Card
from Ccounters import Counter
import random
import sys

playerDeck=[]
compDeck=[]
counter = Counter()

"""
playerDeck.append(Card("Attack", True, "Deal 1 basic attack damage.", 1, 0))
playerDeck.append(Card("Block", True, "Block 1 an attack.", 2, 0))
playerDeck.append(Card("Heal", True, "Recieve one Lifepoint.", 3, 0))

compDeck.append(Card("Attack", True, "Deal 1 basic attack damage.", 1, 0))
compDeck.append(Card("Block", True, "Block 1 an attack.", 2, 0))
compDeck.append(Card("Heal", True, "Recieve one Lifepoint.", 3, 0))
#name, isCoreCard, description, firstAction, secondAction
"""

basicCardList=[]
sCardList=[]
for x in range(0,5):
    basicCardList.append(Card("Attack", False, "Deal 1 basic attack damage.", 1, 0))
    basicCardList.append(Card("Block", False, "Block an attack.", 2, 0))
    basicCardList.append(Card("Heal", False, "Receive one Lifepoint.", 3, 0))

for x in range(0,10):
    ri=random.randrange(0, len(basicCardList))
    compDeck.append(basicCardList[ri])
    basicCardList.pop(ri)

for x in range(0,2):
    sCardList.append(Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1))
    sCardList.append(Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0))
    sCardList.append(Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3))
    sCardList.append(Card("Double Block", False, "1st Action: Block" + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2))
    sCardList.append(Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1))
    sCardList.append(Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0))
    sCardList.append(Card("Life Boost", False, "1st Action: Increase Max Life by 1 " + " 2nd Action: Heal" + "Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3))
    sCardList.append(Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0))
    sCardList.append(Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0))

for x in range(0,17):
    ri=random.randrange(0, len(sCardList))
    compDeck.append(sCardList[ri])
    sCardList.pop(ri)

print("Starter Deck or Customized Deck?")
print("[1] Starter Deck")
print("[2] Customized Deck")
userInput=input("Select a Deck")
if userInput=="1":
    for x in range(0,4):
        playerDeck.append(Card("Attack", False, "Deal 1 basic attack damage.", 1, 0))
    for x in range(0,3):
        playerDeck.append(Card("Block", False, "Block an attack.", 2, 0))
        playerDeck.append(Card("Heal", False, "Receive one Lifepoint.", 3, 0))
    for x in range(0,2):
        playerDeck.append(Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0))
        playerDeck.append(Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0))
        playerDeck.append(Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3))
        playerDeck.append(Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0))
        playerDeck.append(Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1))
        playerDeck.append(Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1))
        playerDeck.append(Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0))
        playerDeck.append(Card("Life Boost", False, "1st Action: Increase Max Life by 1(Not a Heal) " + " 2nd Action: Heal " + " *Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3))
    playerDeck.append(Card("Double Block", False, "1st Action: Block " + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2))

elif userInput=="2":
    for x in range(0,27):
        print()
        print()
        print("Customize your Deck")
        print("[1] Basics")
        print("[2] Specials")
        userInput=input("Select your Cards")
        if userInput=="1" and counter.basicAtkCounter+counter.basicBlkCounter+counter.basicHlCounter<10:
            print()
            print("Basics: 5 Max each")
            print("[1] Attack")
            print("[2] Block")
            print("[3] Heal")
            userInput=input("Select your Cards")
            if userInput=="1" and counter.basicAtkCounter<5:
                playerDeck.append(Card("Attack", False, "Deal 1 basic attack damage.", 1, 0))
                counter.basicAtkCounter+=1
                print("Attack: " + str(counter.basicAtkCounter))
            elif userInput=="2" and counter.basicBlkCounter<5:
                playerDeck.append(Card("Block", False, "Block an attack.", 2, 0))
                counter.basicBlkCounter+=1
                print("Block: " + str(counter.basicBlkCounter))
            elif userInput=="3" and counter.basicHlCounter<5:
                playerDeck.append(Card("Heal", False, "Recieve one Lifepoint.", 3, 0))
                counter.basicHlCounter+=1
                print("Heal: " + str(counter.basicHlCounter))
            else:
                print("Already have 5 of this card!")
        elif userInput=="2" and counter.doubleAtkCounter +counter.mightySwgCounter +counter.strHlCounter +counter.doubleBlkCounter +counter.BlkStrCounter +counter.superHlCounter +counter.lifeBoostCounter+counter.overKillCounter<17:
                print("Specials: 2 Max each")
                print("[1] Double Attack")
                print("[2] Mighty Swing")
                print("[3] Strike & Heal")
                print("[4] Double Block")
                print("[5] Block & Strike")
                print("[6] Super Heal")
                print("[7] Life Boost")
                print("[8] Overkill")
                print("[9] Parry")
                userInput=input("Select your Cards")
                if userInput=="1" and counter.doubleAtkCounter<2:
                    playerDeck.append(Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1))
                    counter.doubleAtkCounter+=1
                    print("Double Attack: " + str(counter.doubleAtkCounter))
                elif userInput=="2" and counter.mightySwgCounter<2:
                    playerDeck.append(Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0))
                    counter.mightySwgCounter+=1
                    print("Mighty Swing: " + str(counter.mightySwgCounter))
                elif userInput=="3" and counter.strHlCounter<2:
                    playerDeck.append(Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3))
                    counter.strHlCounter+=1
                    print("Strike & Heal: " + str(counter.strHlCounter))
                elif userInput=="4" and counter.doubleBlkCounter<2:
                    playerDeck.append(Card("Double Block", False, "1st Action: Block " + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2))
                    counter.doubleBlkCounter+=1
                    print("Double Block: " + str(counter.doubleBlkCounter))
                elif userInput=="5" and counter.BlkStrCounter<2:
                    playerDeck.append(Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1))
                    counter.BlkStrCounter+=1
                    print("Block & Strike: " + str(counter.BlkStrCounter))
                elif userInput=="6" and counter.superHlCounter<2:
                    playerDeck.append(Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0))
                    counter.superHlCounter+=1
                    print("Super Heal: " + str(counter.superHlCounter))
                elif userInput=="7" and counter.lifeBoostCounter<2:
                    playerDeck.append(Card("Life Boost", False, "1st Action: Increase Max Life by 1(Not a Heal) " + " 2nd Action: Heal " + " *Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3))
                    counter.lifeBoostCounter+=1
                    print("Life Boost: " + str(counter.lifeBoostCounter))
                elif userInput=="8" and counter.overKillCounter<2:
                    playerDeck.append(Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0))
                    counter.overKillCounter+=1
                    print("OverKill: " + str(counter.overKillCounter))
                elif userInput=="9" and counter.perryCounter<2:
                    playerDeck.append(Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0))
                    counter.perryCounter+=1
                    print("Parry: " + str(counter.perryCounter))
                else:
                    print("Already have 2 of this card!")
        else:
            print("Already Full there.")
#print("[1]" + pHand[0])

playerHand=[]
compHand=[]
playerCard = ""
compCard = ""


playerHealth=7
compHealth=7

random.shuffle(playerDeck)
random.shuffle(compDeck)

playerLimit=7
compLimit=7

while playerHealth>0 and compHealth>0:
    playerHand.append(Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0))
    playerHand.append(Card("Block(Core)", True, "Block an attack.", 2, 0))
    playerHand.append(Card("Heal(Core)", True, "Recieve one Lifepoint.", 3, 0))

    compHand.append(Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0))
    compHand.append(Card("Block(Core)", True, "Block an attack.", 2, 0))
    compHand.append(Card("Heal(Core)", True, "Recieve one Lifepoint.", 3, 0))

    #dealing
    while len(playerHand) < 7:
        for x in range(0,4):
            playerHand.append(playerDeck[0])
            playerDeck.pop(0)
    while len(compHand) < 7:
        for x in range(0,4):
            compHand.append(compDeck[0])
            compDeck.pop(0)


    #players picking a card
    counter.coreCardCounter = 0
    for x in range(0,5):
        print("")
        print("Your Turn")
        print("Your Health: " + str(playerHealth))
        print("Bot's Health: " + str(compHealth))
        print("Round #"+ str(x+1))
        if x == 2 and counter.coreCardCounter==0: #round 2 and no core cards has been played yet
            for x in range(0, len(playerHand)):
                #print("len playerHand: " + str(len(playerHand)))
                #print("index: " + str(x))
                if playerHand[x].isCoreCard==True:
                    print("[" + str((x+1)) + "] " + playerHand[x].name + ": " + playerHand[x].description)
            userInput=input("Pick a Card")
            if userInput == "1":
                playerCard = playerHand[0]
                playerHand.pop(0)
            elif userInput == "2":
                playerCard = playerHand[1]
                playerHand.pop(1)
            elif userInput == "3":
                playerCard = playerHand[2]
                playerHand.pop(2)
            else:
                print("Didn't enter correctly. Try Again.")
            counter.coreCardCounter += 1
        elif x == 3 and counter.coreCardCounter==1:
            for x in range(0, len(playerHand)):
                if playerHand[x].isCoreCard==True:
                    print("[" + str((x+1)) + "] " + playerHand[x].name + ": " + playerHand[x].description)
            userInput=input("Pick a Card")
            if userInput == "1":
                playerCard = playerHand[0]
                playerHand.pop(0)
            elif userInput == "2":
                playerCard = playerHand[1]
                playerHand.pop(1)
            else:
                print("Didn't enter correctly. Try Again.")
            counter.coreCardCounter += 1
        elif x == 4 and counter.coreCardCounter==2:
            for x in range(0, len(playerHand)):
                if playerHand[x].isCoreCard==True:
                    print("[" + str((x+1)) + "] " + playerHand[x].name + ": " + playerHand[x].description)
            userInput=input("Pick a Card")
            if userInput == "1":
                playerCard = playerHand[0]
                playerHand.pop(0)
            else:
                print("Didn't enter correctly. Try Again.")
        else:
            for x in range(0, len(playerHand)):
                print("[" + str((x+1)) + "] " + playerHand[x].name + ": " + playerHand[x].description)

            userInput=input("Pick a Card")
            if userInput == "1":
                playerCard = playerHand[0]
                playerHand.pop(0)
            elif userInput == "2":
                playerCard = playerHand[1]
                playerHand.pop(1)
            elif userInput == "3":
                playerCard = playerHand[2]
                playerHand.pop(2)
            elif userInput == "4" and len(playerHand) > 3:
                playerCard = playerHand[3]
                playerHand.pop(3)
            elif userInput == "5" and len(playerHand) > 4:
                playerCard = playerHand[4]
                playerHand.pop(4)
            elif userInput == "6" and len(playerHand) > 5:
                playerCard = playerHand[5]
                playerHand.pop(5)
            elif userInput == "7"  and len(playerHand) > 6:
                playerCard = playerHand[6]
                playerHand.pop(6)
            else:
                print("Didn't enter correctly. Try Again.")

        #comp picking a card
        coreCardList = []
        if x == 2 and counter.coreCardCounter==0: #round 2 and no core cards has been played yet
            for x in range(0, len(compHand)):
                if compHand[x].isCoreCard==True:
                    coreCardList.append(coreCardList[x])
                ri = random.randrange(0,len(coreCardList))
                compCard = coreCardList[ri]
                compHand.remove(compCard)
        elif x == 3 and counter.coreCardCounter==1:
            for x in range(0, len(compHand)):
                if compHand[x].isCoreCard==True:
                    coreCardList.append(coreCardList[x])
                ri = random.randrange(0,len(coreCardList))
                compCard = coreCardList[ri]
                compHand.remove(compCard)
        elif x == 4 and counter.coreCardCounter==2:
            for x in range(0, len(compHand)):
                if compHand[x].isCoreCard==True:
                    coreCardList.append(coreCardList[x])
                ri = random.randrange(0,len(coreCardList))
                compCard = coreCardList[ri]
                compHand.remove(compCard)
        else:
            ri = random.randrange(0,len(compHand))
            compCard = compHand[ri]
            compHand.pop(ri)

        print()
        print("Your Card: " + playerCard.name+ "  vs Bot's Card: "+ compCard.name)

        #resolving round
        if playerCard.firstAction==1 and compCard.firstAction==3:
            compHealth-=1
        elif playerCard.firstAction==3 and compCard.firstAction==1:
            playerHealth-=1
        elif playerCard.firstAction==3 and compCard.firstAction==2:
            if playerHealth<playerLimit:
                playerHealth+=1
        elif playerCard.firstAction==2 and compCard.firstAction==3:
            if compHealth<compLimit:
                compHealth+=1
        elif playerCard.firstAction==1 and compCard.firstAction==1:
            compHealth-=1
            playerHealth-=1
        elif playerCard.firstAction==3 and compCard.firstAction==3:
            if compHealth<compLimit:
                compHealth+=1
            if playerHealth<playerLimit:
                playerHealth+=1
        elif playerCard.firstAction==5 and compCard.firstAction==3:
            compHealth-=3
        elif compCard.firstAction==5 and playerCard.firstAction==3:
            playerHealth-=3
        elif playerCard.firstAction==5 and compCard.firstAction==1:
            playerHealth-=1
            compHealth-=2
        elif compCard.firstAction==5 and playerCard.firstAction==1:
            playerHealth-=2
            compHealth-=1
        elif playerCard.firstAction==5 and compCard.firstAction==5:
            playerHealth-=2
            compHealth-=2
        elif playerCard.firstAction==6 and compCard.firstAction==1:
            compHealth-=1
        elif compCard.firstAction==6 and playerCard.firstAction==1:
            playerHealth-=1
        elif playerCard.firstAction==6 and compCard.firstAction==6:
            playerHealth-=1
            compHealth-=1
        elif playerCard.firstAction==7 and compCard.firstAction==2:
            playerHealth-=3
        elif playerCard.firstAction==7 and compCard.firstAction==3:
            compHealth-=4
        elif playerCard.firstAction==7 and compCard.firstAction==1:
            compHealth-=4
            playerHealth-=1
        elif compCard.firstAction==7 and playerCard.firstAction==1:
            playerHealth-=4
            compHealth-=1
        elif compCard.firstAction==7 and playerCard.firstAction==2:
            compHealth-=3
        elif compCard.firstAction==7 and compCard.firstAction==3:
            playerHealth-=4
        elif playerCard.firstAction==7 and compCard.firstAction==5:
            compHealth-=4
            playerHealth-=2
        elif compCard.firstAction==7 and playerCard.firstAction==5:
            playerHealth-=4
            compHealth-=2
        elif playerCard.firstAction==7 and compCard.firstAction==7:
            playerHealth-=4
            compHealth-=4
        elif playerCard.firstAction==4 and compCard.firstAction==3:
            playerLimit+=1
            if compHealth<compLimit:
                compHealth+=1
        elif playerCard.firstAction==4 and compCard.firstAction==4:
            playerLimit+=1
            print(playerLimit)
            compLimit+=1
            print(compLimit)
        elif playerCard.firstAction==4 and compCard.firstAction==2:
            playerLimit+=1
            print(playerLimit)
        elif compCard.firstAction==4 and playerCard.firstAction==2:
            compLimit+=1
            print(compLimit)
        elif compCard.firstAction==4 and playerCard.firstAction==3:
            compLimit+=1
            print(compLimit)
            if playerpHealth<playerLimit:
                playerHealth+=1
        elif playerCard.secondAction==1 and compCard.secondAction==0 or compCard.secondAction==3 or compCard.secondAction==1:
            compHealth-=1
        elif compCard.secondAction==3 and playerCard.secondAction==0 or playerCard.secondAction==2:
            if compHealth<compLimit:
                compHealth+=1
        elif playerCard.secondAction==3 and compCard.secondAction==0 or compCard.secondAction==2:
            if playerHealth<playerLimit:
                playerHealth+=1
        elif playerCard.secondAction==3 and compCard.secondAction==3:
            if compHealth<compLimit:
                compHealth+=1
            if playerHealth<playerLimit:
                playerHealth+=1
        elif compCard.secondAction==1 and playerCard.secondAction==0 or playerCard.secondAction==3:
            playerHealth-=1
        elif compCard.secondAction==1 and playerCard.secondAction==1:
            playerHealth-=1
            compHealth-=1
        elif playerCard.secondAction==2 and compCard.firstAction==2:
            compHealth-=1
        elif compCard.firstAction==2 and compCard.secondAction==2 and playerCard.firstAction==2 and playerCard.secondAction==0 or playerCard.secondAction==1 or playerCard.secondAction==3:
            playerHealth-=1
        elif playerCard.firstAction==2 and playerCard.secondAction==2 and compCard.firstAction==2 and compCard.secondAction==0 or compCard.secondAction==1 or compCard.secondAction==3:
            compHealth-=1

        else:
            if compHealth<=0:
                print("You Won!")
                sys.exit()
            if playerHealth<=0:
                print("Game Over")
                sys.exit()








"""
no action=0
attack=1
defend=2
heal=3
life boost=4
mighty swing=5
perry=6
overkill=7
"""
"""
for m in range(30):
    print(playerDeck)
    print(compDeck)
"""