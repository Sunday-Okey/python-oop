
# https://realpython.com/python-data-classes/

from dataclasses import dataclass
from collections import namedtuple
import attr
from dataclasses import make_dataclass
from typing import Any, List
from math import asin, cos, radians, sin, sqrt
from dataclasses import field, fields
from random import sample
from pympler import asizeof
from timeit import timeit

# They are cclasses that typically contains mainly data
# They provide a convinient way to store data and allow value retrieval by attribute look-up


@dataclass
class DataClass:
    name: str
    value: int


test = DataClass('hello world',  1234)
print(test.name)
print(test.value)

# Comparison to Standard Classes
# Dataclasses are creating using the dataclass decorator


@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_heart = DataClassCard('Q', 'Hearts')
print(queen_of_heart.rank)
print(queen_of_heart == DataClassCard('Q', 'Hearts'))
print(queen_of_heart)


# Regular or Standard Class
class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                "(rank={self.rank!r}), suit={self.suit!r})")

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts == RegularCard('Q', 'Hearts'))

# DataClass Methods
# __repl__() - Representation
# __eq__() - Simple Comparisons

# Alternatives to Data Classess
queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}

# Problems with Tuples and Dictionaries
# Remembering a Variable is a Specific Data Type
# Order Attributes for Tuples
# Consistent Attribute Names for Dictionaries
NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
queen_of_hearts = NamedTupleCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == NamedTupleCard('Q', 'Hearts'))
print(queen_of_hearts == ('Q', 'Hearts'))


Person = namedtuple('Person', ['first_initial', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')
print(ace_of_spades == Person('A', 'Spades'))

card = NamedTupleCard('7', 'Diamonds')
# card.rank = 9


@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()


queen_of_hearts = AttrsCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == AttrsCard('Q', 'Hearts'))

# Basic Data Classes


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


pos = Position('Oslo', 10.8, 59.9)
print(pos.lat)
print(f"{pos.name} is at {pos.lat}N, {pos.lon}E")

# Position = make_dataclass('Position', ['name', 'lat', 'lon'])
# A dataclass is a regular python class that has basic model methods
# It's is easy to add default values

print(Position('Null Island'))
print(Position('Greenwich', lat=51.8))
print(Position('Vancouver', lon=-123.1, lat=49.9))

# Type Hints are Mandatory in dataclasses


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


print(Position(3.14, 'pi day', 2018))

# A dataclass is just a regular class
# You can freely add


@dataclass
class DataClass:
    name: str

    def method(self):
        return True


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth Radius in Kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1)/2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1)/2)**2
             )
        return 2 * r * asin(sqrt(h))


oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
print(oslo.distance_to(vancouver))


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)

# Advanced Default values
RANKS = "2 3 4 5 6 7 8 9 10 J Q K Q A".split()
SUITS = '♠ ♢ ♡ ♣'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


# print(make_french_deck())
@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)


# print(Deck())
@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})


# print(fields(Position))
lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)

# Representations
# repr(obj) - obj.__repr__()
# str(obj) - obj.__str__()


@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.suit}{self.rank}"


ace_of_spades = PlayingCard('A', suit='♠')
print(ace_of_spades)
# print(Deck())


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"


# print(Deck())

# Comparison
queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
# print(ace_of_spades > queen_of_hearts)

# @dataclass Decorator Parameters


@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.suit}{self.rank}"


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
# print(ace_of_spades > queen_of_hearts)

card = PlayingCard('Q', '♡')
print(RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit))


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) *
                           len(SUITS) + SUITS.index(self.suit))

    def __str__(self):
        return f"{self.suit}{self.rank}"


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades > queen_of_hearts)

print(Deck(sorted(make_french_deck())))

print(Deck(sample(make_french_deck(), k=10)))

# Immutable Data Classes


@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


pos = Position('Oslo', 10.8, 59.9)
print(pos.name)
# pos.name = 'Stockholm'


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str


@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]


queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
print(deck)

deck.cards[0] = ImmutableCard('7', '♢')
print(deck)

# Inheritance


@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str


print(Capital('Oslo', 10.8, 59.9, 'Norway'))


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


# @dataclass
# class Capital(Position):
#     country: str

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capita(Position):
    country: str = 'Unknown'
    lat: float = 40.0


print(Capital("Madrid", lon=0.0, lat=40.0, country='Spain'))

# Optimizing Data Classes
# Slots are used to make classes faster and take less memory


@dataclass
class SimplePosition:
    name: str
    lon: str
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float


simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
print(asizeof.asizeof(simple))
print(asizeof.asizeof(slot))
print(timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals())
      )
print(timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals())
      )
