import random


##### 72 CARDS ######


class Rosemary:
    def __init__(self, setid, overallid):
        self.herbName = "rosemary"
        self.setID = setid
        self.overallID = overallid


class Saffron:
    def __init__(self, setid, overallid):
        self.herbName = "saffron"
        self.setID = setid
        self.overallID = overallid


class Bay:
    def __init__(self, setid, overallid):
        self.herbName = "bay"
        self.setID = setid
        self.overallID = overallid


class Lavender:
    def __init__(self, setid, overallid):
        self.herbName = "lavender"
        self.setID = setid
        self.overallID = overallid


class Dill:
    def __init__(self, setid, overallid):
        self.herbName = "dill"
        self.setID = setid
        self.overallID = overallid


class Sage:
    def __init__(self, setid, overallid):
        self.herbName = "sage"
        self.setID = setid
        self.overallID = overallid


class Tarragon:
    def __init__(self, setid, overallid):
        self.herbName = "tarragon"
        self.setID = setid
        self.overallID = overallid


class Chive:
    def __init__(self, setid, overallid):
        self.herbName = "chive"
        self.setID = setid
        self.overallID = overallid
        self.pointValue = 2


class Mint:
    def __init__(self, setid, overallid):
        self.herbName = "mint"
        self.setID = setid
        self.overallID = overallid
        self.pointValue = 1


class Thyme:
    def __init__(self, setid, overallid):
        self.herbName = "thyme"
        self.setID = setid
        self.overallID = overallid
        self.pointValue = 3


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

# ordered deck completed
orderedDeck = list()
for i in range(len(completeDeck)):
    for j in range(len(completeDeck[i])):
        orderedDeck.append(completeDeck[i][j])



###### CONTAINERS #####






#### CARD ACTIONS #####

def identifyCard(cardID):
    for setCount in range(len(completeDeck)):
        for herbCount in range(len(completeDeck[setCount])):
            if completeDeck[setCount][herbCount].overallID == cardID:
                return completeDeck[setCount][herbCount]



def deckSetup():
    playDeck = random.sample(orderedDeck, 36)
    return playDeck
    # print(playDeck[1].__dict__)
    # print(playDeck[1].overallID)


playDeck = deckSetup()
# print(playDeck[1].__dict__)

allOverallID = [o.overallID for o in playDeck]
# print(allOverallID)
# print(len(allOverallID))

def drawCard(cardID):
    drawnCard = identifyCard(cardID)
    # print(drawnCard.__dict__)
    allOverallID.remove(cardID)
    return(drawnCard)


##### GARDENS ########


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
    return discardGarden


discardGarden = discardGarden()
# discardCard(playDeck[1])
# print(discardGarden.cardList[0].__dict__)

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
        communityGarden.cardList = []
        communityGarden.numberOfCards = 0
    else:
        communityGarden.cardList.append(card)

# print(communityGarden.cardList[0].__dict__)

# print(discardGarden.__dict__)


class privateGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []

privateGarden = privateGarden()

def plant2PrivateGarden(card):
    privateGarden.numberOfCards += 1
    privateGarden.cardList.append(card)


##### SETUP #####

def setupGame():
    discardCard(drawCard(random.choice(allOverallID)))

    for i in range(2):
        plant2CommunityGarden(drawCard(random.choice(allOverallID)))

    for i in range(3):
        plant2PrivateGarden(drawCard(random.choice(allOverallID)))

setupGame()
# print(discardGarden.__dict__)
# print(communityGarden.__dict__)
# print(privateGarden.__dict__)

#### GAMEPLAY #####

# while deck !empty or can't pot anymore


choices = [1,2,3]
for i in range(len(choices)):

    drawnCard = drawCard(random.choice(allOverallID))
    print(drawnCard.__dict__)

    # n = int(input('Enter destination for plant: \n'))
    # 1 = Discard Pile
    # 2 = Community Garden
    # 3 = Private Garden

    n = random.choice(choices)
    choices.remove(n)

    if(n == 1):
        discardCard(drawnCard)

    if(n == 2):
        plant2CommunityGarden(drawnCard)

    if(n == 3):
        plant2PrivateGarden(drawnCard)

print(len(allOverallID))
print(privateGarden.__dict__)
print(discardGarden.__dict__)