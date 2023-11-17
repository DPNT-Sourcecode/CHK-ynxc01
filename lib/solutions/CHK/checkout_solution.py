

# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict
prices = {"A":50,"B":30,"C":20,"D":15,"E":40}
offers = {"A":(3,130),"B":(2,45),"E":(2,0,prices["B"])}
def checkout(skus: str) -> int:
    if type(skus) is not str:
        return -1
    
    shoppingFreq = defaultdict(int)
    res = 0
    n = len(skus)
    for x in range(n):
        if not skus[x] in prices:
            return -1
        shoppingFreq[skus[x]]+=1
    
    # iterate through all the items
    for item in shoppingFreq.keys():
        
        freq = shoppingFreq[item]
        # if the item is in the offer check if it's fulfilled
        if not item in offers:
            res += prices[item]*freq
        else:
            q, deal = offers[item]
            # calculate how many offers can be fulfilled
            totalOfferFulfilled = freq// q
            totalStockLeft = freq % q
            
            res+= totalOfferFulfilled*deal
            res+= totalStockLeft*prices[item]
        
    return res


