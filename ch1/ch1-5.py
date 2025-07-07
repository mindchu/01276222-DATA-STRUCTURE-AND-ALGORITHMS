bidder = [int(inp) for inp in input("Enter All Bid : ").split()]
if len(bidder) == 1:
    print("not enough bidder")
else:
    bidder.sort()
    if bidder[-1] == bidder[-2]:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {bidder[-1]} need to pay {bidder[-2]}")