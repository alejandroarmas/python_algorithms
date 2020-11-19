

def coinFlipping(n):
    """
    For n amount of cents, return the minimal amount of currency in coins.

    Top-Down Approach (Memoization): Memo dictionary stores already solved
    subproblems to reuse and avoid recomputing. It's essentially recursion 
    but optimized to avoid recomputing results. 
    """
    COINS = {
        "dollar": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

    memo = {}

    def __coinFlipping(change):

        if change not in memo:
            # Base case (if n is equal to 0.01, 0.05, 0.10, 0.25..)
            if change in COINS.values():
                memo[change] = 1
            else:
                results = []
                coins = [coin for coin in COINS.values() if coin < change]
                for coin in coins:
                    results.append(__coinFlipping(change - coin))
                memo[change] = 1 + min(results)
        return memo[change]         
            
    __coinFlipping(n)
    
    return memo[n]

