# Herbaceous SPV

Herbaceous SPV is the Single Player Variant of Steve Finn, Eduardo Baraf, and Beth Sobel's 2017 flavorful Herbaceous board game. The single player rules have been developped by Keith Matejka. 

[Herbaceous BGG link](https://boardgamegeek.com/boardgame/195314/herbaceous)

This is a fan project to see if it is possible to replicate the Herbaceous mechanics/engine in Python as a text-based game. Although it is not perfect, it should run on linux and Mac with Python 3.6. The game is played through command line inputs. This was not made for monetary reasons (as it is on github) but only as a fun side-project and proof of concept.

### Gameplay screenshot

![Gameplay screenshot](https://github.com/anhtienton/herbaceous/blob/master/herbaceous_SPV_img.png)

## Rules

### Initial setup
36 cards are kept from the original 72 deck for a playthrough. 
* 1 card is drawn to create the discard pile
* 2 cards are placed into the Community Garden
* 3 cards are placed into the Private Garden

### Plant step
Three cards are drawn from the deck. Each card is drawn one at a time, and deciding where to place each card. In any order:
* Private Garden
* Community Garden
* Discard pile

The same location cannot be selected twice in the same set of 3 cards

### Potting your herbs
Before the plant step, you may choose to pot your herbs in one of the 4 containers. You may pick any herbs that are in either the Community Garden or the Private Garden as long as they respect the limits of each container.

### Containers
There are 4 different containers in which you may pot herbs in. 
* Large pot: All the herbs in this container must be of the same type (1 to 7 herbs)
* Wooden planter: All the herbs in this container must be uniquer (1 to 7 herbs)
* Small pots: The herbs must be potted in pairs. Each pair must be different from the other (2 to 12 herbs)
* Glass jars: Any 3 herbs can be potted into this container. It may contain special herbs for bonus points.

### Special rules
If at any time, a 5th card is added to the Community Garden, discard all cards from the Community Garden into the Discard Pile.

During the first turn, it is possible to pot any herbs if desired.

### Game end
The game can end in 2 ways:
* There are no available containers to pot herbs
* There is no more cards to draw. You are then given one last chance to pot any remaining herbs.

## Disclaimer
2018 anhtienton

Distributed for Free with permission of the publisher. Pencil First Games, LLC reserves all rights to the digital versions of Herbaceous in all forms and has copyright. 

All game ideas and rules belong to Pencil First Games and the game creators (Eduardo Baraf, Steve Finn, Beth Sobel, and Keith Matejka). Please make sure to give them credit for such a pleasant and relaxing game. This is just a recreation of their game on Python.

[Pencil First Games](http://www.pencilfirstgames.com/)
