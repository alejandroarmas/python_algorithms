

def fibonacci(n):
    """
    Return n-th fibonacci number using Dynamic Programming. 

    Bottom-up Strategy: Memo dictionary saving the results
    of subsequent sub-problem solutions until we reach the final solution.  
    """
    memo = {0: 0, 1: 1}
    for i in range(n + 1):
        if i not in memo:
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]
    
