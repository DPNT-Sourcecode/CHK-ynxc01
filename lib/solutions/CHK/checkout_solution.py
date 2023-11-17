

# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict
prices = {"A":50,"B":30,"C":20,"D":15,"E":40}
offers = {"A":[(5,200),(3,130)],"B":[(2,45)], "E":[(2,80)]}

def applyDisc(x,y,res,shoppingFreq) -> None:
    if x in shoppingFreq and shoppingFreq[x] >=2 and y in shoppingFreq:
        free = shoppingFreq[x] // 2
        if shoppingFreq[y] >= free:
            res -= free*prices[y]
        else:
            res -= shoppingFreq[y]* prices[y]

def checkout(skus: str) -> int:
    res = 0
    n = len(skus)
    shoppingFreq = defaultdict(int)

    for x in range(n):
        if skus[x] in prices:
            shoppingFreq[skus[x]]+=1
        else:
            return -1
    
    # iterate through all the items
    for item, freq in shoppingFreq.items():
        
        if item in offers:
            for count, price in sorted(offers[item], reverse=True):
                while freq >= count:
                    res += price
                    freq -= count
        res += freq * prices[item]
        
        
        applyDisc('E','B',res,shoppingFreq)
                
    return res


