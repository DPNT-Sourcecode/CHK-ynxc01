

# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict
prices = {"A":50,"B":30,"C":20,"D":15,"E":40,"F":10}
offers = {"A":[(5,200),(3,130)],"B":[(2,45)], "E":[(2,80)], "F":[(2,20)]}



def checkout(skus: str) -> int:
    res = 0
    n = len(skus)
    shoppingFreq = defaultdict(int)

    for x in range(n):
        if skus[x] in prices:
            shoppingFreq[skus[x]]+=1
        else:
            return -1
    
    free = shoppingFreq['E']//2
    if 'B' in shoppingFreq:
        shoppingFreq['B'] = max(0, shoppingFreq['B'] - free)
    
    free = shoppingFreq['F']//2
    if 'F' in shoppingFreq:
        shoppingFreq['F'] = max(0, shoppingFreq['F'] - free)
    
    # iterate through all the items
    for item, freq in shoppingFreq.items():
        
        if item in offers:
            for count, price in sorted(offers[item], reverse=True):
                while freq >= count:
                    res += price
                    freq -= count
        res += freq * prices[item]
        
                
    return res


