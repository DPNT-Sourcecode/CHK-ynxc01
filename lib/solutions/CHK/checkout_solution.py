

# noinspection PyUnusedLocal
# skus = unicode string
from collections import defaultdict
prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35,
        'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
    }
offers = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(10, 80), (5, 45)],
    'K': [(2, 150)],
    'P': [(5, 200)],
    'Q': [(3, 80)],
    'V': [(3, 130), (2, 90)],
    'U': [(3, 80)],
}

def checkout(skus: str) -> int:
    res = 0
    n = len(skus)
    shoppingFreq = defaultdict(int)

    for x in range(n):
        if skus[x] in prices:
            shoppingFreq[skus[x]]+=1
        else:
            return -1
    
    free = shoppingFreq.get('E',0)//2
    if 'B' in shoppingFreq:
        shoppingFreq['B'] = max(0, shoppingFreq['B'] - free)
        
    free = shoppingFreq.get('N',0)//2
    if 'M' in shoppingFreq:
        shoppingFreq['M'] = max(0, shoppingFreq['M'] - free)
    
    free = shoppingFreq.get('R',0)//2
    if 'Q' in shoppingFreq:
        shoppingFreq['Q'] = max(0, shoppingFreq['Q'] - free)
    
    # iterate through all the items
    for item, freq in shoppingFreq.items():
        
        if item in offers:
            for count, price in sorted(offers[item], reverse=True):
                while freq >= count:
                    res += price
                    freq -= count
        res += freq * prices[item]
        
                
    return res
