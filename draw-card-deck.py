from random import randint, choice

suit = ['Clubs', 'Daimonds', 'Hearts', 'Spades']
face = {
    'Ace' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 11,
    'Queen' : 12,
    'King' : 13,
}

def drawCard():
    drawedSuit = suit[randint(0,3)]
    drawedFace, drawedValue = choice(list(face.items()))
    return drawedSuit, drawedFace, drawedValue

print(drawCard())