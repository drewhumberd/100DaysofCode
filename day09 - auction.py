from os import system
from supportfiles.art import auction_logo
print(auction_logo)
print("Welcome to the auction.")
bid_list = {}
def add_bidder(bidder_name, bid):
    bid_list[bidder_name] = int(bid)
auction = True
while auction == True:
  bidder_name = input("What is your name?\n")
  bid = input("What is your bid in dollars?\n")
  add_bidder(bidder_name, bid)
  more_bidders = input("Are there any more bidders? y for yes or n for no\n")
  if more_bidders == "y":
    system("cls")
  else:
    auction = False
winning_bid = max(bid_list.values())
winner = max(bid_list, key=bid_list.get)
system("cls")
print(f"The winner is {winner} with a bid of ${winning_bid}.")