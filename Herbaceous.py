import random
import sys

# TODO: check the error UnboundLocalError: local variable 'additionalInput' referenced before assignment at L604


########################
##### 72 CARD DECK #####
########################
# Generate the whole 72 card decks to ensure more randomness and replayability
# Cards are defined as classes, each with a herb name, an ID for the set, and an overall ID to track
# TODO: try to replace the classes into a dictionary and remove the setID?


class Rosemary:
    def __init__(self, setid, overallid):
        self.herbName = "Rosemary"
        self.setID = setid
        self.overallID = overallid


class Saffron:
    def __init__(self, setid, overallid):
        self.herbName = "Saffron"
        self.setID = setid
        self.overallID = overallid


class Bay:
    def __init__(self, setid, overallid):
        self.herbName = "Bay"
        self.setID = setid
        self.overallID = overallid


class Lavender:
    def __init__(self, setid, overallid):
        self.herbName = "Lavender"
        self.setID = setid
        self.overallID = overallid


class Dill:
    def __init__(self, setid, overallid):
        self.herbName = "Dill"
        self.setID = setid
        self.overallID = overallid


class Sage:
    def __init__(self, setid, overallid):
        self.herbName = "Sage"
        self.setID = setid
        self.overallID = overallid


class Tarragon:
    def __init__(self, setid, overallid):
        self.herbName = "Tarragon"
        self.setID = setid
        self.overallID = overallid


class Chive:
    def __init__(self, setid, overallid):
        self.herbName = "Chive"
        self.setID = setid
        self.overallID = overallid


class Mint:
    def __init__(self, setid, overallid):
        self.herbName = "Mint"
        self.setID = setid
        self.overallID = overallid


class Thyme:
    def __init__(self, setid, overallid):
        self.herbName = "Thyme"
        self.setID = setid
        self.overallID = overallid

# Generate the cards from each herb class, assigning them an overall ID
overallid = 1
completeDeck = list()

rosemarySet = list()
for i in range(9):
    rosemarySet.append(Rosemary(i, overallid))
    overallid += 1
completeDeck.append(rosemarySet)

saffronSet = list()
for i in range(9):
    saffronSet.append(Saffron(i, overallid))
    overallid += 1
completeDeck.append(saffronSet)

baySet = list()
for i in range(9):
    baySet.append(Bay(i, overallid))
    overallid += 1
completeDeck.append(baySet)

lavenderSet = list()
for i in range(9):
    lavenderSet.append(Lavender(i, overallid))
    overallid += 1
completeDeck.append(lavenderSet)

dillSet = list()
for i in range(9):
    dillSet.append(Dill(i, overallid))
    overallid += 1
completeDeck.append(dillSet)

sageSet = list()
for i in range(9):
    sageSet.append(Sage(i, overallid))
    overallid += 1
completeDeck.append(sageSet)

tarragonSet = list()
for i in range(9):
    tarragonSet.append(Tarragon(i, overallid))
    overallid += 1
completeDeck.append(tarragonSet)

chiveSet = list()
for i in range(3):
    chiveSet.append(Chive(i, overallid))
    overallid += 1
completeDeck.append(chiveSet)

mintSet = list()
for i in range(3):
    mintSet.append(Mint(i, overallid))
    overallid += 1
completeDeck.append(mintSet)

thymeSet = list()
for i in range(3):
    thymeSet.append(Thyme(i, overallid))
    overallid += 1
completeDeck.append(thymeSet)

# combine the herb classes together into a complete deck
orderedDeck = list()
for i in range(len(completeDeck)):
    for j in range(len(completeDeck[i])):
        orderedDeck.append(completeDeck[i][j])


#########################
###### 4 CONTAINERS #####
#########################
# Create the four containers in which the herbs may be potted: large pot, wooden planter, small pots, and glass jar
# Make a class that includes all the herbs that will be potted. These are added from the community garden and the private garden
# They are actually functions which cannot be re-selected. They all take in the same class of herbsToPot. 
# Whenever a container is selected to be potted, the points are added to the global points tracker

class herbsToPot:
    def __init__(self):
        self.cardList = []
        self.numberOfCards = 0

herbsToPot = herbsToPot()

def selectToPot(card):
    herbsToPot.cardList.append(card)
    herbsToPot.numberOfCards += 1


def allSame(items):
    return all(x.herbName == items[0].herbName for x in items)

def potInLargePot(herbs):
    # print(herbs.cardList)
    global totalPoints

    if herbs.numberOfCards == 1:
        totalPoints += 2
        return()
    if allSame(herbs.cardList) == False:
        return()
    else:
        if herbs.numberOfCards == 2:
            totalPoints += 6

        if herbs.numberOfCards == 3:
            totalPoints += 10

        if herbs.numberOfCards == 4:
            totalPoints += 14

        if herbs.numberOfCards == 5:
            totalPoints += 18

        if herbs.numberOfCards == 6:
            totalPoints += 20

        if herbs.numberOfCards == 7:
            totalPoints += 22
        return()


def potInWoodenPlanter(herbs):
    herbNameList = [x.herbName for x in herbs.cardList]
    uniqueSet = set(herbNameList)

    global totalPoints

    if len(uniqueSet) == 2:
        totalPoints += 3

    if len(uniqueSet) == 3:
        totalPoints += 4

    if len(uniqueSet) == 4:
        totalPoints += 6

    if len(uniqueSet) == 5:
        totalPoints += 8

    if len(uniqueSet) == 6:
        totalPoints += 12

    if len(uniqueSet) == 7:
        totalPoints += 14

    return()


def potInSmallPots(herbs):

    global totalPoints

    herbNameList = sorted([x.herbName for x in herbs.cardList])
    tempSet = []
    doubles = []
    for herb in herbNameList:
        if herb in tempSet:
            doubles.append(herb)
            tempSet.remove(herb)
        else:
            tempSet.append(herb)
    doubles = set(doubles)

    if len(doubles) == 1:
        totalPoints += 4

    if len(doubles) == 2:
        totalPoints += 8

    if len(doubles) == 3:
        totalPoints += 12

    if len(doubles) == 4:
        totalPoints += 14

    if len(doubles) == 5:
        totalPoints += 16

    if len(doubles) == 6:
        totalPoints += 18

    return()

def potInGlassJar(herbs):

    global totalPoints

    if len(herbs.cardList) > 3:
        return()

    if len(herbs.cardList) == 1:
        totalPoints += 2

    if len(herbs.cardList) == 2:
        totalPoints += 4

    if len(herbs.cardList) == 3:
        totalPoints += 6

    specHerb = ["mint", "chive", "thyme"]
    herbNameList = sorted([x.herbName for x in herbs.cardList])
    presentSpecHerb = [herb for herb in herbNameList if herb in specHerb]

    for i in presentSpecHerb:
        if i == "mint":
            totalPoints += 1
        elif i == "chive":
            totalPoints += 2
        elif i == "thyme":
            totalPoints += 3

    if len(presentSpecHerb) == 3:
        totalPoints += 5

    return()

# selecting the appropriate container to pot herbs in
availableContainers = {1: "Large Pot", 2: "Wooden Planter", 3: "Small Pots", 4: "Glass Jar"}

def selectAppropriatePot(currentHerb, currentHerbList):

    global totalPoints

    print("Current herbs to pot: ", ", ".join(showHerbsToPot(currentHerbList)))

    global availableContainers

    print("Available containers:", availableContainers,"\n")
    while True:
        try:
            n = int(input('Which container would you like to pot the herbs in?\n'
                          ' 1: Large Pot (All identical herbs)\n 2: Wooden Planter (All different herbs)\n'
                          ' 3: Small Pots (Different pairs of identical herbs)\n'
                          ' 4: Glass Jar (Any 1 - 3 herbs, bonus from special herbs)\n'
                          ' 0: To stop potting in containers\n'))
            if n == 0:
                print("Stop potting in containers\n")
                break
            del availableContainers[n]

        except KeyError:
            print("Pot already full. Pick another pot\n")
            print("Available containers:", availableContainers, "\n")
            continue

        if n == 1:
            potInLargePot(currentHerb)
            print("Current point total: ", totalPoints)

            break

        if n == 2:
            potInWoodenPlanter(currentHerb)
            print("Current point total: ", totalPoints)

            break

        if n == 3:
            potInSmallPots(currentHerb)
            print("Current point total: ", totalPoints)

            break

        if n == 4:
            potInGlassJar(currentHerb)
            print("Current point total: ", totalPoints)
            break


#######################
#### CARD ACTIONS #####
#######################
# Important card actions functions needed to play
# Identify a card ID which is used when drawing a card, and the draw card which returns which card has been drawn from the deck
# Create a playdeck of 36 cards from the complete deck. 

def identifyCard(cardID):
    for setCount in range(len(completeDeck)):
        for herbCount in range(len(completeDeck[setCount])):
            if completeDeck[setCount][herbCount].overallID == cardID:
                return completeDeck[setCount][herbCount]



def deckSetup():
    playDeck = random.sample(orderedDeck, 36)
    return playDeck

playDeck = deckSetup()

allOverallID = [o.overallID for o in playDeck]

def drawCard(cardID):
    drawnCard = identifyCard(cardID)
    allOverallID.remove(cardID)
    return(drawnCard)


###################
##### GARDENS #####
###################
# 3 gardens are generated to track the cards in play: discard pile, community garden, and private garden
# The discard pile requires 2 functions: the discard card during play, and the discard set from the community garden 
# The community garden holds at most 4 herbs, and has a function to remove a herb when it is potted, and add a card when drawn
# The private garden holds as many cards as needed, and has the same functions as the community garden

class discardGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []

def discardCard(card):
    discardGarden.cardList.append(card)
    discardGarden.numberOfCards += 1
    return discardGarden


def discardSetCards(set):
    discardGarden.cardList.append(set)
    numCardsDiscarded = len(set)
    discardGarden.numberOfCards += numCardsDiscarded


discardGarden = discardGarden()


class communityGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []


communityGarden = communityGarden()


def plant2CommunityGarden(card):
    communityGarden.numberOfCards += 1
    if communityGarden.numberOfCards == 5:
        communityGarden.cardList.append(card)
        discardSetCards(communityGarden.cardList)
        print("More than 4 cards, discard community garden.")
        communityGarden.cardList = []
        communityGarden.numberOfCards = 0
    else:
        communityGarden.cardList.append(card)

def removeFromCommunityGarden(card):
    communityGarden.numberOfCards -= 1
    communityGarden.cardList.remove(card)

class privateGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []

privateGarden = privateGarden()

def plant2PrivateGarden(card):
    privateGarden.numberOfCards += 1
    privateGarden.cardList.append(card)

def removeFromPrivateGarden(card):
    privateGarden.numberOfCards -= 1
    privateGarden.cardList.remove(card)

######################
##### SETUP GAME #####
######################
# Set the total points to 0
# Distribute the appropriate cards to each pile

totalPoints = 0


def setupGame():
    discardCard(drawCard(random.choice(allOverallID)))

    for i in range(2):
        plant2CommunityGarden(drawCard(random.choice(allOverallID)))

    for i in range(3):
        plant2PrivateGarden(drawCard(random.choice(allOverallID)))


setupGame()

############################################
##### IMPORTANT FUNCTIONS FOR GAMEPLAY #####
############################################
# getInput is used to select which herb to pot from each respective garden
# 2 functions to show the status of the two gardens throughout the game
# 1 function to show which herbs are ready to be potted. 
# TODO: a function to return each herb to its respective pile in case there is a mistake?

userInput = None

def getInput(length):
    while True:
        try:
            num = int(input('Select which herb to pot: \nEnter 0 to stop potting herbs\n'))
        except ValueError:
            print("Not a valid input. Enter an appropriate integer.\n")
            continue
        return num


def showPrivateGardenStatus(currentHerbsPresent):
    garden = sorted([o.herbName for o in currentHerbsPresent])
    return(garden)


def showCommunityGardenStatus(currentHerbsPresent):
    garden = sorted([o.herbName for o in currentHerbsPresent])
    return(garden)

def showHerbsToPot(currentHerbsPresent):
    garden = sorted([o.herbName for o in currentHerbsPresent])
    return(garden)

##########################
##### POTTING ACTION #####    
##########################
# 2 functions to describe the potting actions from either a private garden or a community garden
# Function to ask which garden to select herbs to pot

def potFromPrivateGarden():

    userInput = None

    while userInput != 0:
        print("Current herbs in private garden: ",", ".join(showPrivateGardenStatus(privateGarden.cardList)))

        print("Current herbs ready to pot: ",", ".join(showHerbsToPot(herbsToPot.cardList)),"\n")

        privateGarden.cardList.sort(key=lambda x: x.herbName)

        userInput = getInput(privateGarden.numberOfCards)

        if userInput == 0:
            print("Not potting herbs")
            break

        potInputIndexInPrivate = userInput - 1
        try:
            privateGarden.cardList[potInputIndexInPrivate]
        except IndexError:
            print("not a valid option")
            continue
        else:
            selectedHerb = privateGarden.cardList[potInputIndexInPrivate]

        selectToPot(selectedHerb)
        removeFromPrivateGarden(selectedHerb)

        if privateGarden.numberOfCards == 0:
            print("nothing else to pot from private garden \n")
            break

def potFromCommunityGarden():

    userInput = None

    while userInput != 0:

        print("Current herbs in community garden: ",", ".join(showCommunityGardenStatus(communityGarden.cardList)))

        print("Current herbs ready to pot: ",", ".join(showHerbsToPot(herbsToPot.cardList)),"\n")

        communityGarden.cardList.sort(key=lambda x: x.herbName)

        userInput = getInput(communityGarden.numberOfCards)

        if userInput == 0:
            print("Not potting herbs")
            break

        potInputIndexInCommunity= userInput - 1
        try:
            communityGarden.cardList[potInputIndexInCommunity]
        except IndexError:
            print("not a valid option")
            continue
        else:
            selectedHerb = communityGarden.cardList[potInputIndexInCommunity]

        selectToPot(selectedHerb)
        removeFromCommunityGarden(selectedHerb)

        if communityGarden.numberOfCards == 0:
            print("nothing else to pot from community garden \n")
            break


def potOption():

    potInput = None
    additionalInput = None


    while potInput != 0:

        checkEndGame()

        print(" 0: Don't pot anything\n 1: Pot from private garden\n 2: Pot from community garden")
        potInput = int(input('Select which option: \n'))

        if potInput == 0:
            print("Not potting, proceed to draw card\n")
            break

        if potInput == 1:
            print("Potting from private garden\n")
            potFromPrivateGarden()

            print("\nCurrent herbs ready to pot: ", ", ".join(showHerbsToPot(herbsToPot.cardList)), "\n")
            print("Current herbs in community garden: ", ", ".join(showCommunityGardenStatus(communityGarden.cardList)))

            try:
                additionalInput = int(input('Add more herbs from community garden?\n 0: No\n 1: Yes\n'))
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue

            if additionalInput == 1:
                potFromCommunityGarden()
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

            if additionalInput == 0:
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

            else:
                #selectAppropriatePot(herbsToPot, herbsToPot.cardList)
                continue

        if potInput == 2:
            print("Potting from community garden\n")
            potFromCommunityGarden()

            print("\nCurrent herbs ready to pot: ", ", ".join(showHerbsToPot(herbsToPot.cardList)), "\n")
            print("Current herbs in private garden: ", ", ".join(showPrivateGardenStatus(privateGarden.cardList)))

            try:
                additionalInput = int(input('Add more herbs from private garden?\n 0: No\n 1: Yes\n'))

            except ValueError or UnboundLocalError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue
            if additionalInput == 1:
                print("Potting from private garden\n")
                potFromPrivateGarden()
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

            if additionalInput == 0:
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)


            else:
                #selectAppropriatePot(herbsToPot, herbsToPot.cardList)
                continue

        else:
            continue

def finalPot():
    potInput = None

    while potInput != 0:

        print(" 0: End game\n 1: Pot from private garden\n 2: Pot from community garden")
        potInput = int(input('Select which option: \n'))

        if potInput == 0:
            break

        if potInput == 1:
            print("Potting from private garden\n")
            potFromPrivateGarden()

            print("\nCurrent herbs ready to pot: ", ", ".join(showHerbsToPot(herbsToPot.cardList)), "\n")
            print("Current herbs in community garden: ", ", ".join(showCommunityGardenStatus(communityGarden.cardList)))
            try:
                additionalInput = int(input('Add more herbs from community garden?\n 0: No\n 1: Yes\n'))
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")

            if additionalInput == 1:
                print("Potting from community garden\n")
                potFromCommunityGarden()
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

            else:
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

        if potInput == 2:
            print("Potting from community garden\n")
            potFromCommunityGarden()

            print("\nCurrent herbs ready to pot: ", ", ".join(showHerbsToPot(herbsToPot.cardList)), "\n")
            print("Current herbs in private garden: ", ", ".join(showPrivateGardenStatus(privateGarden.cardList)))

            try:
                additionalInput = int(input('Add more herbs from private garden?\n 0: No\n 1: Yes\n'))
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue
            if additionalInput == 1:
                print("Potting from private garden\n")
                potFromPrivateGarden()
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

            else:
                selectAppropriatePot(herbsToPot, herbsToPot.cardList)

        else:
            continue

def ranking():
    global totalPoints

    if totalPoints < 37:
        print("You are a Fledgling Grower")

    if totalPoints >=37 and totalPoints <=41:
        print("You are a Beginning Planter")

    if totalPoints >=42 and totalPoints <=46:
        print("You are a Clever Cultivator")

    if totalPoints >=47 and totalPoints <=51:
        print("You are a Talented Gardener")

    if totalPoints >=52 and totalPoints <=56:
        print("You are a PRofessional Herbalist")

    if totalPoints > 56:
        print("You are a True Green Thumb Harvester")

####################
##### GAMEPLAY #####
####################
# The gameplay loops continually until the generated play deck is empty, or there are no more containers to be potted
# 1. An option first asks if the player wants to pot any current herbs, if yes, then pot the appropriate herbs, if not move on
# 2. A card is drawn and 3 options are given: discard, plant in community garden, or plant in private garden. 
# Each place can only be chosen once during the plant step before you can pot again
# 3. This is repeated until the deck runs out or there are no available containers anymore

def checkEndGame():
    if not availableContainers:
        print("No more containers available. Game finished!")
        print("Final point total: ", totalPoints)
        ranking()
        sys.exit()

    if not allOverallID:
        print("Deck is empty. Game finished! Pot one last time:")
        finalPot()
        print("Final point total: ", totalPoints)
        ranking()
        sys.exit()

while len(playDeck) != 0:

    print("Current point total: ", totalPoints)
    print("Herbs in community garden: ", ", ".join(showCommunityGardenStatus(communityGarden.cardList)))
    print("Herbs in private garden: ", ", ".join(showPrivateGardenStatus(privateGarden.cardList)), "\n")


    potOption()

    choices = {1: 'Discard pile', 2: 'Community Garden', 3: 'Private Garden'}
    while True:
        #checkEndGame()
        drawnCard = drawCard(random.choice(allOverallID))
        print("Drawn card: ", drawnCard.herbName.upper(), "\n")
        print("Herbs in community garden: ", ", ".join(showCommunityGardenStatus(communityGarden.cardList)))
        print("Herbs in private garden: ", ", ".join(showPrivateGardenStatus(privateGarden.cardList)),"\n")

        while True:

            try:
                print("Remaining places: ", choices)
                n = int(input('Select where to place card: \n 1: Discard pile\n 2: Community garden\n 3: Private garden\n'))
                del choices[n]

            except KeyError:
                print("Place already selected previously. Pick another place\n")
                continue
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue

            if n == 1:
                discardCard(drawnCard)
                break

            if n == 2:
                plant2CommunityGarden(drawnCard)
                break

            if n == 3:
                plant2PrivateGarden(drawnCard)
                break

        if not choices:
            break
