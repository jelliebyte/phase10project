import random
#hello there!
choice = 0
game_run = True
cardDeck = []
cardDeck2 = []
colorDeck = []
getPlayer = random.randint(1, 2)
getPlayer = random.randint(1, 2)
randCard = random.randint(1, 3)

cardColors = [
    f"R{random.randint(1,9)}", f"G{random.randint(1,9)}",
    f"B{random.randint(1,9)}", f"Y{random.randint(1,9)}", "SKIP", "WILD"
]

for i in range(1, 9):
  cardDeck.append(random.choices(cardColors, weights=[10, 10, 10, 10, 1, 1]))

def playCard():
  global choice
  choice = input("What would you like to play? ")
  if choice in cardDeck:
    cardDeck.remove(choice)
  if choice in cardDeck2:
    cardDeck2.remove(choice)

def playerTurn():
  global game_run
  global getPlayer
  global choice

  if getPlayer == 1:
    print("player 1")
    print(cardDeck)
    playCard()
    print(cardDeck)
    getPlayer = 2

  elif getPlayer == 2:
    print("player 2")
    print(cardDeck)
    playCard()
    print(cardDeck)
    getPlayer = 2


while game_run:
  playerTurn()