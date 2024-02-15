bidding_item = input("What is the bidding item?")
reserve_price = int(input("What is the reserve price?"))
highest_bid = 0
bid = 0
print(f"The item is a {bidding_item}. Let the bidding begin!")
while bid != -1:
    bid = int(input("How much are you bidding?"))
    if bid > highest_bid:
        bid += highest_bid
        print(f"You have the highest bid of ${highest_bid}")
    elif bid < highest_bid:
        print(f"You don't have the highest bid! Put a bid bigger than ${highest_bid} to\n"
              f"have the highest bid")
if highest_bid > reserve_price:
    print(f"You won the auction for the {bidding_item} for {highest_bid}!")
else:
    print(f"Unfortunately, your highest bid (${highest_bid}) wasn't higher than \n"
          f"the reserve price and you didn't get the {bidding_item}. Better luck next time!")
