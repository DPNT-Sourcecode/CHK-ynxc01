

# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict
prices = {"A":50,"B":30,"C":20,"D":15,"E":40}
offers = {"A":[(5,200),(3,130)],"B":(2,45)}
free_items = {"E":(2,"B",1)}
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
            
        if item in free_items:
            q, other, q2 = free_items[item]
            totalOfferFulfilled = freq// q
            res += totalOfferFulfilled * (prices[other]*q2)
        
    return res







