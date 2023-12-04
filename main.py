import random

#hello there!
game_run = True
cardDeck = []
cardDeck2 = []
colorDeck = ["Red", "Green", "Yellow", "Blue"] #0-3
# getPlayer = random.randint(1, 2)
getPlayer = 1
randCard = random.randint(1, 3)

for card in range(1, 9):
  cardDeck.append(random.randrange(1, 9) + randCard)
  cardDeck.append(random.sample(colorDeck, k=1))
  cardDeck2.append(random.randrange(1, 9) + randCard)
  cardDeck2.append(random.sample(colorDeck, k=1))

def playCard():
  choice = int(input("What would you like to play? "))
  if choice in cardDeck:
    cardDeck.remove(choice)
  print(cardDeck)

def playerTurn():
  global getPlayer
  global game_run
  if getPlayer == 1:
    print("player 1")
    print(cardDeck)
    playCard()
    getPlayer = 2
  else:
    print("player 2")
    print(cardDeck2)
    game_run = False


while game_run:
  playerTurn()
