import random
#hello there!
choice = 0
game_run = True
cardDeck = []
colorDeck = []
getPlayer = random.randint(1, 2)
getPlayer = random.randint(1, 2)
randCard = random.randint(1, 3)

cardColors = [
    f"R{random.randint(1,9)}", f"G{random.randint(1,9)}",
    f"B{random.randint(1,9)}", f"Y{random.randint(1,9)}"
]

for i in range(1, 9):
  cardDeck.append(random.choice(cardColors))

def playCard():
  global choice
  if choice in cardDeck:
    cardDeck.remove(choice)

def playerTurn():
  global game_run
  global getPlayer
  global choice

  if getPlayer == 1:
    print("player 1")
    print(cardDeck)
    choice = input("What would you like to play? ")
    playCard()
    print(cardDeck)
    getPlayer = 2

  elif getPlayer == 2:
    print("player 2")
    print(cardDeck)
    choice = input("What would you like to play? ")
    playCard()
    print(cardDeck)


while game_run:
  playerTurn()