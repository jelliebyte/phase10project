import random

#hello there!
choice = ""
game_run = True
cardDeck = []
cardDeck2 = []
colorDeck = []
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
    cardDeck.remove(choice)
    choice = " "
  if choice in cardDeck2:
    cardDeck2.remove(choice)
    choice = " "

def playerTurn():
  global game_run
  global getPlayer
  global cardDeck
  global cardDeck2

  if getPlayer == 1:
    print("player 1")
    print(cardDeck)
    playCard()
    print(cardDeck)
    print(" ")
    getPlayer = 2

  elif getPlayer == 2:
    print("player 2")
    print(cardDeck2)
    playCard()
    print(cardDeck2)
    print(" ")
    getPlayer = 1


while game_run:
  playerTurn()
