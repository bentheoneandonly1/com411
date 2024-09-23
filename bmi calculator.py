lives = int(input("Enter number of lives: "))
energy = int(input("Enter energy: "))
shield = int(input("Enter shield: "))
global lives2
global energy2
global shield2
lives2 = ("")
energy2 = ("")
shield2 = ("")
while lives > 0:
    lives2 += "♥"
    lives -= 1
while energy > 0:
    energy2 += "♦"
    energy -= 1
while shield > 0:
    shield2 += "♦"
    shield -= 1
print("Lives:  "+lives2)
print("Energy:  "+energy2)
print("Shield:  "+shield2)