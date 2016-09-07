#!/usr/bin/python

class Auction:
    """This class represents an auction of multiple ad slots to multiple advertisers"""
    query = ""
    bids = []

    def __init__(self, term, bids1=[]):
        self.query = term
        for b in bids1:
            j = 0
            while j < len(self.bids) and float(b.value) < float(self.bids[j].value):
                j += 1
            self.bids.insert(j, b)

    '''
	This method accepts a Vector of slots and fills it with the results
	of a VCG auction. The competition for those slots is specified in the bids Vector.
	@param slots a Vector of Slots, which (on entry) specifies only the clickThruRates
	and (on exit) also specifies the name of the bidder who won that slot,
	the price said bidder must pay,
	and the expected profit for the bidder.
	'''

    def executeVCG(self, slots):
        print ("executeVCG: Implemented")

        # the number of bidders
        numBidder = len(self.bids)
        # the number of slots
        numSlots = len(slots)

        # 1. slots < bidders
        if numSlots < numBidder:

            # the last slot
            slots[numSlots - 1].price = slots[numSlots - 1].clickThruRate * self.bids[numSlots].value
            slots[numSlots - 1].bidder = self.bids[numSlots - 1].name

            # price and bidder name
            for j in range(numSlots - 2, -1, -1):
                slots[j].price = (slots[j].clickThruRate - slots[j + 1].clickThruRate) * self.bids[j+1].value + slots[j + 1].price
                slots[j].bidder = self.bids[j].name

            # profit
            for m in range(numSlots - 1, -1, -1):
                slots[m].profit = self.bids[m].value * slots[m].clickThruRate - slots[m].price

        # 2. slots >= bidder
        else:
            slots[numBidder - 1].bidder = self.bids[numBidder - 1].name
            for j in range(numBidder - 2, -1, -1):
                slots[j].price = (slots[j].clickThruRate - slots[j + 1].clickThruRate) * self.bids[j+1].value + slots[j + 1].price
                slots[j].bidder = self.bids[j].name
            for n in range(numBidder - 1, -1, -1):
                slots[n].profit = self.bids[n].value * slots[n].clickThruRate - slots[n].price
