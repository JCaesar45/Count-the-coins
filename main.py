def countCoins(cents):
    # Define the coin denominations
    coins = [25, 10, 5, 1]
    # Initialize a list to store the number of ways to make change for each amount
    ways = [0] * (cents + 1)
    ways[0] = 1  # There is exactly 1 way to make change for 0 cents
    
    # For each coin, update the ways array
    for coin in coins:
        for amount in range(coin, cents + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[cents]
