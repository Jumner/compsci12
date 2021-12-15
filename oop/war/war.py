import time
import random;

class Card:
  _valueDictionary = {'A': 1, 'J':11, 'Q':12, 'K': 13}
  def __init__(self, v, s):
    self._value = v
    self._suite = self

  def __str__(self):
    return f'{self.value()}'

  def value(self):
    if self._value in Card._valueDictionary:
      return Card._valueDictionary[self._value]
    else:
      return self._value
  
  def __lt__(self, other):
    return self.value() < other.value()
  def __gt__(self,other):
    return self.value() > other.value()
  def __eq__(self,other):
    return self.value() == other.value()

class Deck:
  _numCards = 52
  _cardValues = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
  _suits = ['hearts', 'spades', 'clubs', 'spades']
  def __init__(self):
    self.cards = self._generateCards()
  
  def _generateCards(self):
    d = []
    for s in self._suits:
      for v in self._cardValues:
        d.append(Card(v,s))
    return d
  
  def shuffle(self):
    random.shuffle(self.cards)
  
  def first_half(self):
    return self.cards[:self._numCards//2]
  def last_half(self):
    return self.cards[-self._numCards//2:]

class Player:
  def __init__(self, cards):
    self.cards = cards
    
  def __str__(self):
    cardStrings = []
    for card in self.cards:
      cardStrings.append(f'{card}')
    return f'{cardStrings}'

  def play(self, pile):
    if len(self.cards) == 0:
      return False
    pile.add(self.cards.pop())
    return True

  def add(self, pile):
    while len(pile.cards) > 0:
      self.cards.insert(0,pile.cards.pop())

class Pile:
  def __init__(self):
    self.cards = []

  def __str__(self):
    cardStrings = []
    for card in self.cards:
      cardStrings.append(f'{card}')
    return f'{cardStrings}'

  def add(self, card):
    self.cards.insert(0,card)
  
d = Deck()
d.shuffle()
p1 = Player(d.first_half())
p2 = Player(d.last_half())
pile = Pile()
print("yo")
# print(p1)
# print(p2)
round = 1
while(p1.play(pile) and p2.play(pile)):
  print(f'round {round}:')
  round += 1
  # print(p1)
  # print(p2)
  # print(pile)
  # print(pile.cards)
  if pile.cards[1] > pile.cards[0]:
    p1.add(pile)
  elif pile.cards[0] > pile.cards[1]:
    p2.add(pile)
  print(p1)
  print(p2)
  time.sleep(2)
  # print(len(pile.cards))
