import random 

numberOfDice = int(input('Input the number of dice you want to throw? '))

def throughDice(numberOfDice):
    totalScore = 0
    i = 0
    while i < numberOfDice:
        totalScore += random.randint(1,6)
        i += 1

    print(f'Total score by {numberOfDice} dice is {totalScore}')

throughDice(numberOfDice)