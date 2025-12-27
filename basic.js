function countCoins(cents) {
  const coins = [25, 10, 5, 1];
  const ways = new Array(cents + 1).fill(0);
  ways[0] = 1; // There's exactly 1 way to make 0 cents
  
  for (const coin of coins) {
    for (let amount = coin; amount <= cents; amount++) {
      ways[amount] += ways[amount - coin];
    }
  }
  
  return ways[cents];
}
