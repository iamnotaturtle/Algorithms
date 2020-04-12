# Group of objects is treated the same way
# as a single instance of the same type of object
class Card:
  def show(self):
    pass

class AceHearts(Card):
  def show(self):
    return "Ace of Hearts"

class AceClubs(Card):
  def show(self):
    return "Ace of Clubs"

class CardDeck:
  def __init__(self):
    self.cards = []

  def addCard(self, card):
    self.cards.append(card)

  def showCards(self):
    list(map(lambda card: print(card.show()), self.cards))

deck = CardDeck()
deck.addCard(AceClubs())
deck.addCard(AceHearts())
deck.showCards()