import random

#hello there!
choice = ""
game_run = True
cardDeck = []
cardDeck2 = []
colorDeck = []
discardPile = []
getPlayer = 1
randCard = random.randint(1, 3)

cardColors = [
    f"R{random.randint(1,9)}", f"G{random.randint(1,9)}",
    f"B{random.randint(1,9)}", f"Y{random.randint(1,9)}", "WILD", "SKIP"
]

for i in range(1, 9):
  cardDeck.append(random.choice(cardColors))
  cardDeck2.append(random.choice(cardColors))


def playCard():
  global choice
  global cardDeck
  global cardDeck2

  choice = input("What would you like to play? ")
  if choice in cardDeck:
    discardPile.insert(1, cardDeck.pop(cardDeck.index(choice))) #inserts the popped index from carddeck into the discard pile, we get the input via input
  elif choice in cardDeck2:
    discardPile.insert(1, cardDeck2.pop(cardDeck2.index(choice))) #https://www.geeksforgeeks.org/python-move-one-list-element-to-another-list/
  choice = " "


def playerTurn():
  global game_run
  global getPlayer
  global cardDeck
  global cardDeck2
  global discardPile

  if getPlayer == 1:
    print("player 1")
    print(cardDeck)
    playCard()
    print(cardDeck)
    print(discardPile)
    print(" ")
    getPlayer = 2

  elif getPlayer == 2:
    print("player 2")
    print(cardDeck2)
    playCard()
    print(cardDeck2)
    print(discardPile)
    print(" ")
    getPlayer = 1


while game_run:
  playerTurn()
