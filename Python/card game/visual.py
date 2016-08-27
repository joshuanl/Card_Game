import pygame
import sys
import random
import time
from pygame.locals import *
from Card import Card
from Ccounters import Counter



class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

playerHandPos = [Point(48,420), Point(152,420), Point(256,420), Point(360,420), Point(464,420), Point(567,420), Point(671,420)]
playerCardPos = Point(308,219)
compCardPos = Point(619,219)
compHandPos = [Point(246,13), Point(351, 13), Point(456,13), Point(561,13), Point(666,13), Point(771,13), Point(877,13)]
graveyardPos = Point(871,265)
deckPos = Point(871,419)
displayCardPos = Point(7,13)

playerDeck=[]
compDeck=[]
trashCards = []
counter = Counter()
playerHand = []
compHand = []
playerCard=""
compCard=""
goNextRound = True
onlyCoreCards = False
enlargedCard = Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0, 0, 0)
enlargedCard.showCardBack()
enlargedCardPos=Point(11,18)


pygame.init()
screen = pygame.display.set_mode((1024,576))

main_clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)
background_image = pygame.image.load(r"images\field2.png")
pygame.display.set_caption("RoboTech")


draw_group = pygame.sprite.LayeredUpdates()
player_group = pygame.sprite.LayeredUpdates()
comp_group = pygame.sprite.LayeredUpdates()


random.shuffle(playerDeck)
random.shuffle(compDeck)

compCardSelected = False
playerCardSelected = False
cardInPlay = False
draw = True
counter = Counter()
playerHealth=7
compHealth=7
playerLimit=7
compLimit=7


#functions

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (255, 255, 255))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

def createStarterDeck():


    basicCardList=[]
    sCardList=[]
    for x in range(0,5):
        basicCardList.append(Card("Attack", False, "Deal 1 basic attack damage.", 1, 0, 0, 0))
        basicCardList.append(Card("Block", False, "Block an attack.", 2, 0, 0, 0))
        basicCardList.append(Card("Heal", False, "Receive one Lifepoint.", 3, 0, 0, 0))

    for x in range(0,10):
        ri=random.randrange(0, len(basicCardList))
        compDeck.append(basicCardList[ri])
        basicCardList.pop(ri)

    for x in range(0,2):
        sCardList.append(Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1, 0, 0))
        sCardList.append(Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0, 0, 0))
        sCardList.append(Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3, 0, 0))
        sCardList.append(Card("Double Block", False, "1st Action: Block" + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2, 0, 0))
        sCardList.append(Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1, 0, 0))
        sCardList.append(Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0, 0, 0))
        sCardList.append(Card("Life Boost", False, "1st Action: Increase Max Life by 1 " + " 2nd Action: Heal" + "Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3, 0, 0))
        sCardList.append(Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0, 0, 0))
        sCardList.append(Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0, 0, 0))

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
            playerDeck.append(Card("Attack", False, "Deal 1 basic attack damage.", 1, 0, 0, 0))
        for x in range(0,3):
            playerDeck.append(Card("Block", False, "Block an attack.", 2, 0, 0, 0))
            playerDeck.append(Card("Heal", False, "Receive one Lifepoint.", 3, 0, 0, 0))
        for x in range(0,2):
            playerDeck.append(Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0, 0, 0))
            playerDeck.append(Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0, 0, 0))
            playerDeck.append(Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3, 0, 0))
            playerDeck.append(Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0, 0, 0))
            playerDeck.append(Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1, 0, 0))
            playerDeck.append(Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1, 0, 0))
            playerDeck.append(Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0, 0, 0))
            playerDeck.append(Card("Life Boost", False, "1st Action: Increase Max Life by 1(Not a Heal) " + " 2nd Action: Heal " + " *Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3, 0, 0))
        playerDeck.append(Card("Double Block", False, "1st Action: Block " + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2, 0, 0))

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
                    playerDeck.append(Card("Attack", False, "Deal 1 basic attack damage.", 1, 0, 0, 0))
                    counter.basicAtkCounter+=1
                    print("Attack: " + str(counter.basicAtkCounter))
                elif userInput=="2" and counter.basicBlkCounter<5:
                    playerDeck.append(Card("Block", False, "Block an attack.", 2, 0, 0, 0))
                    counter.basicBlkCounter+=1
                    print("Block: " + str(counter.basicBlkCounter))
                elif userInput=="3" and counter.basicHlCounter<5:
                    playerDeck.append(Card("Heal", False, "Recieve one Lifepoint.", 3, 0, 0, 0))
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
                        playerDeck.append(Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1, 0, 0))
                        counter.doubleAtkCounter+=1
                        print("Double Attack: " + str(counter.doubleAtkCounter))
                    elif userInput=="2" and counter.mightySwgCounter<2:
                        playerDeck.append(Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0, 0, 0))
                        counter.mightySwgCounter+=1
                        print("Mighty Swing: " + str(counter.mightySwgCounter))
                    elif userInput=="3" and counter.strHlCounter<2:
                        playerDeck.append(Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3, 0, 0))
                        counter.strHlCounter+=1
                        print("Strike & Heal: " + str(counter.strHlCounter))
                    elif userInput=="4" and counter.doubleBlkCounter<2:
                        playerDeck.append(Card("Double Block", False, "1st Action: Block " + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2, 0, 0))
                        counter.doubleBlkCounter+=1
                        print("Double Block: " + str(counter.doubleBlkCounter))
                    elif userInput=="5" and counter.BlkStrCounter<2:
                        playerDeck.append(Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1, 0, 0))
                        counter.BlkStrCounter+=1
                        print("Block & Strike: " + str(counter.BlkStrCounter))
                    elif userInput=="6" and counter.superHlCounter<2:
                        playerDeck.append(Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0, 0, 0))
                        counter.superHlCounter+=1
                        print("Super Heal: " + str(counter.superHlCounter))
                    elif userInput=="7" and counter.lifeBoostCounter<2:
                        playerDeck.append(Card("Life Boost", False, "1st Action: Increase Max Life by 1(Not a Heal) " + " 2nd Action: Heal " + " *Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3, 0, 0))
                        counter.lifeBoostCounter+=1
                        print("Life Boost: " + str(counter.lifeBoostCounter))
                    elif userInput=="8" and counter.overKillCounter<2:
                        playerDeck.append(Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0, 0, 0))
                        counter.overKillCounter+=1
                        print("OverKill: " + str(counter.overKillCounter))
                    elif userInput=="9" and counter.perryCounter<2:
                        playerDeck.append(Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0, 0, 0))
                        counter.perryCounter+=1
                        print("Parry: " + str(counter.perryCounter))
                    else:
                        print("Already have 2 of this card!")
            else:
                print("Already Full there.")

def drawCards():
    #print("len of playerHand: " + str(len(playerHand)))
    popList = []
    for index in range(0, len(playerHand)):
        #print("index: " + str(index))
        if playerHand[index].cardPlayed==True:
            playerCardSelected.rect.x = graveyardPos.x
            playerCardSelected.rect.y = graveyardPos.y
            popList.append(index)
    popList.sort()
    popList.reverse()
    while len(popList) > 0:
        playerHand.pop(popList[0])
        popList.pop(0)

    playerHand.append(Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0, 0, 0))
    playerHand.append(Card("Block(Core)", True, "Block an attack.", 2, 0, 0, 0))
    playerHand.append(Card("Heal(Core)", True, "Recieve one Lifepoint.", 3, 0, 0, 0))

    compHand.append(Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0, 0, 0))
    compHand.append(Card("Block(Core)", True, "Block an attack.", 2, 0, 0, 0))
    compHand.append(Card("Heal(Core)", True, "Recieve one Lifepoint.", 3, 0, 0, 0))

    while len(playerHand) < 7:
        for x in range(0,4):
            playerHand.append(playerDeck[0])
            playerDeck.pop(0)
    while len(compHand) < 7:
        for x in range(0,4):
            compHand.append(compDeck[0])
            compDeck.pop(0)

def drawDeck():
    for x in range(0, len(playerDeck)):
        playerDeck[x].rect.x = deckPos.x
        playerDeck[x].rect.y = deckPos.y
        draw_group.add(playerDeck[x])

def allCardsToDeck():
    #print("playerDeck len: " + str(len(playerDeck)))
    for x in range(0, len(playerDeck)):
        playerDeck[x].rect.x = deckPos.x
        playerDeck[x].rect.y = deckPos.y
        playerDeck[x].showCardBack()

    for x in range(0, len(compDeck)):
        compDeck[x].showCardBack()

def loadImage(card):
    #print("card name: " + card.name)
    if card.name == "Attack(Core)":
        card.image = pygame.image.load(r"images\coreA.png")
    elif card.name == "Block(Core)":
        card.image = pygame.image.load(r"images\coreB.png")
    elif card.name == "Heal(Core)":
        card.image = pygame.image.load(r"images\coreH.png")
    elif card.name == "Attack":
        card.image = pygame.image.load(r"images\attack.png")
    elif card.name == "Block":
        card.image = pygame.image.load(r"images\block.png")
    elif card.name == "Heal":
        card.image = pygame.image.load(r"images\heal.png")
    elif card.name == "Double Attack":
        card.image = pygame.image.load(r"images\dblatk.png")
    elif card.name == "Mighty Swing":
        card.image = pygame.image.load(r"images\mightyswing.png")
    elif card.name == "Strike & Heal":
        card.image = pygame.image.load(r"images\strhl.png")
    elif card.name == "Double Block":
        card.image = pygame.image.load(r"images\dblblk.png")
    elif card.name == "Block & Strike":
        card.image = pygame.image.load(r"images\blockstrike.png")
    elif card.name == "Super Heal":
        card.image = pygame.image.load(r"images\superhl.png")
    elif card.name == "Life Boost":
        card.image = pygame.image.load(r"images\life boost.png")
    elif card.name == "Overkill":
        card.image = pygame.image.load(r"images\overkill.png")
    elif card.name == "Parry":
        card.image = pygame.image.load(r"images\parry.png")

def loadCImage(card):
    #print("card name: " + card.name)
    if card.name == "Attack(Core)":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Block(Core)":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Heal(Core)":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Attack":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Block":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Heal":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Double Attack":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Mighty Swing":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Strike & Heal":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Double Block":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Block & Strike":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Super Heal":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Life Boost":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Overkill":
        card.image = pygame.image.load(r"images\backcover.png")
    elif card.name == "Parry":
        card.image = pygame.image.load(r"images\backcover.png")

def loadCSImage(card):
    if card.name == "Attack(Core)":
        card.image = pygame.image.load(r"images\coreA.png")
    elif card.name == "Block(Core)":
        card.image = pygame.image.load(r"images\coreB.png")
    elif card.name == "Heal(Core)":
        card.image = pygame.image.load(r"images\coreH.png")
    elif card.name == "Attack":
        card.image = pygame.image.load(r"images\attack.png")
    elif card.name == "Block":
        card.image = pygame.image.load(r"images\block.png")
    elif card.name == "Heal":
        card.image = pygame.image.load(r"images\heal.png")
    elif card.name == "Double Attack":
        card.image = pygame.image.load(r"images\dblatk.png")
    elif card.name == "Mighty Swing":
        card.image = pygame.image.load(r"images\mightyswing.png")
    elif card.name == "Strike & Heal":
        card.image = pygame.image.load(r"images\strhl.png")
    elif card.name == "Double Block":
        card.image = pygame.image.load(r"images\dblblk.png")
    elif card.name == "Block & Strike":
        card.image = pygame.image.load(r"images\blockstrike.png")
    elif card.name == "Super Heal":
        card.image = pygame.image.load(r"images\superhl.png")
    elif card.name == "Life Boost":
        card.image = pygame.image.load(r"images\life boost.png")
    elif card.name == "Overkill":
        card.image = pygame.image.load(r"images\overkill.png")
    elif card.name == "Parry":
        card.image = pygame.image.load(r"images\parry.png")

def displayHand():
    foo = 0
    #draw_group.empty()
    player_group.empty()
    comp_group.empty()
    #for x in range(0,7):
        #print(str(playerHandPos[x].x) + ", " + str(playerHandPos[x].y))
    for x in range(0,7):
        playerHand[x].rect.x=playerHandPos[x].x
        playerHand[x].rect.y=playerHandPos[x].y
        compHand[x].rect.x=compHandPos[x].x
        compHand[x].rect.y=compHandPos[x].y
        #print("pos: " + str(x) + " (" + str(playerHand[x].rect.x) + ", " + str(playerHand[x].rect.y) + ")")
        loadImage(playerHand[x])
        loadCImage(compHand[x])
        draw_group.add(playerHand[x])
        player_group.add(playerHand[x])
        draw_group.add(compHand[x])
        comp_group.add(compHand[x])

def getCardIndex(sprite):
    counter = 0
    for point in playerHandPos:
        if sprite.rect.x == point.x and sprite.rect.y == point.y:
            return counter
        counter += 1
    return -1

def CompChoosesCard():
    foo = 0
    global compCardSelected

    ri = random.randrange(0,len(compHand))
    compCardSelected = compHand[ri]
    compHand.pop(ri)
    compCardSelected.rect.x=compCardPos.x
    compCardSelected.rect.y=compCardPos.y
    draw_group.remove(compCardSelected)
    draw_group.add(compCardSelected)

def resolveRound():

    foo=0
    global playerCardSelected
    global compCardSelected
    global playerHealth
    global compHealth
    global playerLimit
    global compLimit
    global counter
    global goNextRound

    if playerCardSelected.isCoreCard:
        counter.coreCardCounter += 1

    if playerCardSelected.firstAction==1 and compCardSelected.firstAction==3:
            compHealth-=1
    elif playerCardSelected.firstAction==3 and compCardSelected.firstAction==1:
        playerHealth-=1
    elif playerCardSelected.firstAction==3 and compCardSelected.firstAction==2:
        if playerHealth<playerLimit:
            playerHealth+=1
    elif playerCardSelected.firstAction==2 and compCardSelected.firstAction==3:
        if compHealth<compLimit:
            compHealth+=1
    elif playerCardSelected.firstAction==1 and compCardSelected.firstAction==1:
        compHealth-=1
        playerHealth-=1
    elif playerCardSelected.firstAction==3 and compCardSelected.firstAction==3:
        if compHealth<compLimit:
            compHealth+=1
        if playerHealth<playerLimit:
            playerHealth+=1
    elif playerCardSelected.firstAction==5 and compCardSelected.firstAction==3:
        compHealth-=3
    elif compCardSelected.firstAction==5 and playerCardSelected.firstAction==3:
        playerHealth-=3
    elif playerCardSelected.firstAction==5 and compCardSelected.firstAction==1:
        playerHealth-=1
        compHealth-=2
    elif compCardSelected.firstAction==5 and playerCardSelected.firstAction==1:
        playerHealth-=2
        compHealth-=1
    elif playerCardSelected.firstAction==5 and compCardSelected.firstAction==5:
        playerHealth-=2
        compHealth-=2
    elif playerCardSelected.firstAction==6 and compCardSelected.firstAction==1:
        compHealth-=1
    elif compCardSelected.firstAction==6 and playerCardSelected.firstAction==1:
        playerHealth-=1
    elif playerCardSelected.firstAction==6 and compCardSelected.firstAction==6:
        playerHealth-=1
        compHealth-=1
    elif playerCardSelected.firstAction==7 and compCardSelected.firstAction==2:
        playerHealth-=3
    elif playerCardSelected.firstAction==7 and compCardSelected.firstAction==3:
        compHealth-=4
    elif playerCardSelected.firstAction==7 and compCardSelected.firstAction==1:
        compHealth-=4
        playerHealth-=1
    elif compCardSelected.firstAction==7 and playerCardSelected.firstAction==1:
        playerHealth-=4
        compHealth-=1
    elif compCardSelected.firstAction==7 and playerCardSelected.firstAction==2:
        compHealth-=3
    elif compCardSelected.firstAction==7 and compCardSelected.firstAction==3:
        playerHealth-=4
    elif playerCardSelected.firstAction==7 and compCardSelected.firstAction==5:
        compHealth-=4
        playerHealth-=2
    elif compCardSelected.firstAction==7 and playerCardSelected.firstAction==5:
        playerHealth-=4
        compHealth-=2
    elif playerCardSelected.firstAction==7 and compCardSelected.firstAction==7:
        playerHealth-=4
        compHealth-=4
    elif playerCardSelected.firstAction==4 and compCardSelected.firstAction==3:
        playerLimit+=1
        if compHealth<compLimit:
            compHealth+=1
    elif playerCardSelected.firstAction==4 and compCardSelected.firstAction==4:
        playerLimit+=1
        #print(playerLimit)
        compLimit+=1
        #print(compLimit)
    elif playerCardSelected.firstAction==4 and compCardSelected.firstAction==2:
        playerLimit+=1
        #print(playerLimit)
    elif compCardSelected.firstAction==4 and playerCardSelected.firstAction==2:
        compLimit+=1
        #print(compLimit)
    elif compCardSelected.firstAction==4 and playerCardSelected.firstAction==3:
        compLimit+=1
        #print(compLimit)
        if playerpHealth<playerLimit:
            playerHealth+=1
    if playerCardSelected.secondAction==1 and compCardSelected.secondAction==0 or compCardSelected.secondAction==3 or compCardSelected.secondAction==1:
        compHealth-=1
    if compCardSelected.secondAction==3 and playerCardSelected.secondAction==0 or playerCardSelected.secondAction==2:
        if compHealth<compLimit:
            compHealth+=1
    if playerCardSelected.secondAction==3 and compCardSelected.secondAction==0 or compCardSelected.secondAction==2:
        if playerHealth<playerLimit:
            playerHealth+=1
    if playerCardSelected.secondAction==3 and compCardSelected.secondAction==3:
        if compHealth<compLimit:
            compHealth+=1
        if playerHealth<playerLimit:
            playerHealth+=1
    if compCardSelected.secondAction==1 and playerCardSelected.secondAction==0 or playerCardSelected.secondAction==3:
        playerHealth-=1
    if compCardSelected.secondAction==1 and playerCardSelected.secondAction==1:
        playerHealth-=1
        compHealth-=1
    if playerCardSelected.secondAction==2 and compCardSelected.firstAction==2:
        compHealth-=1
    if compCardSelected.secondAction==2 and playerCardSelected.firstAction==2 and playerCardSelected.secondAction==0 or playerCardSelected.secondAction==1 or playerCardSelected.secondAction==3:
        playerHealth-=1
    if playerCardSelected.secondAction==2 and compCardSelected.firstAction==2 and compCardSelected.secondAction==0 or compCardSelected.secondAction==1 or compCardSelected.secondAction==3:
        compHealth-=1
    goNextRound = True
    print("go next")
    #print("Player health: " + str(playerHealth))
    #print("Comp health: " + str(compHealth))

def displayLargeCard(cardName):
    global enlargedCard
    draw_group.remove(enlargedCard)
    if cardName == "Attack":
        enlargedCard = Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\attack2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Attack(Core)":
        enlargedCard = Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\coreA2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Block(Core)":
        enlargedCard = Card("Block(Core)", True, "Block an attack.", 2, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\coreB2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Heal(Core)":
        enlargedCard = Card("Attack(Core)", True, "Deal 1 basic attack damage.", 1, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\coreH2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Block":
        enlargedCard = Card("Block", True, "Block an attack.", 2, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\block2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Heal":
        enlargedCard = Card("Heal(Core)", True, "Recieve one Lifepoint.", 3, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\heal2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Double Attack":
        enlargedCard = Card("Double Attack", False, "1st Action: Attack " + " 2nd Action: Attack", 1, 1, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\dblatk2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Mighty Swing":
        enlargedCard = Card("Mighty Swing", False, "Make an Attack that deals 2 damage. However, if Hit against a Heal, deal 3 damage!", 5, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\mighty swing2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Strike & Heal":
        enlargedCard = Card("Strike & Heal", False, "1st Action: Attack " + " 2nd Action: Heal", 1, 3, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\strhl2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Double Block":
        enlargedCard = Card("Double Block", False, "1st Action: Block" + " 2nd Action: Block" + "Special: Shield Bash, if matcheed against a block, 2nd Action: Block and Attack.", 2, 2, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\dblblk2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Block & Strike":
        enlargedCard = Card("Block & Strike", False, "1st Action: Block " + " 2nd Action: Attack", 2, 1, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\blockstrike2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Super Heal":
        enlargedCard = Card("Super Heal", False, "Heal 2 Lifepoints as a single action. If matched against an Attack, then Super Heal is negated", 3, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\superhl2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Life Boost":
        enlargedCard = Card("Life Boost", False, "1st Action: Increase Max Life by 1 " + " 2nd Action: Heal" + "Gaining Max Life only increases Max Life potential, not a Lifepoint. Can be negated by Attack depending on 1st or 2nd Action.", 4, 3, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\life boost2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Overkill":
        enlargedCard = Card("Overkill", False, "Deal 4 damage. However, if matched against a Block, take 3 damage instead.", 7, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\overkill2.png")
        draw_group.add(enlargedCard)
    elif card.name == "Parry":
        enlargedCard = Card("Parry", False, "Deal 1 damage. However, if matched against an Attack, 1st Action: Block and Attack.", 6, 0, 7, 13)
        enlargedCard.image = pygame.image.load(r"images\parry2.png")
        draw_group.add(enlargedCard)

#health variables


#action boolean variables

createStarterDeck()
random.shuffle(playerDeck)
drawDeck()
draw_group.remove(comp_group)
turnCounter=1
drawCards()
allCardsToDeck()
displayHand()
while True and playerHealth>0 and compHealth>0:

    #check if new turn
    if turnCounter == 6:
        onlyCoreCards = False
        turnCounter=1
        counter.coreCardCounter = 0
        drawCards()
        #allCardsToDeck()
        displayHand()
        compCardSelected.rect.x=graveyardPos.x
        compCardSelected.rect.y=graveyardPos.y

    # checking core card restriction
    if turnCounter==3 and counter.coreCardCounter==0:
        onlyCoreCards = True
    elif turnCounter==4 and counter.coreCardCounter==1:
        onlyCoreCards = True
    elif turnCounter==5 and counter.coreCardCounter==2:
        onlyCoreCards = True

    # check mouse pos
    mousePosX, mousePosY = pygame.mouse.get_pos()
    # print(mousePos)
    for card in player_group:
        if card.rect.x <= mousePosX and mousePosX <= card.rect.x + 100 and card.rect.y <= mousePosY and mousePosY <= card.rect.y + 140:
            displayLargeCard(card.name)
    """
    for card in comp_group:
        if card.rect.x <= mousePosX and mousePosX <= card.rect.x + 100 and card.rect.y <= mousePosY and mousePosY <= card.rect.y + 140:
            displayLargeCard(card.name)
    """

    # check for events
    for event in pygame.event.get():
       if event.type == QUIT:
            pygame.quit()
            sys.exit()

       if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          #print(pos)
          #print("0TC: " + str(turnCounter))
          #print("0CCC: " + str(counter.coreCardCounter))
          if cardInPlay:
            playerCardSelected.rect.x=graveyardPos.x
            playerCardSelected.rect.y=graveyardPos.y
            compCardSelected.rect.x=graveyardPos.x
            compCardSelected.rect.y=graveyardPos.y
          # get a list of all sprites that are under the mouse cursor
          if goNextRound:
            #print("getting sprites")
            clicked_sprites = [s for s in player_group if s.rect.collidepoint(pos)]
          # do something with the clicked sprites...
          for sprite in clicked_sprites:

            x = getCardIndex(sprite)
            #print("index: " + str(x))
            playerCardSelected = playerHand[x]
            playerHand[x].cardPlayed = True
            if playerCardSelected.isCoreCard:
                print("got cCard")
            else:
                print("not cCard")

            if onlyCoreCards:
                if playerCardSelected.isCoreCard==True:
                    goNextRound = False
                    #for x in range(0, len(playerHand)):
                        #if playerCardSelected.isCoreCard==True:
                    playerCardSelected.rect.x=playerCardPos.x
                    playerCardSelected.rect.y=playerCardPos.y
                    draw_group.remove(playerCardSelected)
                    draw_group.add(playerCardSelected)
                    cardInPlay = True
                    CompChoosesCard()
                    loadCSImage(compCardSelected)
                    resolveRound()
                    turnCounter += 1

            elif onlyCoreCards == False:
                goNextRound = False
                playerCardSelected.rect.x=playerCardPos.x
                playerCardSelected.rect.y=playerCardPos.y
                draw_group.remove(playerCardSelected)
                draw_group.add(playerCardSelected)
                cardInPlay = True
                CompChoosesCard()
                loadCSImage(compCardSelected)
                resolveRound()
                turnCounter += 1

          print("TC: " + str(turnCounter))
          print("CCC: " + str(counter.coreCardCounter))


    main_clock.tick(100)


    screen.blit(background_image,(0,0))
    draw_group.clear(screen, background_image)
    draw_group.draw (screen)
    draw_text("Player Health: " + str(playerHealth), font, screen, 15,350)
    draw_text("Comp Health: " + str(compHealth), font, screen, 15,375)
    pygame.display.update()

time.sleep(2)
pygame.quit()
sys.exit()

