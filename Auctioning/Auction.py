import os
from art import logo

def findHighestBidder(biddingRecord):
    highestBidder = 0
    winner = ""
    for i in biddingRecord:
        bidAmount = biddingRecord[i] 
        if bidAmount > highestBidder:
            highestBidder = bidAmount
            winner = i
    print(f"The winner is {winner} with the bid of ${highestBidder}")

print(logo)
bids = {}
biddingFinished = False


while not biddingFinished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    shouldContinue = input("Are there any other bidders? Type 'yes or 'no'.")
    if shouldContinue == "no":
        biddingFinished = True
        findHighestBidder(bids)
    elif shouldContinue == "yes":
        os.system('cls')
