#from fastapi import FastAPI, HTTPException
import requests

scores = []

def makedeck():
# API URL
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=52"  # Example API

# Make a GET request
    response = requests.get(url)

    deck = []

# Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        card_data=(data['cards'])

        for x in card_data:
            deck.append(x['value'])
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

    return deck



def checkvalue(card):
    if card == "JACK":
        return 11
    if card == "QUEEN":
        return 12
    if card == "KING":
        return 13      
    if card == "ACE":
        return 14
    return card
def game(deck):
    i=0
    score = 0
    for x in deck:
        i += 1
        card_value = int(checkvalue(x))
        print("Current card: ", x)
        next_card = deck[i]
        next_card_value = int(checkvalue(next_card))
        print("next card value:", next_card_value)
        choice = input("\nIs the next higher or lower? Enter h or l: ")
        if choice == "h" or choice == "l":
            if ((int(next_card_value) > int(card_value)) and (choice == "h")) or ((int(next_card_value) < int(card_value)) and choice == "l"):
                score += 1
                print("correct. Your current score is", score)
            else:
                if(card_value == next_card_value):
                    print("Values were equal going to next cards.")
                else:
                    print("incorrect, your final score is", score)
                    return score
        else:
            print("invalid input going to next card")
while True:
    deck = makedeck()
    score = game(deck)
    scores.append(score)
    newgame = input("Would you like to play a newgame? y/n ")
    if newgame == "y":
        continue
    else:
        break

maxscore = 0

avgscore = 0.0
for x in scores:
    avgscore += x
    if x > maxscore:
        maxscore = x

avgscore /= len(scores)


print("\n"*3)
print("Your average score was:", avgscore)
print("Your max score was", maxscore)
print("\n"*3)
