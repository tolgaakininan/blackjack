import random as rand
import time
import os
def calculatePoint(liste):
    point=0
    for cardPoint in liste:
        point=point+cardPoint
    return point
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
play=input("Want to play blackjack?, type 'y' or 'n'").lower()

computerPast21=False
playerPast21=False
tekrar=True
while tekrar is True:
    devamMi=True
    if play=='y':
        print("""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """)
        playerCards=[]
        computerCards=[]
        playerCards.append(rand.choice(cards))
        playerCards.append(rand.choice(cards))
        computerCards.append(rand.choice(cards))
        print(playerCards)
        playerPoint=calculatePoint(playerCards)
        computerPoint=calculatePoint(computerCards)
        print(f"Your current score:{playerPoint}")
        print(f"Computer's first card:{computerCards}")
        while devamMi:
            anotherCard=input("Type 'y' for another card, type 'n' to pass: ").lower()
            if anotherCard=='y':
                playerCards.append(rand.choice(cards))
                print(playerCards)
                playerPoint=calculatePoint(playerCards)
                
            elif anotherCard=='n':
                computerCards.append(rand.choice(cards))
                computerPoint=calculatePoint(computerCards)
                print(computerCards)
                if playerPoint>computerPoint:
                    computerCards.append(rand.choice(cards))
                    print(computerCards)
                    computerPoint=calculatePoint(computerCards)
                
                devamMi=False
            if playerPoint>21:
                print("You past 21.")
                print("Computer has won!")
                playerPast21=True
                break
            elif computerPoint>21:
                print("Computer past 21.")
                print("Player has won!")
                computerPast21=True
                break
            print(f"Your current score:{playerPoint}")
            print(f"Computers current score:{computerPoint}")
            time.sleep(2)
            os.system("cls")
        print(f"Your score:{playerPoint}")
        print(f"Computers score:{computerPoint}")
        if computerPast21 is False and playerPast21 is False and playerPoint>computerPoint:
            print("Player has won!")
        elif computerPast21 is False and playerPast21 is False and playerPoint<computerPoint:
            print("Computer has won!")
        elif computerPast21 is False and playerPast21 is False and playerPoint==computerPoint:
            print("Draw!")
        play=input("Want to play blackjack again?, type 'y' or 'n'").lower()
        if play=='n':
            tekrar=False
        os.system("cls")
print("Take Care!")
