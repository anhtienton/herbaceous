import random
import sys

################
# 72 CARD DECK #
################
# Generate the whole 72 card decks to ensure more randomness and replayability
# Cards are defined as classes, each with a herb name, an ID for the set, and an overall ID to track
# TODO: try to replace the classes into a dictionary and remove the setID?


class Rosemary:
    def __init__(self, setid, overid):
        self.herbName = "Rosemary"
        self.setID = setid
        self.overallID = overid


class Saffron:
    def __init__(self, setid, overid):
        self.herbName = "Saffron"
        self.setID = setid
        self.overallID = overid


class Bay:
    def __init__(self, setid, overid):
        self.herbName = "Bay"
        self.setID = setid
        self.overallID = overid


class Lavender:
    def __init__(self, setid, overid):
        self.herbName = "Lavender"
        self.setID = setid
        self.overallID = overid


class Dill:
    def __init__(self, setid, overid):
        self.herbName = "Dill"
        self.setID = setid
        self.overallID = overid


class Sage:
    def __init__(self, setid, overid):
        self.herbName = "Sage"
        self.setID = setid
        self.overallID = overid


class Tarragon:
    def __init__(self, setid, overid):
        self.herbName = "Tarragon"
        self.setID = setid
        self.overallID = overid


class Chive:
    def __init__(self, setid, overid):
        self.herbName = "Chive"
        self.setID = setid
        self.overallID = overid


class Mint:
    def __init__(self, setid, overid):
        self.herbName = "Mint"
        self.setID = setid
        self.overallID = overid


class Thyme:
    def __init__(self, setid, overid):
        self.herbName = "Thyme"
        self.setID = setid
        self.overallID = overid


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


################
# 4 CONTAINERS #
################
# Create the four containers in which the herbs may be potted: large pot, wooden planter, small pots, and glass jar
# Make a class that includes all the herbs that will be potted. 
# These are added from the community garden and the private garden
# They are actually functions which cannot be re-selected. They all take in the same class of herbsToPot. 
# Whenever a container is selected to be potted, the points are added to the global points tracker

class HerbsToPot:
    def __init__(self):
        self.cardList = []
        self.numberOfCards = 0


# Initiate herbsToPot class that holds all herbs
herbsToPot = HerbsToPot()


def clear_potted_herbs(herbs):
    del herbs.cardList[:]


def select_to_pot(card):
    herbsToPot.cardList.append(card)
    herbsToPot.numberOfCards += 1


def all_same(items):
    return all(x.herbName == items[0].herbName for x in items)


def pot_in_large_pot(herbs):
    # print(herbs.cardList)
    global totalPoints

    if herbs.numberOfCards == 1:
        totalPoints += 2
        return()
    if not all_same(herbs.cardList):
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
        clear_potted_herbs(herbs)
        return()


def pot_in_wooden_planter(herbs):
    herbname_list = [x.herbName for x in herbs.cardList]
    unique_set = set(herbname_list)

    global totalPoints

    if len(unique_set) == 2:
        totalPoints += 3

    if len(unique_set) == 3:
        totalPoints += 4

    if len(unique_set) == 4:
        totalPoints += 6

    if len(unique_set) == 5:
        totalPoints += 8

    if len(unique_set) == 6:
        totalPoints += 12

    if len(unique_set) == 7:
        totalPoints += 14
    clear_potted_herbs(herbs)
    return()


def pot_in_small_pots(herbs):

    global totalPoints

    herbname_list = sorted([x.herbName for x in herbs.cardList])
    temp_set = []
    doubles = []
    for herb in herbname_list:
        if herb in temp_set:
            doubles.append(herb)
            temp_set.remove(herb)
        else:
            temp_set.append(herb)
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

    clear_potted_herbs(herbs)

    return()


def pot_in_glass_jar(herbs):

    global totalPoints

    if len(herbs.cardList) > 3:
        return()

    if len(herbs.cardList) == 1:
        totalPoints += 2

    if len(herbs.cardList) == 2:
        totalPoints += 4

    if len(herbs.cardList) == 3:
        totalPoints += 6

    special_herb = ["chive", "mint", "thyme"]
    herbname_list = sorted([x.herbName for x in herbs.cardList])
    present_special_herb = [herb for herb in herbname_list if herb in special_herb]

    for present_herb in present_special_herb:
        if present_herb == "mint":
            totalPoints += 1
            present_special_herb.remove("mint")
        elif present_herb == "chive":
            totalPoints += 2
            present_special_herb.remove("chive")
        elif present_herb == "thyme":
            totalPoints += 3
            present_special_herb.remove("thyme")

    if not present_special_herb:
        totalPoints += 5

    clear_potted_herbs(herbs)
    return()


# selecting the appropriate container to pot herbs in
availableContainers = {1: "Large Pot", 2: "Wooden Planter", 3: "Small Pots", 4: "Glass Jar"}


def select_appropriate_pot(current_herb, current_herb_list):

    global totalPoints

    print("Current herbs to pot: ", ", ".join(show_herbs_to_pot(current_herb_list)))

    global availableContainers

    print("Available containers:", availableContainers,"\n")
    while True:
        try:
            pot_input = int(input('Which container would you like to pot the herbs in?\n'
                          ' 1: Large Pot (All identical herbs)\n 2: Wooden Planter (All different herbs)\n'
                          ' 3: Small Pots (Different pairs of identical herbs)\n'
                          ' 4: Glass Jar (Any 1 - 3 herbs, bonus from special herbs)\n'
                          ' 0: To stop potting in containers\n'))
            if pot_input == 0:
                print("Stop potting in containers\n")
                break
            del availableContainers[pot_input]

        except ValueError:
            print("Not a valid input. Enter an appropriate integer.\n")
            continue

        except KeyError:
            print("Pot already full. Pick another pot\n")
            print("Available containers:", availableContainers, "\n")
            continue

        if pot_input == 1:
            pot_in_large_pot(current_herb)
            print("Current point total: ", totalPoints)

            break

        if pot_input == 2:
            pot_in_wooden_planter(current_herb)
            print("Current point total: ", totalPoints)

            break

        if pot_input == 3:
            pot_in_small_pots(current_herb)
            print("Current point total: ", totalPoints)

            break

        if pot_input == 4:
            pot_in_glass_jar(current_herb)
            print("Current point total: ", totalPoints)
            break


################
# CARD ACTIONS #
################
# Important card actions functions needed to play
# Identify a card ID which is used when drawing a card, 
# The draw card  returns which card has been drawn from the deck
# Create a playdeck of 36 cards from the complete deck. 

def identify_card(card_id):
    for setCount in range(len(completeDeck)):
        for herbCount in range(len(completeDeck[setCount])):
            if completeDeck[setCount][herbCount].overallID == card_id:
                return completeDeck[setCount][herbCount]


def deck_setup():
    current_deck_setup = random.sample(orderedDeck, 36)
    return current_deck_setup


play_deck = deck_setup()

allOverallID = [o.overallID for o in play_deck]


def draw_card(card_id):
    current_drawn_card = identify_card(card_id)
    allOverallID.remove(card_id)
    return current_drawn_card


###########
# GARDENS #
###########
# 3 gardens are generated to track the cards in play: discard pile, community garden, and private garden
# The discard pile requires 2 functions: the discard card during play, and the discard set from the community garden 
# The community garden holds at most 4 herbs, 
# and has a function to remove a herb when it is potted, and add a card when drawn
# The private garden holds as many cards as needed, and has the same functions as the community garden

class DiscardGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []


def discard_card(card):
    DiscardGarden.cardList.append(card)
    DiscardGarden.numberOfCards += 1
    return DiscardGarden


def discard_set_cards(current_set):
    DiscardGarden.cardList.append(current_set)
    num_cards_discarded = len(current_set)
    DiscardGarden.numberOfCards += num_cards_discarded


DiscardGarden = DiscardGarden()


class CommunityGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []


CommunityGarden = CommunityGarden()


def plant_2_community_garden(card):
    CommunityGarden.numberOfCards += 1
    if CommunityGarden.numberOfCards == 5:
        CommunityGarden.cardList.append(card)
        discard_set_cards(CommunityGarden.cardList)
        print("More than 4 cards, discard community garden.")
        CommunityGarden.cardList = []
        CommunityGarden.numberOfCards = 0
    else:
        CommunityGarden.cardList.append(card)


def remove_from_community_garden(card):
    CommunityGarden.numberOfCards -= 1
    CommunityGarden.cardList.remove(card)


class PrivateGarden:
    def __init__(self):
        self.numberOfCards = 0
        self.cardList = []


PrivateGarden = PrivateGarden()


def plant_2_private_garden(card):
    PrivateGarden.numberOfCards += 1
    PrivateGarden.cardList.append(card)


def remove_from_private_garden(card):
    PrivateGarden.numberOfCards -= 1
    PrivateGarden.cardList.remove(card)


##############
# SETUP GAME #
##############
# Set the total points to 0
# Distribute the appropriate cards to each pile

totalPoints = 0


def setup_game():
    discard_card(draw_card(random.choice(allOverallID)))

    for count in range(2):
        plant_2_community_garden(draw_card(random.choice(allOverallID)))

    for count in range(3):
        plant_2_private_garden(draw_card(random.choice(allOverallID)))


setup_game()

####################################
# IMPORTANT FUNCTIONS FOR GAMEPLAY #
####################################
# get_input is used to select which herb to pot from each respective garden
# 2 functions to show the status of the two gardens throughout the game
# 1 function to show which herbs are ready to be potted. 
# TODO: a function to return each herb to its respective pile in case there is a mistake?

userInput = None


def get_input():
    while True:
        try:
            num = int(input('Select which herb to pot: \nEnter 0 to stop potting herbs\n'))
        except ValueError:
            print("Not a valid input. Enter an appropriate integer.\n")
            continue
        return num


def show_private_garden_status(current_herbs_present):
    garden = sorted([o.herbName for o in current_herbs_present])
    return garden


def show_community_garden_status(current_herbs_present):
    garden = sorted([o.herbName for o in current_herbs_present])
    return garden


def show_herbs_to_pot(current_herbs_present):
    garden = sorted([o.herbName for o in current_herbs_present])
    return garden


##################
# POTTING ACTION #   
##################
# 2 functions to describe the potting actions from either a private garden or a community garden
# Function to ask which garden to select herbs to pot

def pot_from_private_garden():

    user_input = None

    while user_input != 0:
        print("Current herbs in private garden: ", ", ".join(show_private_garden_status(PrivateGarden.cardList)))

        print("Current herbs ready to pot: ", ", ".join(show_herbs_to_pot(herbsToPot.cardList)), "\n")

        PrivateGarden.cardList.sort(key=lambda x: x.herbName)

        user_input = get_input()

        if user_input == 0:
            print("Not potting herbs")
            break

        pot_input_index_in_private = user_input - 1
        try:
            PrivateGarden.cardList[pot_input_index_in_private]
        except IndexError:
            print("not a valid option")
            continue
        else:
            selected_herb = PrivateGarden.cardList[pot_input_index_in_private]

        select_to_pot(selected_herb)
        remove_from_private_garden(selected_herb)

        if PrivateGarden.numberOfCards == 0:
            print("nothing else to pot from private garden \n")
            break


def pot_from_community_garden():

    user_input = None

    while user_input != 0:

        print("Current herbs in community garden: ", ", ".join(show_community_garden_status(CommunityGarden.cardList)))

        print("Current herbs ready to pot: ", ", ".join(show_herbs_to_pot(herbsToPot.cardList)), "\n")

        CommunityGarden.cardList.sort(key=lambda x: x.herbName)

        user_input = get_input()

        if user_input == 0:
            print("Not potting herbs")
            break

        pot_input_index_in_community = user_input - 1
        try:
            CommunityGarden.cardList[pot_input_index_in_community]
        except IndexError:
            print("not a valid option")
            continue
        else:
            selected_herb = CommunityGarden.cardList[pot_input_index_in_community]

        select_to_pot(selected_herb)
        remove_from_community_garden(selected_herb)

        if CommunityGarden.numberOfCards == 0:
            print("nothing else to pot from community garden \n")
            break


def pot_option():

    pot_input = None

    while pot_input != 0:

        check_end_game()

        print(" 0: Don't pot anything\n 1: Pot from private garden\n 2: Pot from community garden")
        while True:
            try:
                pot_input = int(input('Select which option: \n'))
                #if pot_input != 0 or pot_input != 1 or pot_input != 2:
                #    print("Not a valid input. Enter an appropriate integer.\n")

            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue

            if pot_input == 0:
                print("Not potting, proceed to draw card\n")
                break

            if pot_input == 1:
                print("Potting from private garden\n")
                pot_from_private_garden()

                print("\nCurrent herbs ready to pot: ", ", ".join(show_herbs_to_pot(herbsToPot.cardList)), "\n")
                print("Current herbs in community garden: "
                      "", ", ".join(show_community_garden_status(CommunityGarden.cardList)))
                while True:
                    try:
                        additional_input = int(input('Add more herbs from community garden?\n 0: No\n 1: Yes\n'))
                        if additional_input != 0 or additional_input != 1:
                            print("Not a valid input. Enter an appropriate integer.\n")

                    except ValueError:
                        print("Not a valid input. Enter an appropriate integer.\n")
                        continue

                    if additional_input == 1:
                        pot_from_community_garden()
                        select_appropriate_pot(herbsToPot, herbsToPot.cardList)
                        break

                    if additional_input == 0:
                        select_appropriate_pot(herbsToPot, herbsToPot.cardList)
                        break
                break

            if pot_input == 2:
                print("Potting from community garden\n")
                pot_from_community_garden()

                print("\nCurrent herbs ready to pot: ", ", ".join(show_herbs_to_pot(herbsToPot.cardList)), "\n")
                print("Current herbs in private garden: "
                      "", ", ".join(show_private_garden_status(PrivateGarden.cardList)))

                while True:
                    try:
                        additional_input = int(input('Add more herbs from private garden?\n 0: No\n 1: Yes\n'))
                        if additional_input != 0 or additional_input != 1:
                            print("Not a valid input. Enter an appropriate integer.\n")

                    except ValueError or UnboundLocalError:
                        print("Not a valid input. Enter an appropriate integer.\n")
                        continue

                    if additional_input == 1:
                        print("Potting from private garden\n")
                        pot_from_private_garden()
                        select_appropriate_pot(herbsToPot, herbsToPot.cardList)
                        break

                    if additional_input == 0:
                        select_appropriate_pot(herbsToPot, herbsToPot.cardList)
                        break
                break

            else:
                print("Enter valid input")
                continue

def final_pot():
    pot_input = None
    additional_input = None
    while pot_input != 0:

        print(" 0: End game\n 1: Pot from private garden\n 2: Pot from community garden")
        pot_input = int(input('Select which option: \n'))

        if pot_input == 0:
            break

        if pot_input == 1:
            print("Potting from private garden\n")
            pot_from_private_garden()

            print("\nCurrent herbs ready to pot: ", ", ".join(show_herbs_to_pot(herbsToPot.cardList)), "\n")
            print("Current herbs in community garden: "
                  "", ", ".join(show_community_garden_status(CommunityGarden.cardList)))
            try:
                additional_input = int(input('Add more herbs from community garden?\n 0: No\n 1: Yes\n'))
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")

            if additional_input == 1:
                print("Potting from community garden\n")
                pot_from_community_garden()
                select_appropriate_pot(herbsToPot, herbsToPot.cardList)

            else:
                select_appropriate_pot(herbsToPot, herbsToPot.cardList)

        if pot_input == 2:
            print("Potting from community garden\n")
            pot_from_community_garden()

            print("\nCurrent herbs ready to pot: ", ", ".join(show_herbs_to_pot(herbsToPot.cardList)), "\n")
            print("Current herbs in private garden: ", ", ".join(show_private_garden_status(PrivateGarden.cardList)))

            try:
                additional_input = int(input('Add more herbs from private garden?\n 0: No\n 1: Yes\n'))
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue
            if additional_input == 1:
                print("Potting from private garden\n")
                pot_from_private_garden()
                select_appropriate_pot(herbsToPot, herbsToPot.cardList)

            else:
                select_appropriate_pot(herbsToPot, herbsToPot.cardList)

        else:
            continue


def ranking():
    global totalPoints

    if totalPoints < 37:
        print("You are a Fledgling Grower")

    if 37 <= totalPoints <= 41:
        print("You are a Beginning Planter")

    if 42 <= totalPoints <= 46:
        print("You are a Clever Cultivator")

    if 47 <= totalPoints <= 51:
        print("You are a Talented Gardener")

    if 52 <= totalPoints <= 56:
        print("You are a PRofessional Herbalist")

    if totalPoints > 56:
        print("You are a True Green Thumb Harvester")


############
# GAMEPLAY #
############
# The gameplay loops continually until the generated play deck is empty, or there are no more containers to be potted
# 1. An option first asks if the player wants to pot any current herbs, 
# if yes, then pot the appropriate herbs, if not move on
# 2. A card is drawn and 3 options are given: discard, plant in community garden, or plant in private garden. 
# Each place can only be chosen once during the plant step before you can pot again
# 3. This is repeated until the deck runs out or there are no available containers anymore

def check_end_game():
    if not availableContainers:
        print("No more containers available. Game finished!")
        print("Final point total: ", totalPoints)
        ranking()
        sys.exit()

    if not allOverallID:
        print("Deck is empty. Game finished! Pot one last time:")
        final_pot()
        print("Final point total: ", totalPoints)
        ranking()
        sys.exit()


while len(play_deck) != 0:

    print("Current point total: ", totalPoints)
    print("Herbs in community garden: ", ", ".join(show_community_garden_status(CommunityGarden.cardList)))
    print("Herbs in private garden: ", ", ".join(show_private_garden_status(PrivateGarden.cardList)), "\n")

    pot_option()

    choices = {1: 'Discard pile', 2: 'Community Garden', 3: 'Private Garden'}
    while True:
        drawn_card = draw_card(random.choice(allOverallID))
        print("Drawn card: ", drawn_card.herbName.upper(), "\n")
        print("Herbs in community garden: ", ", ".join(show_community_garden_status(CommunityGarden.cardList)))
        print("Herbs in private garden: ", ", ".join(show_private_garden_status(PrivateGarden.cardList)), "\n")

        while True:

            try:
                print("Remaining places: ", choices)
                n = int(input('Select where to place card: '
                              '\n 1: Discard pile\n 2: Community garden\n 3: Private garden\n'))
                del choices[n]

            except KeyError:
                print("Place already selected previously. Pick another place\n")
                continue
            except ValueError:
                print("Not a valid input. Enter an appropriate integer.\n")
                continue

            if n == 1:
                discard_card(drawn_card)
                break

            if n == 2:
                plant_2_community_garden(drawn_card)
                break

            if n == 3:
                plant_2_private_garden(drawn_card)
                break

        if not choices:
            break
