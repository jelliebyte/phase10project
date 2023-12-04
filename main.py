import random

#hello there!
game_run = True
cardDeck = []
cardDeck2 = []
colorDeck = ["Red", "Green", "Yellow", "Blue"]
getPlayer = random.randint(1, 2)
randCard = random.randint(1, 3)

for card in range(1, 9):
  cardDeck.append(random.randrange(1, 9) + randCard)
  cardDeck.append(random.sample(colorDeck, k=1))
  cardDeck2.append(random.randrange(1, 9) + randCard)
  cardDeck2.append(random.sample(colorDeck, k=1))


def playerTurn():
  global getPlayer
  global game_run
  if getPlayer == 1:
    print("player 1")
    print(cardDeck)
    getPlayer = 2
  else:
    print("player 2")
    print(cardDeck2)
    game_run = False


while game_run:
  playerTurn()
